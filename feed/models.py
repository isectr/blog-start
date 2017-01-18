from django.db import models

class HashTag(models.Model) :
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Article(models.Model):
    DEVELOPMENT = "dv"
    PERSONAL = "ps"
    CATEGORY_CHOICES = (
        (DEVELOPMENT, "development"),
        (PERSONAL, "personal"),
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=DEVELOPMENT,
    )

    hashtag = models.ManyToManyField(HashTag)


    def __str__(self):
        return self.title
#클래스 안에서 함수를 새로 정의할 때는, self를 써야 한다..(왜그러는거지)
class Comment(models.Model) :
    article = models.ForeignKey(
    Article,
    related_name="article_comments",
    on_delete=models.CASCADE,
    )
    #캐스캐이드 : 아티클이 지워지면 코멘트도 따라 지워라.
    username = models.CharField(max_length=50)
    content = models.CharField(max_length=200)

    def __str__(self):
        return "{}의 reply : {}".format(self.article.title, self.content)
        # return self.article.title
