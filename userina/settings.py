from django.conf import settings

# How long do people have to verify their account.
USERINA_VERIFICATION_DAYS = getattr(settings, 'USERINA_VERIFICATION_DAYS', 2)

# This value will be inserted into ``Account.verification_key`` if a key get's
# used succesfully.
USERINA_VERIFIED = getattr(settings, 'USERINA_VERIFIED', 'ALREADY_VERIFIED')