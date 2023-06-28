from django.urls import path
from . import views

# setting up some paths/urls
urlpatterns = [
    path('', views.BlogViews.as_view(), name='home'),
    path('<slug:slug>/', views.BlogDetail.as_view(), name='post_detail')
]