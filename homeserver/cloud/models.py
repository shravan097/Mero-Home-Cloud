from __future__ import unicode_literals
from django.forms import ModelForm,forms
from django import forms
from django.db import models
from datetime import date
import os


# Create your models here.

class File(models.Model):
    file = models.FileField(upload_to='cloud/uploads/%Y%m%d')
    date = models.DateField(auto_now_add=False, default=date.today)
    password = models.CharField(max_length=1000, null=True, blank=True)

    def get_pass(self):
        return self.password

    def file_name(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return str(self.id)
    #ADD AUTHOR AS DEVICE MAC ADDRESS

class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ['file','password']

class PasswordForm(forms.Form):
    client_password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={"name":"password","class":"w3-input w3-border"}))