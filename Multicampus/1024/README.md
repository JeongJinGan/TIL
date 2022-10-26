# M:N (Article-User)

# LIKE

## 모델 관계 설정 (1/6)

- ManyToManyField 작성

```python
# articles/models.py
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```



## 모델 관계 설정 (2/6)

- Migration 진행 후 에러 확인

```bash
$ python manage.py makemigrations
```

```bash
ERRORS:
articles.Article.like_users: (fields.E304) Reverse accessor for 'Article.like_users' clashes with
reverse accessor for 'Article.user'. 
HINT: Add or change a related_name argument to the definition for 'Article.like_users' or
'Article.user'.
articles.Article.user: (fields.E304) Reverse accessor for 'Article.user' clashes with reverse 
accessor for 'Article.like_users'.
HINT: Add or change a related_name argument to the definition for 'Article.user' or
'Article.like_users'.
```



## 모델 관계 설정 (3/6)

- like_users 필드 생성 시 자동으로 역참조에는 .article_set 매니저가 생성됨 
- 그러나 이전 N:1(Article-User) 관계에서 이미 해당 매니저를 사용 중 
  - user.article_set.all() → 해당 유저가 작성한 모든 게시글 조회 
  - user가 작성한 글들(user.article_set)과 user가 좋아요를 누른 글(user.article_set)을 구분할 수 없게 됨

-  user와 관계된 ForeignKey 혹은 ManyToManyField 중 하나에 related_name을 작성해야 함



##  모델 관계 설정 (4/6)

- ManyToManyField에 related_name 작성 후 Migration

```python
# articles/models.py
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```



## 모델 관계 설정 (5/6)

- 생성된 중개 테이블 확인
  - db.sqlite3 -> Open database -> SQLITE EXPLORER -> db.sqlite3 테이블 확인



## 모델 관계 설정 (6/6)

- User - Article간 사용 가능한 related manager 정리 
  - article.user 
    - 게시글을 작성한 유저 - N:1 
  - user.article_set 
    - 유저가 작성한 게시글(역참조) - N:1 
  - article.like_users 
    - 게시글을 좋아요한 유저 - M:N 
  - user.like_articles 
    - 유저가 좋아요한 게시글(역참조) - M:N



## LIKE 구현 (1/2)

- url 및 view 함수 작성

```python
# articles/urls.py
urlpatterns = [
    ...
    path('<int:article_pk>/likes/', views.likes, name='likes'),
]
```

```python
# articles/views.py
def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if article.like_users.filter(pk=request.user.pk).exists():
        # if request.user in article.like_users.all():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('articles:index')
```



## .exists()

- QuerySet에 결과가 포함되어 있으면 True를 반환하고 그렇지 않으면 False를 반환 
- 특히 큰 QuerySet에 있는 특정 개체의 존재와 관련된 검색에 유용



## LIKE 구현 (2/2)

- index 템플릿에서 각 게시글에 좋아요 버튼 출력하기

```html
<!-- articles/index.html -->
{% extends 'base.html' %}
{% block content %}
    …
    {% for article in articles %}
    …
        <div>
        <form action="{% url 'articles:likes' article.pk %}" method="POST">
            {% csrf_token %}
            {% if request.user in article.like_users.all %}
            <input type="submit" value="좋아요 취소">
            {% else %}
            <input type="submit" value="좋아요">
            {% endif %}
        </form>
        </div>
        <a href="{% url 'articles:detail' article.pk %}">DETAIL</a>
        <hr>
    {% endfor %}
{% endblock content %}
```
