package routes

import (
	"blog-backend/controllers"

	"github.com/gin-gonic/gin"
)

func Routes(r *gin.Engine) {
	v1 := r.Group("api/v1")
	{
		v1.GET("artical-get", controllers.GetArticals)
		v1.GET("artical-get/:id", controllers.GetArticalsId)
		v1.POST("artical-add", controllers.AddArtical)
		v1.PUT("artical-add/:id", controllers.UpdateArtical)
		v1.DELETE("artical-delete/:id", controllers.DeleteArtical)
		v1.OPTIONS("artical", controllers.Options)
	}
}
