from django import forms
from django.contrib.auth import authenticate
from .models import ManagerUser, RegisterCode


def checkio(s):
    fs = ''.join(filter(str.isalnum, s)) # keep only letters and digits
    return (
            len(fs) >= 1        # There is at least one letter or digit
        and len(s)  >= 8       # ... and there are at least 10 characters
        and not fs.isalpha()    # ... and there is at least one digit
        and not fs.isdigit()    # ... and there is at least one letter
        and not fs.islower()    # ... and not all letters are lowercase
        and not fs.isupper()    # ... and not all letters are uppercase
    )

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名',
                             widget=forms.TextInput(attrs={
                                 'class':'form-control',
                                 'id': "disableinput",
                                 'placeholder':'请输入用户名',
                             }))
    password = forms.CharField(label='密码', widget=forms.PasswordInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': '请输入密码',
                             }))

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('用户名或者密码不正确')
        else:
            self.cleaned_data['user'] = user
        return self.cleaned_data


class ProfileForm(forms.Form):
    old_password = forms.CharField(label='旧密码', widget=forms.PasswordInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': '请输入旧的密码',
                             }))
    new_password = forms.CharField(label='新密码', widget=forms.PasswordInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': '请输入新的密码',
                             }))
    new_password_re = forms.CharField(label='确认新密码', widget=forms.PasswordInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': '请确认新的密码',
                             }))

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super(ProfileForm, self).__init__(*args, **kwargs)

    def clean_old_password(self):
        old_pass = self.cleaned_data.get('old_password','')
        if not self.user.check_password(old_pass):
            raise forms.ValidationError('旧的密码错误')
        return old_pass

    def clean_new_password(self):
        new_password = self.cleaned_data.get('new_password', '')
        if not checkio(new_password):
            raise forms.ValidationError("密码至少8位并包含一个字母")
        return new_password

    def clean_new_password_re(self):
        new_password = self.cleaned_data.get('new_password', '')
        new_password_re = self.cleaned_data.get('new_password_re', '')
        if new_password != new_password_re or new_password == '':
            raise forms.ValidationError("两次输入密码不一致")
        return new_password_re


class EmailForm(forms.Form):
    email = forms.EmailField(label='新邮箱', widget=forms.EmailInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': '请输入新的Email',
                             }))

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super(EmailForm, self).__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data.email
        if email == '':
            pass
        return email