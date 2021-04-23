from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Team


class RegisterForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ('teamname', 'email', 'member1', 'member1_phone',
                  'member2', 'member2_phone', 'member3', 'member3_phone')
        labels = {
            'teamname': '',
                        'email': '',
                        'member1': '',
                        'member1_phone': '',
                        'member2': '',
                        'member2_phone': '',
            'member3': '',
            'member3_phone': '',
        }
        widgets = {
                'teamname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'TeamName (Use as username while signup)'}),
                'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
                'member1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' Member 1'}),
                'member1_phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Member 1 Phone'}),
                'member2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Member 2 (Write NA if none)'}),
                'member2_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Member 2 Phone'}),
                'member3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Member 3 (Write NA if none)'}),
                'member3_phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Member 3 Phone'}),
                
            }