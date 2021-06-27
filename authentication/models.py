from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class UserActivity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, editable=False)
    last_login = models.DateTimeField(null=True, blank=True)
    last_request = models.DateTimeField(null=True, blank=True)

    # def __str__(self):
    #     return self.user.username

    class Meta:
        db_table = 'user_activity'

