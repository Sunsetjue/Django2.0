from django import forms
from .models import Username

class SignUpForm(forms.ModelForm):
    pwd1 = forms.CharField(max_length=16, min_length=6, error_messages={"required": "请输入正确的密码"})
    pwd2 = forms.CharField(max_length=16, min_length=6, error_messages={"required": "请输入正确的密码"})

    class Meta:
        model = Username
        exclude = ["password"]
        error_messages = {
            "username": {"required": '请输入正确的用户名！'},
            "telephone": {"required": '请输入正确的手机号！'},
            "money": {"required": '请输入正确的金额！'}
        }

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        pwd1 = cleaned_data.get("pwd1")
        pwd2 = cleaned_data.get("pwd2")
        if pwd1 != pwd2:
            raise forms.ValidationError("两次输入的密码不一致!")
        else:
            return cleaned_data

    def get_errors(self):
        errors = self.errors.get_json_data()
        error_list = []
        for v in errors.values():
            for error_dict in v:
                error_message = error_dict["message"]
                error_list.append(error_message)
        return error_list

class SignInForm(forms.ModelForm):
    class Meta:
        model = Username
        fields = ["telephone", "password"]
        error_messages = {
            "telephone": {"required": '请输入正确的电话号码！'},
            "password": {"required": '请输入正确的密码！', "invalid": '密码错误！'}
        }

    def get_errors(self):
        errors = self.errors.get_json_data()
        error_list = []
        for v in errors.values():
            for error_dict in v:
                error_message = error_dict["message"]
                error_list.append(error_message)
        return error_list


class TransformForm(forms.ModelForm):
    class Meta:
        model = Username
        fields = ["telephone", "money"]
        error_messages = {
            "telephone": {"required": '请输入电话号码！', "invalid": "电话不存在或者没有注册！"},
            "money": {"required": '请输入转账金额！'}
        }

    def get_errors(self):
        errors = self.errors.get_json_data()
        error_list = []
        for v in errors.values():
            for error_dict in v:
                error_message = error_dict["message"]
                error_list.append(error_message)
        return error_list
