from django import forms
from . import models


class audio_upload_form(forms.ModelForm):
    class Meta:
        model = models.audio_files
        fields = [
            'comments',
            'audio'
        ]
        exclude = [
            'user',
            'sentence'
        ]
