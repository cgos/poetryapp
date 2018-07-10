package main

import (
    "encoding/json"
    "log"
    "net/http"
    "github.com/gorilla/mux"
)

type Bio struct {
	ID string `json:"id,omitempty"`
	Bio string `json:"bio,omitempty"`
}

var bio []Bio

// our main function
func main() {
    router := mux.NewRouter()

	bio = append(bio, Bio{ID: "0", Bio: "Billy Collins, (born March 22, 1941) is an American poet. He has served as a professor at Lehman College of the City University of New York and is the senior distinguished fellow of the Winter Park Institute, Florida. Collins was considered as a Literary Lion of the New York Public Library (1992) and selected as the New York State Poet for 2004 through 2006. As of 2015, he is a teacher in the MFA program at Stony Brook Southampton."})
	//bio = append(bio, Bio{ID: "1", Bio: "James Douglas Morrison was an American singer-songwriter and poet, best remembered as the lead vocalist of the Doors."})

    router.HandleFunc("/poetbio", GetBio).Methods("GET")
    log.Fatal(http.ListenAndServe(":8888", router))
}

func GetBio(w http.ResponseWriter, r *http.Request){
	json.NewEncoder(w).Encode(bio[0])
}