from django.db import models



class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=100, blank=True, null=True, verbose_name='Описание')

    def __string__(self):
        return self.name

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'


class Measurement(models.Model):
    sensor = models.ForeignKey(
        Sensor,
        on_delete=models.CASCADE,
        related_name='measurements',
        verbose_name='Датчик'
    )

    temperature = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='Температура'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время измерения'
    )

    image = models.ImageField(
        null=True,
        blank=True,  # ← Добавьте это
        upload_to='measurements/',
        verbose_name='Изображение'  #
    )


    def __str__(self):
        return f'{self.sensor.name}: {self.temperature}°C'

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
        ordering = ['-created_at']