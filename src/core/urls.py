"""Clauselocator URL configuration."""

from django.urls import include, path

urlpatterns = [
    path("api/clauses/", include("clauses.urls", namespace="clauses")),
]
