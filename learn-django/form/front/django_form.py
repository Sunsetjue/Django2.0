from django import forms
from django.core import validators
from .models import Registered

class MessageBoardForm(forms.Form):
    title = forms.CharField(max_length=100, min_length=1, label="标题", error_messages={"required": '请传入参数'})
    content = forms.CharField(widget=forms.Textarea, label="内容", error_messages={"required": '请传入参数'})
    # widget=forms.Textarea 表示内容可以多行排列
    email = forms.EmailField(label="邮箱", error_messages={"required": '请传入参数'})
    reply = forms.BooleanField(required=False, label="是否回复") # 是否回复表示可以不回复， 默认为True

    # django 里填写表单

class Forms(forms.Form):
    '''常用验证器'''
    # 验证是否为邮箱格式
    email = forms.CharField(validators=[validators.EmailValidator(message= "请输入正确的邮箱")])
    # 正则表达式验证
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[345678]\d{9}', message="请输入正确的手机号码")])

class RegisteredForm(forms.Form):
    name = forms.CharField(max_length=4, min_length=2, error_messages={"required": "请输入正确的名字"})
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[345678]\d{9}', message="请输入正确的手机号码")])
    pwd1 = forms.CharField(max_length=16)
    pwd2 = forms.CharField(max_length=16)

    # 验证是否用户输入的数据在数据库中存在 对某个关键字进行验证
    def clean_telephone(self):
        telephone = self.cleaned_data.get("telephone")
        exists = Registered.objects.filter(telephone=telephone)
        if exists:
            raise forms.ValidationError(message="手机号码已经存在！")
        return telephone

    # 重写clean 父类 对某些关键字进行排查
    def clean(self):
        super().clean()
        pwd1 = self.cleaned_data.get("pwd1")
        pwd2 = self.cleaned_data.get("pwd2")
        if pwd1 != pwd2:
            raise forms.ValidationError(message="密码核对错误！")
        return super().clean()

    def get__error(self):
        errors = self.errors.get_json_data()
        dict = {}
        for keys,error in errors.items():
            ls = []
            for message in error:
                msg = message["message"]
                ls.append(msg)
            dict[keys] = ls
        return dict
    # 如果所有的form 表单都需要这个 则可以写成父类 让其余的表单来当子类调用这个父类
