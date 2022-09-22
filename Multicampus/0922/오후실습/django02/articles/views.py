from django.shortcuts import render
import random

# Create your views here.

def dinner(request):

    menus = [
        ['족발', 'https://w.namu.la/s/3c05b431f6a5e430a2b2db390a5b3b9ccd6ff8d823a05693a6d507d74b8b63ce794c733c0a0d46f6bf0dba35ddddef6c1593786a98beb539e80b781e18497c96a6a04335e4c11f648d526a2bc85d476df55680740c531507dfaa0be1af7eebea95ec064388c166dc02c22ba06b594eee'],
        ['삼겹살','https://img.kr.news.samsung.com/kr/wp-content/uploads/2017/03/%ED%91%B8%EB%93%9C%ED%8F%AC%EC%BB%A4%EC%8A%A44%ED%8E%B804.jpg'],
        ['미역국','https://www.k-health.com/news/photo/201911/46112_38509_4731.jpg'],
        ['아구찜','https://recipe1.ezmember.co.kr/cache/recipe/2021/08/05/98998b80a8bba88b91b8829417f416a61.jpg'],
        ['초밥','https://rimage.gnst.jp/livejapan.com/public/article/detail/a/00/00/a0000370/img/basic/a0000370_main.jpg?20201002142956&q=80&rw=750&rh=536'],
    ]

    menu = random.choice(menus)

    context = {
        'menu' : menu[0],
        'images' : menu[1],
    }

    return render(request, 'dinner.html', context)


def lotto(request):

    numbers = random.sample(range(1, 45), 6)
    numbers.sort()
    context = {
        'numbers' : numbers,
        'try' : '5',
    }

    return render(request, 'lotto.html', context)