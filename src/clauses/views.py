"""API views for accessing clause-related logic."""

from rest_framework import authentication, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from clauses.forms import ClauseForm


class LocateClauseView(APIView):
    """View to locate clauses within the provided context."""

    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request: Request) -> Response:
        """Process user-provided parameters and return any relevant data."""
        success, results = False, None
        form = ClauseForm(request.data or None)

        if form.is_valid():
            success, results = form.process()
        errors = form.errors.get_json_data()

        status_code = status.HTTP_200_OK if success else status.HTTP_400_BAD_REQUEST
        return Response(
            data={"success": success, "results": results, "errors": errors},
            status=status_code,
        )
