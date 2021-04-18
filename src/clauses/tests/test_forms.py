from django.test import TestCase

from clauses import forms


class ClauseFormTests(TestCase):
    """Tests for processing logic in ClauseForm."""

    def test_valid_clause_context(self) -> None:
        """Ensure that valid clause contexts return the relevant results."""
        form = forms.ClauseForm(self.valid_form_data)
        self.assertTrue(form.is_valid())
        success, results = form.process()
        self.assertTrue(success)
        self.assertEqual(results, (111, 126))

    def test_invalid_clause_context(self) -> None:
        """Ensure that invalid clause contexts return False, None."""
        form = forms.ClauseForm(self.invalid_form_data)
        self.assertTrue(
            form.is_valid()
        )  # This built-in method only ensures fields are valid CharFields.
        success, results = form.process()
        self.assertFalse(success)
        self.assertIsNone(results)

    def setUp(self) -> None:
        """Set up any relevant initialisation data."""
        self.valid_form_data = {
            "clause": "Housing Act 2004",
            "context": (
                "The tenant shall occupy the Property under a statutory periodic tenancy "
                "in accordance with section 5(2) of the Housing Act 2004."
            ),
        }
        self.invalid_form_data = {
            "clause": "Computer Misuse Act 1990",
            "context": (
                "The tenant shall occupy the Property under a statutory periodic tenancy "
                "in accordance with section 5(2) of the Housing Act 2004."
            ),
        }
