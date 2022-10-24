# 좋아요 기능

```python
# articles/urls.py
path("<int:pk>/like/", views.like, name="like"),
```

```python
# views.py
@login_required
def like(request, pk):
    article = Article.objects.get(pk=pk)
    # 만약에 로그인한 유저가 이 글을 좋아요를 눌렀다면,
    # if article.like_users.filter(id=request.user.id).exists():
    if request.user in article.like_users.all():
        # 좋아요 삭제하고
        article.like_users.remove(request.user)
    else:
        # 좋아요 추가하고
        article.like_users.add(request.user)
    # 상세 페이지로 redirect
    return redirect("articles:detail", pk)
```

```html
<!-- detail.html -->
<div class="mb-3">
        {% if request.user.is_authenticated %}
        <a class="like-heart" href="{% url 'articles:like' article.pk %}">
            {% if request.user in article.like_users.all %}
            <i class="bi bi-heart-fill"></i>
            {% else %}
            <i class="bi bi-heart"></i>
            {% endif %}</a>{{ article.like_users.count }}</span>
        {% endif %}
</div>
```

