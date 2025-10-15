from rest_framework import serializers

from measurement.models import Sensor, Measurement


# TODO: опишите необходимые сериализаторы

class SensorSerializer(serializers.ModelSerializer): #для создания/обновления датчиков и списка
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class MeasurementSerializer(serializers.ModelSerializer):#для измерений температуры
    class Meta:
        model = Measurement
        fields = ['id', 'temperature', 'created_at', 'sensor']

class SensorDetailSerializer(serializers.ModelSerializer):#для детальной информации с вложенными измерениями
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
