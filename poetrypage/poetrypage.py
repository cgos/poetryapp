#!/usr/bin/python

from flask import Flask, request, render_template, redirect, url_for
import simplejson as json
import requests
import sys
from json2html import *
import logging
import requests

# These two lines enable debugging at httplib level (requests->urllib3->http.client)
# You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# The only thing missing will be the response.body which is not logged.
try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1

app = Flask(__name__)
logging.basicConfig(filename='microservice.log',filemode='w',level=logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.DEBUG)

from flask_bootstrap import Bootstrap
Bootstrap(app)

poemprovider = {
    "name" : "http://localhost:8080",
    "endpoint" : "poem",
    "children" : []
}

poempage = {
    "name" : "http://localhost:9080",
    "endpoint" : "poetrypage",
    "children" : [poemprovider]
}

service_dict = {
    "poempage" : poempage,
    "poemprovider" : poemprovider,
}

def getForwardHeaders(request):
    headers = {}

    user_cookie = request.cookies.get("user")
    if user_cookie:
        headers['Cookie'] = 'user=' + user_cookie

    incoming_headers = [ 'x-request-id',
                         'x-b3-traceid',
                         'x-b3-spanid',
                         'x-b3-parentspanid',
                         'x-b3-sampled',
                         'x-b3-flags',
                         'x-ot-span-context'
    ]

    for ihdr in incoming_headers:
        val = request.headers.get(ihdr)
        if val is not None:
            headers[ihdr] = val
            print ("incoming: "+ihdr+":"+val)

    return headers


# The UI:
@app.route('/')
@app.route('/index.html')
def index():
    """ Display gifPage"""
    global gifPage

    table = json2html.convert(json=json.dumps(gifPage),
                              table_attributes="class=\"table table-condensed table-bordered table-hover\"")

    return render_template('index.html', serviceTable=table)


@app.route('/health')
def health():
    return 'page is healthy'


@app.route('/login', methods=['POST'])
def login():
    user = request.values.get('username')
    response = app.make_response(redirect(request.referrer))
    response.set_cookie('user', user)
    return response


@app.route('/logout', methods=['GET'])
def logout():
    response = app.make_response(redirect(request.referrer))
    response.set_cookie('user', '', expires=0)
    return response


@app.route('/poetrypage')
def front():
    poem_id = 0 # TODO: replace default value
    headers = getForwardHeaders(request)
    user = request.cookies.get("user", "")
    #product = getProduct(product_id)
    #detailsStatus, details = getProductDetails(product_id, headers)
    #reviewsStatus, reviews = getProductReviews(product_id, headers)
    #poem = getPoem(poet_id)
    poemStatus, poem = getPoemTxt(poem_id, headers)
    return render_template(
        'poetrypage.html',
        poemStatus=poemStatus,
        poem=poem)


# The API:
@app.route('/api/v1/products')
def productsRoute():
    return json.dumps(getProducts()), 200, {'Content-Type': 'application/json'}


@app.route('/api/v1/products/<product_id>')
def productRoute(product_id):
    headers = getForwardHeaders(request)
    status, details = getProductDetails(product_id, headers)
    return json.dumps(details), status, {'Content-Type': 'application/json'}


@app.route('/api/v1/products/<product_id>/reviews')
def reviewsRoute(product_id):
    headers = getForwardHeaders(request)
    status, reviews = getProductReviews(product_id, headers)
    return json.dumps(reviews), status, {'Content-Type': 'application/json'}


@app.route('/api/v1/products/<product_id>/ratings')
def ratingsRoute(product_id):
    headers = getForwardHeaders(request)
    status, ratings = getProductRatings(product_id, headers)
    return json.dumps(ratings), status, {'Content-Type': 'application/json'}



# Data providers:
def getProducts():
    return [
        {
            'id': 0,
            'title': 'The Comedy of Errors',
            'descriptionHtml': '<a href="https://en.wikipedia.org/wiki/The_Comedy_of_Errors">Wikipedia Summary</a>: The Comedy of Errors is one of <b>William Shakespeare\'s</b> early plays. It is his shortest and one of his most farcical comedies, with a major part of the humour coming from slapstick and mistaken identity, in addition to puns and word play.'
        }
    ]

