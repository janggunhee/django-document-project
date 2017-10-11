from multiprocessing.managers import BaseManager

from django.db import models


__all__ = (
    'Idol',
    'Group',
    'Membership',
)


class Idol(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)
    debut_date = models.DateField()
    members = models.ManyToManyField(
        Idol,
        through='Membership',
        through_fields=('group', 'idol') # intermediate (idol,Group) table 지정
    )

    def __str__(self):
        return self.name

class Membership(models.Model):
    idol = models.ForeignKey(
        Idol,
        on_delete=models.CASCADE,
        related_name='membership_set'
    )
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    #recommoneder = models.ForeignKey(
    #    Idol,
    #    null=True,
    #    on_delete=models.SET_NULL,
    #    related_name='recommend_membership_set',
    #)
    recommender = models.ManyToManyField(
        Idol,
        blank=True,
        related_name='recommend_membership_set', # _set 기본의 집합
    )
    joined_date = models.DateField()
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.group.name}' \
               f'{self.Idol.name}' \
               f'({self.is_active.name})'
