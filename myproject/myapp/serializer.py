from dataclasses import fields
from rest_framework import serializers
from .models import Actor, Movies


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class MoviesSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many = True, read_only=True)

    class Meta:
        model = Movies
        fields = "__all__"