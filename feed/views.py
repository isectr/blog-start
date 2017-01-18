from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Article, Comment, HashTag

# Create your views here.
def index(request):
    #리퀘스트, 장고 기능. 모든 함수에 자동으로 넘겨준다.

    # GET, Post : 클라이언트가 서버에 데이터 요청할 때 요청하는 방식의 종류
    category= request.GET.get("category")
    hashtag = request.GET.get("hashtag")

    hashtag_list = HashTag.objects.all()
    if not category and not hashtag :
        article_list = Article.objects.all()
#아티클의 전체 리스트를 뽑아 온다 / 데이터베이스의 모든 자료를 가져와라.
    elif category :
        article_list = Article.objects.filter(category=category)
    else :
        article_list = Article.objects.filter(hashtag__name=hashtag)

    # category_list = set([])
    # for article in article_list:
    #     category_list.add(article.get_category_display())
    # print(category_list)
    category_list = set([
        (article.category, article.get_category_display())
        for article in article_list
    ])

    ctx = {
        "article_list" : article_list,
        "hashtag_list" : hashtag_list,
        "category_list" : category_list,
    }
    #넘겨줬다. 본문에서 사용할 수 있게됐다.
    return render(request, "index.html", ctx)

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    #방법1: comment_list=Comment.objects.filter(article__id=articel_id)
    #방법2: comment_list = article.article_comments.all()
    hashtag_list = HashTag.objects.all()
    ctx = {
        "article" : article,
        # "comment_list" : comment_list,
        "hashtag_list" : hashtag_list,
    }
    if request.method == "GET" :
        pass
    elif request.method == "POST" :
        username= request.POST.get("username")
        content = request.POST.get("content")
        Comment.objects.create(
            article=article,
            username=username,
            content=content,
        )
        return HttpResponseRedirect("/{}/".format(article_id))
    return render(request, "detail.html", ctx)

#POST는 서버에다 정보를 전달해서 데이터베이스에 입력하도록 하는 것.
# 서버에서 추가적 작업이 필요하면 POST 방식.

# def about(request):
#     pass
