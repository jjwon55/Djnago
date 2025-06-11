from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#UserCreationForm 상속받아 회원가입 폼 커스텀
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        # 필드 공통 설정
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

        # 개별 필드 설정
        self.fields['username'].widget.attrs.update({'placeholder': '아이디'})
        self.fields['password1'].widget.attrs.update({'placeholder': '비밀번호'})
        self.fields['password2'].widget.attrs.update({'placeholder': '비밀번호 확인'})