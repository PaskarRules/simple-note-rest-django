from django.core.exceptions import ValidationError

import re


def email_validator(email):
    forbiddenlist = ["gmail.com", "icloud.com"]

    user_regex = r"^[A-z0-9]{3,}\S$"
    domain_regex = r"^[A-z-0-9]{3,}.[A-z-0-9]{3,}$"

    if not email or "@" not in email:
        raise ValidationError("Invalid email")

    user_part, domain_part = email.split("@")

    if not re.fullmatch(user_regex, user_part) or \
            not re.fullmatch(domain_regex, domain_part) or domain_part in forbiddenlist:
        raise ValidationError("Invalid email")


def password_validate(password):
    regex = r'^[A-Z](?=.*\d)(?=.*[a-zA-Z])[a-zA-Z\d_]{6,15}$'

    if not re.fullmatch(regex, password):
        raise ValidationError("Invalid password")


def first_name_validate(first_name):
    regex = r'^\S[A-z-]{3,}\S$'

    if not re.fullmatch(regex, first_name):
        raise ValidationError("Invalid First name.")


def last_name_validate(last_name):
    regex = r'^\S[A-z- ]{3,}\S$'

    if not re.fullmatch(regex, last_name):
        raise ValidationError("Invalid Last name.")
