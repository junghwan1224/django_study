from django.db import models
from accounts.models import Account
# Create your models here.

# 판매 게시판, 구매 게시판 따로 보여주는지, 아니면 카테고리 분류 후 다 보여주는지?


class MainTheme(models.Model):
    title = models.CharField(max_length=15)

    def __str__(self):
        return self.title


class MidTheme(models.Model):
    title = models.CharField(max_length=15)
    main_theme = models.ForeignKey(
            MainTheme,
            on_delete=models.CASCADE,
            related_name='related_mid_theme'
        )

    def __str__(self):
        return self.title


class SubTheme(models.Model):
    title = models.CharField(max_length=15)
    mid_theme = models.ForeignKey(
            MidTheme,
            on_delete=models.CASCADE,
            related_name='related_sub_theme'
        )

    def __str__(self):
        return self.title


class Post(models.Model):

    title = models.CharField(max_length=30)
    content = models.TextField()
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']


# 판매중, 구매중, 거래중 로직 어떤식으로 짤지 구체적으로 정해야 할 것 같습니다...!


class SellPost(Post):

    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    sub_theme = models.ForeignKey(
            SubTheme,
            on_delete=models.CASCADE,
            related_name='sell_post_sub_theme'
        )


class PurchasePost(Post):

    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    sub_theme = models.ForeignKey(
            SubTheme,
            on_delete=models.CASCADE,
            related_name='purchase_post_sub_theme'
        )
