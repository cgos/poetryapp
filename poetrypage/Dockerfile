	FROM ubuntu:latest
	RUN apt-get update -y && \
	    apt-get install -y python3-pip python-dev build-essential
	COPY . /app
	ENV POEM_PROVIDER_URL fill
	ENV POET_BIO_URL fill
	WORKDIR /app
	RUN pip3 install -r requirements.txt && \
	    python3 
	EXPOSE 80
	ENTRYPOINT ["python3", "poetrypage.py"]