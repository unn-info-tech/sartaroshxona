from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import re


class NoRepeatingSequencesValidator:
    def validate(self, password, user=None):
        if re.match(r'(\d)\1{2,}', password):  # Checks for repeating sequences of numbers
            raise ValidationError(
                "Password contains a sequence of repeating characters (e.g., '111', '222', etc.).",
                code='password_no_repeating_sequences',
            )

    def get_help_text(self):
        return "Your password cannot contain sequences of repeating characters (e.g., '111', '222', etc.)."