from django import forms
from django.db import models
from .models import Order, Ship
from django.contrib.auth import authenticate

class OrderForm(forms.Form):
    goods_name = forms.CharField(label='货名', widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': '请输入货名',
                                }))
    cargo_owner = forms.CharField(label='货主所属公司', widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': '请输入公司名',
                                }))
    goods_amount = forms.IntegerField(label='货物数量', widget=forms.NumberInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': '请输入货物数量',
                                }))
    unit = forms.ChoiceField(label = '单位',
                             widget=forms.Select(attrs={'class': 'form-control',
                                                        'placeholder': '请输入货物数量',}),
                             choices=(("KG", "kilogram"), ("T", "Ton"))
                             )
    target_port = forms.CharField(label='目的港', widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': '请输入港口名',
                                }))
    ship_use = forms.ChoiceField(
                                label='船只名称',
                                widget=forms.Select(attrs={'class': 'form-control',
                                                           'placeholder': '请输入货物数量',})
                             )
    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['ship_use'].choices = ((x['ship_name'], x['ship_name']) for x in Ship.objects.all().values('ship_name')
                                      )
