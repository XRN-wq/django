from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Movie

class MovieReview(ListView):
        model = Movie
        queryset = Movie.objects.filter(draft=False)

class MovieDetailView(DetailView):
    model = Movie
    slug_field = "url"
