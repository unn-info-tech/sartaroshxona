from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import re


class NoRepeatingSequencesValidator:
    def validate(self, password, user=None):
        if re.match(r'(\d)\1{2,}', password):  # Проверка на повторяющиеся последовательности цифр
            raise ValidationError(
                "Пароль содержит последовательность повторяющихся символов (например, '111', '222' и т. д.).",
                code='password_no_repeating_sequences',
            )

    def get_help_text(self):
        return "Ваш пароль не может содержать последовательности повторяющихся символов (например, '111', '222' и т. д.)."
