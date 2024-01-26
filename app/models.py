from django.db import models
from django import forms
from django.core import validators

def validate_for_a(data):
    if data.lower().startswith('m'):
        raise forms.ValidationError('cannot startwith m')
# Create your models here.
    
class Student(models.Model):
    sname=models.CharField(max_length=20,primary_key=True,validators=[validate_for_a])
    sage=models.IntegerField()
    smobile=models.CharField(max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    def __str__(self) -> str:
        return self.sname

