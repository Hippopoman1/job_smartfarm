from rest_framework import viewsets
from smartfarm.models import User, WeatherData, Farmer, WateringSchedule, Notification, WaterUsage, IoTDevice, BackupLog, MaintenanceLog

from .serializers import UserSerializer, WeatherDataSerializer, FarmerSerializer, WateringScheduleSerializer,NotificationSerializer, WaterUsageSerializer, IoTDeviceSerializer, BackupLogSerializer, MaintenanceLogSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class WeatherDataViewSet(viewsets.ModelViewSet):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer


class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer


class WateringScheduleViewSet(viewsets.ModelViewSet):
    queryset = WateringSchedule.objects.all()
    serializer_class = WateringScheduleSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class WaterUsageViewSet(viewsets.ModelViewSet):
    queryset = WaterUsage.objects.all()
    serializer_class = WaterUsageSerializer


class IoTDeviceViewSet(viewsets.ModelViewSet):
    queryset = IoTDevice.objects.all()
    serializer_class = IoTDeviceSerializer


class BackupLogViewSet(viewsets.ModelViewSet):
    queryset = BackupLog.objects.all()
    serializer_class = BackupLogSerializer


class MaintenanceLogViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceLog.objects.all()
    serializer_class = MaintenanceLogSerializer
