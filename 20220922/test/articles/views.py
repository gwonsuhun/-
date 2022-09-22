from email.mime import image
from multiprocessing import context
from multiprocessing.dummy import Namespace
from random import random
from readline import append_history_file
from django.shortcuts import render
import random

# Create your views here.
def index(request):

    names = [ '삼겹살','김길동','임길동','최길동']

    name = random.choice(names)

    context = {
        'name' : name,
        'img' : 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIfRKrgGu0DsObpEInmX5CscFPES_MxFeLalXFO_jlx8NYdyWU5IySvBJioftp6JPBUcI&usqp=CAU'
        #변수명 값
    }
    return render(request, 'index.html', context)

def welcome(request, name):
    
    context = {
        'name' : name,
        'greetings' :[ "안녕하세요" , "반갑습니다",
        ],

        'images' : [
            'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIfRKrgGu0DsObpEInmX5CscFPES_MxFeLalXFO_jlx8NYdyWU5IySvBJioftp6JPBUcI&usqp=CAU',
            'https://previews.123rf.com/images/houbacze/houbacze1505/houbacze150500043/40703277-%EC%9D%B4-%ED%8C%8C%EB%9E%80%EC%83%89-%EA%B7%B8%EB%A6%BC%EC%9D%84-%ED%99%98%EC%98%81%ED%95%A9%EB%8B%88%EB%8B%A4.jpg',
        ]
    }
    return render(request, 'welcome.html', context)


def food(request):
    
    randomFood = ['삼겹살','불고기','돼지갈비','오징어회','갈비찜']
    food = random.choice(randomFood)
    if food == '삼겹살':
        randomimg = 'https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/201702/27/117f5b49-1d09-4550-8ab7-87c0d82614de.jpg'
    elif food == '불고기':
        randomimg = 'https://recipe1.ezmember.co.kr/cache/recipe/2016/12/30/df939769792632a48a0eba8bc895e8601.jpg'
    elif food == '돼지갈비':
        randomimg = 'https://crcf.cookatmarket.com/product/images/2020/09/pebu_1599119477_8882_720.jpg'
    elif food == '오징어회':
        randomimg = 'https://d12zq4w4guyljn.cloudfront.net/20210824185118_photo1_1bd15efe9497.jpg'
    elif food == '갈비찜':
        randomimg = 'https://recipe1.ezmember.co.kr/cache/recipe/2016/01/31/5240d19f3477433a28138af269ed26d71.jpg'
    context = {
    'name' : food,
    'img' : randomimg,
    }
    return render(request, 'food.html', context)


# def lotto(request):
#     number = []
#     randomnum = range(1,46)
#     for i in randomnum:
#     return render(request,"lotto.html",context)
