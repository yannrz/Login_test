"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class RegistrationForm(forms.Form):
 
   username = forms.CharField(label="nom",widget=forms.TextInput(attrs={'placeholder': 'Nom d\'utilisateur','class':'form-control input-perso'}),max_length=30,min_length=3)
   email = forms.EmailField(label="email",widget=forms.EmailInput(attrs={'placeholder': 'Email','class':'form-control input-perso'}),max_length=100,error_messages={'invalid': ("Email invalide.")})
   passwordInput = forms.CharField(label="passwordInput",max_length=50,min_length=6,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe','class':'form-control input-perso','id':'passwordInput'}))
   confirmPasswordInput = forms.CharField(label="confirmPasswordInput",max_length=50,min_length=6,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Confirmer mot de passe','class':'form-control input-perso','id':'confirmPasswordInput'}))