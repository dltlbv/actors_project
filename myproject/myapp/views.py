from django.shortcuts import render
from rest_framework import viewsets
from .models import Actor, Movies
from .serializer import ActorSerializer, MoviesSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MoviesViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
