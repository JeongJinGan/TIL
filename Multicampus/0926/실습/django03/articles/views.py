from django.shortcuts import render
import random

# Create your views here.


def index(request, num):
    number = int(num)
    if number % 2 == 0:
        res = "짝수"
    else:
        res = "홀수"
    if number == 0:
        res = "0"

    context = {
        "num": number,
        "res": res,
    }

    return render(request, "index.html", context)


def four(request, num, num2):
    number1 = int(num)
    number2 = int(num2)

    plus = number1 + number2
    minus = number1 - number2
    mul = number1 * number2
    div = number1 // number2

    context = {
        "num1": number1,
        "num2": number2,
        "plus": plus,
        "minus": minus,
        "mul": mul,
        "div": div,
    }

    return render(request, "four_operation.html", context)


def life(request):
    return render(request, "life.html")


def result(request):
    # print(request)
    # print(dir(request))
    # print(request.GET.get('ball'))
    name = request.GET.get("name")
    past_life = ["왕", "노비", "내시", "고래", "개미", "똥", "돌멩이", "암행어사", "장군"]
    past = random.choice(past_life)
    context = {
        "name": name,
        "past": past,
    }

    return render(request, "result.html", context)


def lipsum(request):
    return render(request, "lipsum.html")


def korean(request):

    sen = request.GET.get("sen")
    word = request.GET.get("word")
    context = {
        "sen": sen,
        "word": word,
    }

    return render(request, "korean.html", context)
