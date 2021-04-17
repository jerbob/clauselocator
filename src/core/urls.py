"""Clauselocator URL configuration."""

from django.urls import include, path


urlpatterns = [
    path("clauses/", include("clauses.urls", namespace="clauses")),
]