def getPoems():
    return [
            {
                'id': 0,
                'poet': 'Billy Collins',
                'title': 'The Afterlife',
                'txt' : "While you are preparing for sleep, brushing your teeth,<br /> or riffling through a magazine in bed,<br /> the dead of the day are setting out on their journey.<br /> <br /> They're moving off in all imaginable directions,<br /> each according to his own private belief,<br /> and this is the secret that silent Lazarus would not reveal:<br /> that everyone is right, as it turns out.<br /> you go to the place you always thought you would go,<br /> The place you kept lit in an alcove in your head.<br /> <br /> Some are being shot into a funnel of flashing colors<br /> into a zone of light, white as a January sun.<br /> Others are standing naked before a forbidding judge who sits<br /> with a golden ladder on one side, a coal chute on the other.<br /> <br /> Some have already joined the celestial choir<br /> and are singing as if they have been doing this forever,<br /> while the less inventive find themselves stuck<br /> in a big air conditioned room full of food and chorus girls.<br /> <br /> Some are approaching the apartment of the female God,<br /> a woman in her forties with short wiry hair<br /> and glasses hanging from her neck by a string.<br /> With one eye she regards the dead through a hole in her door.<br /> <br /> There are those who are squeezing into the bodies<br /> of animals--eagles and leopards--and one trying on<br /> the skin of a monkey like a tight suit,<br /> ready to begin another life in a more simple key,<br /> <br /> while others float off into some benign vagueness,<br /> little units of energy heading for the ultimate elsewhere.<br /> <br /> There are even a few classicists being led to an underworld<br /> by a mythological creature with a beard and hooves.<br /> He will bring them to the mouth of the furious cave<br /> guarded over by Edith Hamilton and her three-headed dog.<br /> <br /> The rest just lie on their backs in their coffins<br /> wishing they could return so they could learn Italian<br /> or see the pyramids, or play some golf in a light rain.<br /> They wish they could wake in the morning like you<br /> and stand at a window examining the winter trees,<br /> every branch traced with the ghost writing of snow.<br /> <br /> (And some just smile, forever on)"
            }
           ]


def getPoem(poem_id):
    poems = getPoems()
    if poem_id + 1 > len(poems):
        return None
    else:
        return poems[poem_id]

def getProduct(product_id):
    products = getProducts()
    if product_id + 1 > len(products):
        return None
    else:
        return products[product_id]

def getPoemTxt(poem_id, headers):
    try:
        url = poemprovider['name'] + "/" + poemprovider['endpoint']
        res = requests.get(url, headers=headers, timeout=3.0)
    except:
        res = None
    if res and res.status_code == 200:
        return 200, res.json()
    else:
        status = res.status_code if res is not None and res.status_code else 500
        return status, {'error': 'Sorry, poems are currently unavailable.'}


def getProductDetails(product_id, headers):
    try:
        #url = details['name'] + "/" + details['endpoint'] + "/" + str(product_id)
        url = details['name'] + "/" + details['endpoint']
        res = requests.get(url, headers=headers, timeout=3.0)
    except:
        res = None
    if res and res.status_code == 200:
        return 200, res.json()
    else:
        status = res.status_code if res is not None and res.status_code else 500
        return status, {'error': 'Sorry, product details are currently unavailable for this book.'}


def getProductReviews(product_id, headers):
    ## Do not remove. Bug introduced explicitly for illustration in fault injection task
    ## TODO: Figure out how to achieve the same effect using Envoy retries/timeouts
    for _ in range(2):
        try:
            url = reviews['name'] + "/" + reviews['endpoint'] + "/" + str(product_id)
            res = requests.get(url, headers=headers, timeout=3.0)
        except:
            res = None
        if res and res.status_code == 200:
            return 200, res.json()
    status = res.status_code if res is not None and res.status_code else 500
    return status, {'error': 'Sorry, product reviews are currently unavailable for this book.'}


def getProductRatings(product_id, headers):
    try:
        url = ratings['name'] + "/" + ratings['endpoint'] + "/" + str(product_id)
        res = requests.get(url, headers=headers, timeout=3.0)
    except:
        res = None
    if res and res.status_code == 200:
        return 200, res.json()
    else:
        status = res.status_code if res is not None and res.status_code else 500
        return status, {'error': 'Sorry, product ratings are currently unavailable for this book.'}


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print ("usage: %s port" % (sys.argv[0]))
        sys.exit(-1)

    p = int(sys.argv[1])
    print ("start at port %s" %(p))    
    #fileError = open("stderr.log", "w" )
    #sys.stderr = fileError

    #fileOutput = open("stdout.log", "w")
    #sys.stdout = fileOutput

    app.run(host='0.0.0.0', port=p, debug=True, threaded=True)
