"""Forms used in the 'clauses' app."""

from typing import Optional

from django import forms

from clauses.logic.locator import ClauseLocator


class ClauseForm(forms.Form):
    """Form for validating any provided clauses and context."""

    clause = forms.CharField(max_length=1024)
    context = forms.CharField(max_length=1024)

    def process(self) -> tuple[bool, Optional[tuple[int, int]]]:
        """Take validated fields and pass them to a ClauseLocator."""
        locator = ClauseLocator(
            self.cleaned_data["clause"], self.cleaned_data["context"]
        )
        results = locator.locate()
        success = True

        if not results:
            success = False

        return success, results
