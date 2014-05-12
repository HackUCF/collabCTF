from crispy_forms.helper import FormHelper
from crispy_forms_foundation.layout import Layout, Fieldset, ButtonHolder, Submit, Reset
from django import forms
from django.core.urlresolvers import reverse


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