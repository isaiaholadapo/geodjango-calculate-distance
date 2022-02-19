from django import forms

from . import models


class MeasurementModelForm(forms.ModelForm):
    class Meta:
        model = models.Measurement
        fields = ('destination', )