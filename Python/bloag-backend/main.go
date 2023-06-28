package main

import (
	"blog-backend/database"
	"blog-backend/routes"
	"log"

	"github.com/gin-gonic/gin"
)

func checkErr(err error) {
	if err != nil {
		log.Fatal(err)
	}
}

func main() {
	err := database.ConnnectToDatabase()
	checkErr(err)

	r := gin.Default() // sets up a defualt router
	routes.Routes(r)

	// creates a group for the routes.
	// the url will look like this - api/v1/artical

	r.Run()
}
