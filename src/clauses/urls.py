"""URL configuration for the clauses app."""

from django.urls import path

from clauses.views import LocateClauseView


app_name = "clauses"

urlpatterns = [
    path("locate/", LocateClauseView.as_view(), name="locate"),
]
