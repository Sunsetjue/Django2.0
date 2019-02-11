from django import forms
from .models import Username

class SignUpView(forms.ModelForm):
    pwd1 = forms.CharField(max_length=16, min_length=6)
    pwd2 = forms.CharField(max_length=16, min_length=6)

    class Meta:
        model = Username
        exclude = ["password"]

    def clean(self):
        clean_data = super(SignUpView, self).clean()
        pwd1 = clean_data.get("pwd1")
        pwd2 = clean_data.get("pwd2")
        if pwd1 != pwd2:
            raise forms.ValidationError("两次输入的密码不一致")

        return clean_data

    error_messages = {
        "username": {"required": '请输入正确的用户名！'},
        "password": {"required": "请输入正确的密码！"}
    }

    def get_errors(self):
        errors = self.errors.get_json_data()
        errors_list = []
        for v in errors.values():
            for error_dict in v:
                message = error_dict["message"]
                errors_list.append(message)
        return errors_list

class SignInView(forms.ModelForm):
    class Meta:
        model = Username
        fields = ["username", "password"]

        error_messages = {
            "username": {"required": '请输入正确的用户名！'},
            "password": {"required": "请输入正确的密码！"}
        }
    def get_errors(self):
        errors = self.errors.get_json_data()
        errors_list = []
        for v in errors.values():
            for error_dict in v:
                message = error_dict["message"]
                errors_list.append(message)
        return errors_list