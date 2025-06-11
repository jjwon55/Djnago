from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

from accounts.form import SignUpForm

# Create your views here.
# 회원가입
def signup(request):
  
  if request.method == 'POST':
    # UserCreationForm : Django에서 제공하는 회원가입 폼
    # form = UserCreationForm(request.POST)
    form = SignUpForm(request.POST)
    if form.is_valid():
      # 회원가입 성공
      form.save()
      
      return redirect('/')
  else:
    # 회원가입 실패
    form = SignUpForm() 
    
  return render(request, 'registration/signup.html', {'form': form})
    