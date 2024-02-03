from django.urls import path
from . import views

urlpatterns = [
	path ('', views.home, name="home"),
	path ('movies/', views.movies, name="movies"),
	path ('about/', views.about, name="about"),
	path ('navbar/', views.about, name="navbar"),
	path ('food/', views.food, name="food"),
	path ('contact/', views.contact, name="contact"),
	path ('profile/<int:pk>/', views.profile, name="profile"),
	path ('spiderman/', views.spiderman, name="spiderman"),
	path ('mermaid/', views.mermaid, name="mermaid"),
	path ('indiana/', views.indiana, name="indiana"),
	path ('transformers/', views.transformers, name="transformers"),
	path ('cart/', views.cart, name="cart"),
    path ('main/', views.main, name="main"),
    path ('subscription/', views.subscription, name="subscription"),
	path ('update/<int:pk>/', views.update, name="update"),
	path ('delete/<int:pk>/', views.delete, name="delete"),
]