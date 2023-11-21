from django.db import models


class TypeChoices(models.TextChoices):
    VISA = 'VISA'
    ELCARD = 'ELCARD'
    MASTER_CARD = 'MASTER CARD'
