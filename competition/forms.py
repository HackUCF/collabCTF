from django import forms

from competition.models import Challenge, Competition

_form_control = {'class': 'form-control'}


class CompetitionModelForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ('name', 'url', 'start_time', 'end_time')
        widgets = {
            'name': forms.TextInput(attrs=_form_control),
            'url': forms.URLInput(attrs=_form_control),
            'start_time': forms.DateTimeInput(attrs=_form_control),
            'end_time': forms.DateTimeInput(attrs=_form_control)
        }


class ChallengeModelForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ('name', 'point_value', 'progress', 'num_progress', 'competition')
        widgets = {
            'point_value': forms.NumberInput(_form_control),
            'num_progress': forms.NumberInput(_form_control)
        }


class HashForm(forms.Form):
    HASH_CHOICES = (
        ('MD5', 'MD5'),
        ('SHA1', 'SHA1'),
        ('SHA256', 'SHA256'),
        ('SHA512', 'SHA512'),
    )

    hash_type = forms.ChoiceField(choices=HASH_CHOICES)
    value = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))


class RotForm(forms.Form):
    ENCODE_CHOICE = (
        ("True", 'Encode'),
        ("False", 'Decode')
    )
    rot_type = forms.CharField(widget=forms.TextInput(attrs={'size': 2, 'type': 'number'}))
    value = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    encode = forms.ChoiceField(choices=ENCODE_CHOICE, label="")


class BaseConversionForm(forms.Form):
    value = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    base = forms.CharField(widget=forms.TextInput(attrs={'size': 2}))
    currBase = forms.CharField(widget=forms.TextInput(attrs={'size': 2}), label="Current Base")


class XorForm(forms.Form):
    value = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    key = forms.CharField(widget=forms.TextInput(attrs={'size': 40}))
