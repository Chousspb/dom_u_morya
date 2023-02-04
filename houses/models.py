from django.db import models

class House(models.Model):
    name = models.CharField('название', max_length=50)
    price = models.IntegerField('цена')
    description = models.TextField('описание')
    photo = models.ImageField('фотография', upload_to='houses/photo', default='', blank=True)

    class Meta:
        verbose_name = 'дом'
        verbose_name_plural = 'дома'
        ordering = ['price']

    def __str__(self):
        return self.name.upper()