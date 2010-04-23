from django.db import models

REPORT_FREQUENCY = (
    ('daily', 'Daily'),
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
    ('quarterly', 'Quarterly'),
)

REPORT_DELIVERY = (
    ('sms', 'SMS'),
    ('email', 'Email'),
)
