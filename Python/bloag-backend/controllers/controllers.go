package controllers

import (
	"blog-backend/database"
	"blog-backend/model"
	"log"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
)

func checkErr(err error) {
	if err != nil {
		log.Fatal(err)
	}
}

func GetArticals(c *gin.Context) {
	articals, err := database.GetArticals(10)
	checkErr(err)

	if articals == nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "No Records Found"})
		return
	} else {
		c.JSON(http.StatusOK, gin.H{"data": articals})
	}
}

func GetArticalsId(c *gin.Context) {
	id := c.Param("id")

	articals, err := database.GetArticalById(id)
	checkErr(err)

	// if the title is blank there is probably no artical
	if articals.TITLE == "" {
		c.JSON(http.StatusBadRequest, gin.H{"error": "No Records Found"})
		return
	} else {
		c.JSON(http.StatusOK, gin.H{"data": articals})
	}
}

func AddArtical(c *gin.Context) {
	var json model.Articals

	if err := c.ShouldBindJSON(&json); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	success, err := database.AddArticals(json)

	if success {
		c.JSON(http.StatusOK, gin.H{"message": "Success"})
	} else {
		c.JSON(http.StatusBadRequest, gin.H{"error": err})
	}
}

func UpdateArtical(c *gin.Context) {
	var json model.Articals
	id := c.Param("id")

	if err := c.ShouldBindJSON(&json); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	articalId, err := strconv.Atoi(id)

	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid ID"})
	}

	success, err := database.UpdateArticals(json, articalId)

	if success {
		c.JSON(http.StatusOK, gin.H{"message": "Success"})
	} else {
		c.JSON(http.StatusBadRequest, gin.H{"error": err})
	}
}

func DeleteArtical(c *gin.Context) {
	id := c.Param("id")
	c.JSON(http.StatusOK, gin.H{"message": "deleteArtical" + id + "called"})
}

func Options(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{"message": "getArticals called"})
}
