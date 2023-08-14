from django.forms import ModelForm
from .models import Version


class VersionForm(ModelForm):
    class Meta:
        model = Version
        fields = ['name', 'release_year']
