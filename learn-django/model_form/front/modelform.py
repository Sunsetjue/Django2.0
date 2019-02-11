from django import forms
from .models import Username,Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__" # 表示需要模型里的全部字段
        '''
        exclude = ['price'] # 表示除了列表里的字段 别的字段都要
        fields = ["title", 'pages'] # 表示需要列表里的字段
        '''
        # 定义错误信息
        error_messages = {
            "pages": {
                "required": "请输入页数",
                "invalid": "请输入正确的页数"
            },
            "price": {
                "required": '请输入价格',
                "invalid": '请输入正确的价格'
            },
            "title": {
                "required": '请输入书名',
                "invalid": '书名长度不能超过15'
            }
        }

class Registered(forms.ModelForm):
    pwd1 = forms.CharField(max_length=16, min_length=6)
    pwd2 = forms.CharField(max_length=16, min_length=6)

    class Meta:
        model = Username
        exclude = ["password"]

    def clean(self):
        clean_data = super(Registered, self).clean()
        pwd1 =clean_data.get("pwd1")
        pwd2 = clean_data.get("pwd2")
        if pwd1 != pwd2:
            raise forms.ValidationError("输入的密码二次不一致")
        return clean_data