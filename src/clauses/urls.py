"""URL configuration for the clauses app."""

from django.urls import re_path

from clauses.views import LocateClauseView


app_name = "clauses"

urlpatterns = [
    re_path("locate/?$", LocateClauseView.as_view(), name="locate"),
]
