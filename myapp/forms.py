from django import forms
from django.forms import widgets
class UserRegisterForm(forms.Form):
    username = forms.CharField(required=True, max_length=12,widget=widgets.TextInput(attrs={'class': 'form-username', 'placeholder': "请输入用户名"}), min_length=4,error_messages={
                                   "max_length": "用户名至多为12位",
                                   "min_length": "用户名最少为4位",
                                   "required": "用户名不能为空",
                               })
    email = forms.CharField(required=True,widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': "请输入邮箱前缀"}), error_messages={
        "required": "邮箱不能为空",
    })
    password = forms.CharField(required=True, max_length=18, min_length=6,widget=widgets.PasswordInput(attrs={'class':'from-pwd','placeholder':"请输入密码"}), error_messages={
        "max_length": "密码最多18位",
        "min_length": "密码至少6位",
        "required": "密码不能为空",
    })
    password2 = forms.CharField(required=True, max_length=18, min_length=6,widget=widgets.PasswordInput(attrs={'class': 'from-pwd', 'placeholder': "请输入确认密码"}),
                               error_messages={
                                   "max_length": "确认密码最多18位",
                                   "min_length": "确认密码至少6位",
                                   "required": "确认密码不能为空"
                               })
    code = forms.CharField(required=True,widget=widgets.TextInput(attrs={'class': 'from-yzm', 'placeholder': "请输入验证码"}),min_length=4, error_messages={
            "min_length": "验证码最少为5位",
            "required": "验证码不能为空",
        })

class renzhengForm(forms.Form):
    sfz_id = forms.CharField(required=True,widget=widgets.TextInput(attrs={'class': 'form-username', 'placeholder': "请输入新身份证号码",'value':''}),max_length=18,min_length=18, error_messages={
            "max_length": "身份证最多为18位",
            "min_length": "身份证最多为18位",
            "required": "身份证不能为空",
        })
    name  = forms.CharField(required=True,widget=widgets.TextInput(attrs={'class': 'form-username', 'placeholder': "请输入真实姓名",'value':''}),error_messages={
                                   "required": "姓名不能为空",
                               })
class renzhengForm2(forms.Form):
    sfz_id1 = forms.CharField(required=True,widget=widgets.TextInput(attrs={'class': 'form-username', 'placeholder': "请输入原身份证号码" ,'value':''}),max_length=18,min_length=18, error_messages={
            "max_length": "原身份证号最多为18位",
            "min_length": "原身份证号码最多为18位",
            "required": "原身份证号码不能为空",
        })
    name1  = forms.CharField(required=True,widget=widgets.TextInput(attrs={'class': 'form-username', 'placeholder': "请输入原姓名",'value':''}),error_messages={
                                   "required": "原姓名不能为空",
                               })
class UserLoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=12,widget=widgets.TextInput(attrs={'class':'name','placeholder':"请输入用户名"}), min_length=4,error_messages={
        "max_length": "用户名至多为12位",
        "min_length": "用户名最少为4位",
        "required": "用户名不能为空",
    })
    password = forms.CharField(required=True, max_length=18, min_length=6, widget=widgets.PasswordInput(attrs={'class':'pwd','placeholder':"请输入密码"}), error_messages={
        "max_length":"密码最多18位" ,
        "min_length":"密码至少6位",
        "required": "密码不能为空",
    })
class UserforgetpasswordForm(forms.Form):
    username = forms.CharField(required=True, max_length=12,widget=widgets.TextInput(attrs={'class': 'form-username', 'placeholder': "请输入用户名"}),min_length=4, error_messages={
            "max_length": "用户名至多为12位",
            "min_length": "用户名最少为4位",
            "required": "用户名不能为空",
        })
    email = forms.CharField(required=True,widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': "请输入绑定的邮箱"}),error_messages={
                                "required": "邮箱不能为空",
                            })
    password = forms.CharField(required=True, max_length=18, min_length=6,widget=widgets.PasswordInput(attrs={'class': 'from-pwd', 'placeholder': "请输入新密码"}),
                               error_messages={
                                   "max_length": "新密码最多18位",
                                   "min_length": "新密码至少6位",
                                   "required": "新密码不能为空"
                               })
    password2 = forms.CharField(required=True, max_length=18, min_length=6,widget=widgets.PasswordInput(attrs={'class': 'from-pwd', 'placeholder': "请输入确认新密码"}),
                                error_messages={
                                    "max_length": "确认密码最多18位",
                                   "min_length": "确认密码至少6位",
                                   "required": "确认密码不能为空"
                                })
    code = forms.CharField(required=True,widget=widgets.TextInput(attrs={'class': 'from-yzm', 'placeholder': "请输入验证码"}),min_length=4, error_messages={
            "min_length": "验证码最少为5位",
            "required": "验证码不能为空",
        })
class ChangePasswordForm(forms.Form):
    password = forms.CharField(required=True, max_length=18, min_length=6,widget=widgets.PasswordInput(attrs={'class': 'form-pwd', 'placeholder': "请输入原密码"}),
                               error_messages={
                                   "max_length": "原密码最多18位",
                                   "min_length": "原密码至少6位",
                                   "required": "密码不能为空",
                               })
    password2 = forms.CharField(required=True, max_length=18, min_length=6,widget=widgets.PasswordInput(attrs={'class': 'form-pwd', 'placeholder': "请输入新密码"}),
                                error_messages={
                                    "max_length": "新密码最多18位",
                                    "min_length": "新密码至少6位",
                                    "required": "新密码不能为空"
                                })
    password3 = forms.CharField(required=True, max_length=18, min_length=6,widget=widgets.PasswordInput(attrs={'class': 'form-pwd', 'placeholder': "请确认新密码"}),
                                error_messages={
                                    "max_length": "确认新密码最多18位",
                                    "min_length": "确认新密码至少6位",
                                    "required": "确认新密码不能为空"
                                })