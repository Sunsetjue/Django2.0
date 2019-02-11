from django import forms
from django.contrib.auth import get_user_model

class UserForm(forms.ModelForm):
    remember = forms.IntegerField(required=False) # 表示为可选可不选
    telephone = forms.CharField(max_length=11)
    class Meta:
        model = get_user_model()
        fields = ["password"]