from django.db import models

__all__ = (
    'Car',
    'Manufacturer',
    'User',
)


class Car(models.Model):
    manufacturer = models.ForeignKey(
        'Manufacturer',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.manufacturer.name} - {self.name}'


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    def save(self, *args, **kwargs):
        if self.teacher and self.teacher.pk == self.pk:
            print("insult other name")
            self.teacher = None
        super(User, self).save(*args, *kwargs)

    def __str__(self):
        return self.name
