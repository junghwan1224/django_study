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


# 거래상태 필드는 아직
class Post(models.Model):

    POST_TYPE = (
        ('Buy', '구매글'),
        ('Sell', '판매글'),
    )

    post_type = models.CharField(
            max_length=10,
            choices=POST_TYPE,
            default='Buy',
        )
    sub_theme = models.ForeignKey(
            SubTheme,
            on_delete=models.CASCADE,
            related_name='post_sub_theme',
            default=1,
        )
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return '{0} - {1}'.format(self.get_post_type_display(), self.title)


# class Tag(models.Model):
#     name = models.CharField(max_length=10)

# 판매중, 구매중, 거래중 로직 어떤식으로 짤지 구체적으로 정해야 할 것 같습니다...!


# class SellPost(Post):

#     author = models.ForeignKey(Account, on_delete=models.CASCADE)
#     sub_theme = models.ForeignKey(
#             SubTheme,
#             on_delete=models.CASCADE,
#             related_name='sell_post_sub_theme'
#         )


# class PurchasePost(Post):

#     author = models.ForeignKey(Account, on_delete=models.CASCADE)
#     sub_theme = models.ForeignKey(
#             SubTheme,
#             on_delete=models.CASCADE,
#             related_name='purchase_post_sub_theme'
#         )
