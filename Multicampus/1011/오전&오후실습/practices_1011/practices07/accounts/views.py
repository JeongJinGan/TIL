from django.shortcuts import render, redirect

# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

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
            form.save()
            return redirect("accounts:index")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


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
