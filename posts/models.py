import uuid as uuid
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=50, null=True, blank=True)
    body = models.CharField(max_length=150, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.title

    class Meta:
        db_table = 'posts'


class Likes(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like_date = models.DateField(auto_now_add=True)
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f"{self.post.title} {self.liked_by.username}"

    class Meta:
        db_table = 'likes'



