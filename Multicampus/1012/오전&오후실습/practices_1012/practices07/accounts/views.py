from django.shortcuts import render, redirect

# from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm

# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm


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
        form = CustomUserCreationForm(request.POST)
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
    return redirect("articles:index")


def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        "user": user,
    }
    return render(request, "accounts/detail.html", context)


def update(request, pk):
    user = get_user_model().objects.get(pk=pk)
    if request.method == "POST":
        # POST : input 값 가져와서, 검증하고, DB에 저장
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
            form.save()
            return redirect("account:detail", user.pk)
        # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 article_form을 랜더링
    else:
        # GET : Form을 제공
        form = CustomUserCreationForm(request.POST)
    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context)


def delete(request, pk):
    user = get_user_model().objects.get(pk=pk)
    user.delete()

    return redirect("accounts:index")
