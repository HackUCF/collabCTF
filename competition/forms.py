from django import forms


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