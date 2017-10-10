from django.db import models


__all__ = (
    'Pizza',
    'Topping',
    'FacebookUser',
)

class Pizza(models.Model):
    name = models.CharField(max_length=30)
    toppings = models.ManyToManyField('Topping')

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class FacebookUser(models.Model):
    name = models.CharField(max_length=30)
    friends = models.ManyToManyField(
        'self',
        blank=True,
    )

    # 자기자신 (TwitterUser('self'))를 참조해서
    # friends 필드를 MTM으로 정의

class InstagramUser(models.Model):
    name = models.CharField(max_length=30)
    # symentrical = False 를 옵셥으로
    follower = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
    )

