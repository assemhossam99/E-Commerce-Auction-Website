from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('newItem', views.newItem, name="newItem"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('<int:listingID>', views.listingPage, name="listingPage"),
    path('<int:listingID>/addToWatchlist', views.addToWatchlist, name="addToWatchlist")
]
