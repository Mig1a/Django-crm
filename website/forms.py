from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(Label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    first_name = forms.CharField(Label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First_name'}))
    last_name = forms.CharField(Label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last_name'}))

    class Meta:
        model = user
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


    def __int__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class = "form-text text-muted"><small>Required. 150 characters or fewer'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'User Name'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<span class = "form-text text-muted"><small>Required. Your password must be 8 characters'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'User Name'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class = "form-text text-muted"><small>Required. your pasword must be similar with the first one'