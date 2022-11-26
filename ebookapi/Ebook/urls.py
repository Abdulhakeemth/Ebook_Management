from django.conf.urls import url
from django.contrib import admin
from Ebook import views
from django.urls import path
from . import views


urlpatterns = [
    path('ebooksdetaillist/', views.Ebooksdetiallist.as_view()),
    path('ebooksdetaillist/<int:pk>/', views.EbooksDetail.as_view()),
    path('ratingdetailist/<str:book>/',views.Ratingdetaillist.as_view()),
] 