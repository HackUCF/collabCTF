from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Reset, Layout, Fieldset, ButtonHolder
from django import forms
from django.core.urlresolvers import reverse

from competition.models import Challenge, Competition


_form_control = {'class': 'form-control'}


class CompetitionModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CompetitionModelForm, self).__init__(*args, **kwargs)
        self.add_helper = FormHelper()
        self.add_helper.form_id = 'add-ctf'
        self.add_helper.form_method = 'post'
        self.add_helper.form_action = ''

        self.update_helper = FormHelper()
        self.update_helper.form_id = 'update-ctf'
        self.update_helper.form_method = 'post'
        self.update_helper.form_action = ''

        button_holder = ButtonHolder(
            Submit('submit', 'Submit'),
            Reset('reset', 'Reset'),
            css_class='text-right'
        )

        self.add_helper.layout = Layout(
            Fieldset(
                'Add a competition',
                'name',
                'url',
                'start_time',
                'end_time'
            ),
            button_holder
        )

        self.update_helper.layout = Layout(
            Fieldset(
                'Update competition',
                'name',
                'url',
                'start_time',
                'end_time'
            ),
            button_holder
        )

    class Meta:
        model = Competition
        fields = ('name', 'url', 'start_time', 'end_time')


class ChallengeModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ChallengeModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'add-challenge'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.layout = Layout(
            Fieldset(
                'Add a challenge',
                'name',
                'point_value',
                'progress',
                'num_progress'
            ),
            ButtonHolder(
                Submit('submit', 'Submit'),
                Reset('reset', 'Reset'),
                css_class='text-right'
            )
        )

    class Meta:
        model = Challenge
        fields = ('name', 'point_value', 'progress', 'num_progress')
        widgets = {
            'num_progress': forms.NumberInput(attrs={'type': 'range',
                                                     'min': 0,
                                                     'max': 100,
                                                     'step': 1})
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

    def __init__(self, *args, **kwargs):
        super(XorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'xor-form'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse("tools_xor")
        self.helper.layout = Layout(
            Fieldset(
                'XOR Strings',
                'value',
                'key'
            ),
            ButtonHolder(
                Submit('submit', 'Submit'),
                Reset('reset', 'Reset'),
                css_class='text-right'
            )
        )
