from django import forms

from crispy_forms.helper import FormHelper, reverse
from crispy_forms.layout import Layout, Field, HTML, Submit
from django.utils.safestring import mark_safe
from crispy_forms.bootstrap import PrependedText


class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["email"].label = ""
        self.fields["password"].label = ""
        self.helper.layout = Layout(
            PrependedText('email', mark_safe('<i class="glyphicon glyphicon-envelope"></i>'),
                          placeholder="Enter Email Address"),
            PrependedText('password', '<i class="glyphicon glyphicon-envelope"></i>',
                          placeholder="Enter Password"),
            Field('remember_me'),
            Submit('sign_in', 'Log in',
                   css_class="btn btn-lg btn-primary btn-block"),
        )

# class CrispyAddressForm(AddressForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.fields["email"].label = ""
#         self.helper.layout = Layout(
#             Field(PrependedText('email', mark_safe('<i class="glyphicon glyphicon-envelope form-control-feedback"></i>'),
#                 placeholder=("Email")))
            # Field(
            #     PrependedText('email',
            #         mark_safe(
            #             '<span class="glyphicon glyphicon-envelope"></span>'),
            #             placeholder=("Enter Email"), autofocus="")
            # ),
            # Field(
            #     PrependedText('password',
            #         mark_safe(
            #             '<span class="glyphicon glyphicon-user"></span>'),
            #             placeholder=("Enter Full Name"))
            # ),
        # )
