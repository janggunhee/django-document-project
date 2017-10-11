from django.db import models

__all__ = (
    'InstagramUser',
)
class InstagramUser(models.Model):
    name = models.CharField(max_length=30)
    # symentrical = False 를 옵셥으로
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
    )
    def __str__(self):
        return self.name
