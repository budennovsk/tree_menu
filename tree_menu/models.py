from django.db import models


# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=150)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               related_name='children',
                               blank=True,
                               null=True,
                               verbose_name='Родитель'
                               )
    is_main = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элементы меню'

    def __str__(self):
        return f'{self.name}'
