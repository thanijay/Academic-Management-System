import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class NumberValidator(object):
    def validate(name, password, user=None):
        if not re.findall('\d', password):
            raise ValidationError(
                _("The password must contain at least 1 digit, 0-9."),
                code='password_no_number',
            )
