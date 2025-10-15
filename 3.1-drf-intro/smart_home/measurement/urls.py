from django.urls import path

from measurement.views import SensorListCreateView, SensorDetailView, MeasurementCreateView

urlpatterns = [
    path('sensors/', SensorListCreateView.as_view(), name='sensors'),
    path('sensors/<int:pk>/', SensorDetailView.as_view(), name='sensor-detail'),
    path('measurements/', MeasurementCreateView.as_view(), name='measurements'),


    # TODO: зарегистрируйте необходимые маршруты
]
