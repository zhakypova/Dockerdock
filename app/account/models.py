from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
