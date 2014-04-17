from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Reset, Layout, Fieldset, ButtonHolder, HTML
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse

from competition.models import Challenge, Competition, ChallengeFile


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

        self.add_helper = FormHelper()
        self.add_helper.form_id = 'add-challenge'
        self.add_helper.form_method = 'post'
        self.add_helper.form_action = ''

        self.update_helper = FormHelper()
        self.update_helper.form_id = 'update-challenge'
        self.update_helper.form_method = 'post'
        self.update_helper.form_action = ''

        holder = ButtonHolder(
            Submit('submit', 'Submit'),
            Reset('reset', 'Reset'),
            css_class='text-right'
        )

        self.add_helper.layout = Layout(
            Fieldset(
                'Add a challenge',
                'name',
                'point_value',
                'progress',
                'num_progress'
            ),
            holder
        )

        self.update_helper.layout = Layout(
            Fieldset(
                'Update a challenge',
                'name',
                'point_value',
                'progress',
                'num_progress'
            ),
            holder
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


class ChallengeFileModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ChallengeFileModelForm, self).__init__(*args, **kwargs)

        self.add_helper = FormHelper()
        self.add_helper.form_id = 'add-file'
        self.add_helper.form_method = 'post'
        self.add_helper.form_action = ''

        self.update_helper = FormHelper()
        self.update_helper.form_id = 'update-file'
        self.update_helper.form_method = 'post'
        self.update_helper.form_action = ''

        holder = ButtonHolder(
            Submit('submit', 'Submit'),
            Reset('reset', 'Reset'),
            css_class='text-right'
        )

        self.add_helper.layout = Layout(
            Fieldset(
                'Add a file',
                HTML('<p>Original filenames are preserved whenever possible.</p>'),
                'file',
            ),
            holder
        )

        self.update_helper.layout = Layout(
            Fieldset(
                'Update a file',
                'file',
            ),
            holder
        )

    class Meta:
        model = ChallengeFile
        fields = ('file',)


class HashForm(forms.Form):
    HASH_CHOICES = (
        ('MD5', 'MD5'),
        ('SHA1', 'SHA1'),
        ('SHA256', 'SHA256'),
        ('SHA512', 'SHA512'),
    )

    hash_type = forms.ChoiceField(choices=HASH_CHOICES)
    value = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    result = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40, 'id': "hash-result"}), required=False)

    def __init__(self, *args, **kwargs):
        super(HashForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'hash-form'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse("tools_hash")
        self.helper.layout = Layout(
            Fieldset(
                'Hashing Tools',
                'hash_type',
                'value',
                'result'
            ),
            ButtonHolder(
                Submit('submit', 'Submit'),
                Reset('reset', 'Reset'),
                css_class='text-right'
            )
        )


class RotForm(forms.Form):
    ENCODE_CHOICE = (
        ("True", 'Encode'),
        ("False", 'Decode')
    )
    rot_type = forms.CharField(widget=forms.TextInput(attrs={'size': 2, 'type': 'number'}))
    value = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    encode = forms.ChoiceField(choices=ENCODE_CHOICE, label="")
    result = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40, 'id': "rot-result"}), required=False)

    def __init__(self, *args, **kwargs):
        super(RotForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'rot-form'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse("tools_rot")
        self.helper.layout = Layout(
            Fieldset(
                'ROT=* Encoder/Decoder',
                'rot_type',
                'value',
                'encode',
                'result'
            ),
            ButtonHolder(
                Submit('submit', 'Submit'),
                Reset('reset', 'Reset'),
                css_class='text-right'
            )
        )


class BaseConversionForm(forms.Form):
    value = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    base = forms.CharField(widget=forms.TextInput(attrs={'size': 2}))
    currBase = forms.CharField(widget=forms.TextInput(attrs={'size': 2}), label="Current Base")
    result = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40, 'id': "base-conversion-result"}),
                             required=False)

    def __init__(self, *args, **kwargs):
        super(BaseConversionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'base-conversion-form'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse("tools_base_conversion")
        self.helper.layout = Layout(
            Fieldset(
                'Base Conversion Tool',
                'value',
                'base',
                'currBase',
                'result'
            ),
            ButtonHolder(
                Submit('submit', 'Submit'),
                Reset('reset', 'Reset'),
                css_class='text-right'
            )
        )


class XorForm(forms.Form):
    value = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    key = forms.CharField(widget=forms.TextInput(attrs={'size': 40}))
    result = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40, 'id': "xor-result"}), required=False)

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
                'key',
                'result'
            ),
            ButtonHolder(
                Submit('submit', 'Submit'),
                Reset('reset', 'Reset'),
                css_class='text-right'
            )
        )


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'registration-form'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse("register")
        self.helper.layout = Layout(
            Fieldset(
                'Register',
                'username',
                'password1',
                'password2'
            ),
            ButtonHolder(
                Submit('submit', 'Submit'),
                Reset('reset', 'Reset'),
                css_class='text-right'
            )
        )
