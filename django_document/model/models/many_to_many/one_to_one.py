from django.db import models

__all__ = (
    'Place',
    'Restaurant',
    'Waiter'
)


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)


    def __str__(self):
        return f'{self.name} the place'

class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
        # primary_key는 변경 불가 바꾸게 되면 primary_key 복제되서 다시 변수로 저장
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.place.name} the restaurant'

class Waiter(models.Model):
    restarant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.place.name} the Waiter'

