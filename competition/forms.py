from crispy_forms.helper import FormHelper
from crispy_forms_foundation.layout import Submit, Reset, Layout, Fieldset, ButtonHolder, HTML
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm as PWChangeForm, \
    SetPasswordForm
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


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'registration-form'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse("register")
        self.helper.layout = Layout(
            Fieldset(
                '',
                'username',
                'first_name',
                'last_name',
                'email',
                'password1',
                'password2'
            ),
            ButtonHolder(
                Submit('submit', 'Submit'),
                Reset('reset', 'Reset'),
                css_class='text-right'
            )
        )


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'login-form'
        self.helper.attrs = {'data_abide': ''}
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.layout = Layout(
            Fieldset(
                '',
                'username',
                'password'
            ),
            ButtonHolder(
                Reset('reset', 'Reset', css_class='secondary'),
                Submit('submit', 'Submit'),
                css_class='buttons text-right'
            )
        )


class PasswordChangeForm(PWChangeForm):
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'pw-change-form'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.layout = Layout(
            Fieldset(
                'Change password',
                'old_password',
                'new_password1',
                'new_password2'
            ),
            ButtonHolder(
                Submit('submit', 'Submit'),
                Reset('reset', 'Reset'),
                css_class='text-right'
            )
        )


#not currently working and actually changing things
class EmailChangeForm(forms.Form):
    email = forms.EmailField(label="New Email Address")
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")

    def __init__(self, *args, **kwargs):
        super(EmailChangeForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'email-change-form'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.layout = Layout(
            Fieldset(
                'Change email',
                HTML(
                    '''<p><label class="control-label">Current Email Address: </label><span style="padding-left: 2em;">{{ user.email }}</span></p>'''),
                'email',
                'password'
            ),
            ButtonHolder(
                Submit('submit', 'Submit'),
                Reset('reset', 'Reset'),
                css_class='text-right'
            )
        )

    #The below was taken from password change form
    error_messages = dict(SetPasswordForm.error_messages, **{
        'password_incorrect': ("Your old password was entered incorrectly. "
                               "Please enter it again.")
    })

    def clean_password(self):
        """
        Validates that the old_password field is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',
            )
        return old_password

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['new_password1'])
        if commit:
            self.user.save()
        return self.user
