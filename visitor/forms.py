from django import forms
from visitor.models import Visitor


class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = [
            "full_name", "ssn", "birth_date",
            "apartment_number", "vehicle_plate",
        ]

        error_messages = {
            "full_name": {
                "required": "Guest's full anme is required ofr a visit."
            },
            "ssn": {
                "required": "Guest SSN is required for a visit."
            },
            "birth_date": {
                "required": "Guest Birth Date is required for a visit.",
                "invalid": "Please provide the birth date in the correct format (MM/DD/YYYY)"

            },
            "apartment_number": {
                "required": "The apartment number is required for a visit."
            },
        }


