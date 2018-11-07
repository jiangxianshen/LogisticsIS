from django import forms
from django.contrib.auth import authenticate
from .models import ManagerUser, RegisterCode


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名',
                             widget=forms.TextInput(attrs={
                                 'class':'form-control',
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


class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名',
                               widget=forms.TextInput(attrs={
                                 'class':'form-control',
                                 'placeholder':'请输入用户名',
                             }))
    password = forms.CharField(label='密码',
                               widget=forms.PasswordInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': '请输入密码',
                             }))
    email = forms.EmailField(label='邮箱地址',
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': '请输入邮箱地址',}))
    authcode = forms.CharField(label='注册码',
                               widget=forms.TextInput(attrs={
                                 'class':'form-control',
                                 'placeholder':'请输入注册码',
                             }))

    def clean(self):
        #username = self.cleaned_data['username']
        #eamil = self.cleaned_data['email']
        #code = self.cleaned_data['authcode']
        if ManagerUser.objects.get(username=self.cleaned_data['username']):
            raise forms.ValidationError('该用户名已存在')
        if ManagerUser.objects.get(eamil=self.cleaned_data['email']):
            raise forms.ValidationError('该email已被注册')
        if RegisterCode.objects.get(code=self.cleaned_data['authcode'],is_new=1) is None:
            raise forms.ValidationError('该邀请码不可用')
        else:
            RegisterCode.objects.filter(code=self.cleaned_data['authcode']).update(is_new=0)
        return self.cleaned_data
