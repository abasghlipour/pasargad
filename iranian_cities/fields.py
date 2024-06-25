from django.db import models
from django import forms

from iranian_cities.models import (
    Ostan, Shahrestan,
    Shahr, 
)


class OstanField(models.ForeignKey):
    description = 'Iranian Ostan'

    def __init__(self, *args, **kwargs):
        defaults = {
            'to': Ostan,
            'on_delete': models.CASCADE
        }
        defaults.update(kwargs)
        super().__init__(*args, **defaults)

class ShahrestanField(models.ForeignKey):
    description = 'Iranian Shahrestan'

    def __init__(self, *args, **kwargs):
        defaults = {
            'to': Shahrestan,
            'on_delete': models.CASCADE
        }
        defaults.update(kwargs)
        super().__init__(*args, **defaults)



class ShahrField(models.ForeignKey):
    description = 'Iranian Shahr'

    def __init__(self, *args, **kwargs):
        defaults = {
            'to': Shahr,
            'on_delete': models.CASCADE
        }
        defaults.update(kwargs)
        super().__init__(*args, **defaults)


