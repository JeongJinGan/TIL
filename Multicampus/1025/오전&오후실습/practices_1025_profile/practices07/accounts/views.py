from django.shortcuts import render, redirect

# from .models import User
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm


# Create your views here.


def main(request):
    return render(request, "/main.html")


def index(request):
    # 게시글을 가져와서..
    # get_user_model().objects.get(pk=pk)
    accounts = get_user_model().objects.order_by("-pk")
    # Template에 전달한다.
    context = {"accounts": accounts}
    return render(request, "accounts/index.html", context)


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()  # ModelForm의 save메소드의 리턴값은 해당 모델의 인스턴스다
            auth_login(request, user)  # 로그인
            return redirect("accounts:index")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


def login(request):
    if request.method == "POST":
        # AuthenticationForm은 ModelForm이 아니다
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 세션에 저장
            # login 함수는 request, user 객체를 인자로 받음
            # user 객체는 어디? 바로 form에서 인증된 유저 정보를 받을 수 있음
            auth_login(request, form.get_user())
            return redirect(request.GET.get("next") or "articles:index")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("accounts:login")


def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        "user": user,
    }
    return render(request, "accounts/detail.html", context)


@login_required
def follow(request, pk):
    accounts = get_user_model().objects.get(pk=pk)
    if request.user == accounts:
        messages.warning(request, "스스로 팔로우 할 수 없습니다.")
        return redirect("accounts:detail", pk)
    # 프로필에 해당하는 유저를 로그인한 유저가
    if request.user in accounts.followers.all():
        # (이미) 팔로우 상태이면, '팔로우 취소' 버튼을 누르면 삭제(remove)
        accounts.followers.remove(request.user)
    else:
        # 팔로우 상태가 아니면 '팔로우'를 누르면 추가 (add)
        accounts.followers.add(request.user)
    # 상세 페이지로 redirect
    return redirect("accounts:detail", pk)


@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:detail", request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context)


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("accounts:index")
    else:
        form = PasswordChangeForm(request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/change_password.html", context)


def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect("accounts:index")
