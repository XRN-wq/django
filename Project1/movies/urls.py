from django.urls import path

from . import views

urlpatterns = [
    path("", views.MovieReview.as_view()),
    path("<slug:slug>/", views.MovieDetailView.as_view(), name="movie_detail")
]