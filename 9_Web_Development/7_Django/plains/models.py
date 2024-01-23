from django.db import models
from django.forms import ValidationError


from main.models import City


class Plains(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Номер самолета')
    travel_time = models.PositiveIntegerField(verbose_name='Время в пути')
    fromCity = models.ForeignKey(City, on_delete=models.CASCADE, related_name='from_city_set', verbose_name='Из какого города')
    toCity = models.ForeignKey(City, on_delete=models.CASCADE, related_name='to_city_set', verbose_name='В какой город')
    
    def __str__(self):
        return f'Самолет под номером {self.name} из города - {self.fromCity}'
    
    class Meta:
        verbose_name = 'Самолет'
        verbose_name_plural = 'Самолеты'
        ordering = ('travel_time',)

    def clean(self):
        if self.fromCity == self.toCity:
            raise ValidationError('Измените город прибытия')
        qs = Plains.objects.filter(
            fromCity = self.fromCity, toCity = self.toCity, travel_time = self.travel_time).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError('Измените время')
    
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)