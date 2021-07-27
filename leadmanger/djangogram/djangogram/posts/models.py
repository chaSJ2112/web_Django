from django.db import models
from djangogram.users import models as user_model 

# Create your models here.

# 시간 관리(업로드 업데이트 날짜) - 상속
class TimeStamedModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    upadte_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

# 사진 관리
class Post(TimeStamedModel):
    # 작성자 (users모델의 user - 외래키)
    author = models.ForeignKey(
                user_model.User, 
                null=True,
                on_delete=models.CASCADE,
                related_name='post_author'
            )
    # 사진
    image = models.ImageField(blank=True)
    # 캡션
    cpation = models.TextField(blank=True)
    # 좋아요(다대다 관계)
    image_likes = models.ManyToManyField(user_model.User, related_name='post_image_likes')


# 댓글 관리
class Comment(TimeStamedModel):
    # 작성자
    author = models.ForeignKey(
                user_model.User,
                null=True, 
                on_delete=models.CASCADE, 
                related_name='comment_author'
            )
    # 포스트
    posts = models.ForeignKey(
                Post,
                null=True, 
                on_delete=models.CASCADE, 
                related_name='comment_post'
            )
    # 댓글 내용
    contents = models.TextField(blank=True)