from django.db import models


class User(models.Model):
    ROLE_CHOICES = [('admin', 'Admin'), ('farmer', 'Farmer')]
    STATUS_CHOICES = [('active', 'Active'), ('inactive', 'Inactive')]

    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Farmer')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    last_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username


class WeatherData(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    rainfall = models.FloatField()
    wind_speed = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Farmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    farm_location = models.CharField(max_length=255)
    plant_type = models.CharField(max_length=50)
    water_requirement = models.FloatField()

    def __str__(self):
        return f"Farmer: {self.user.username}"


class WateringSchedule(models.Model):
    STATUS_CHOICES = [('on', 'On'), ('off', 'Off')]

    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default='off')


class Notification(models.Model):
    STATUS_CHOICES = [('sent', 'Sent'), ('pending', 'Pending'), ('failed', 'Failed')]

    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    message = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    timestamp = models.DateTimeField(auto_now_add=True)


class WaterUsage(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    water_used = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


class IoTDevice(models.Model):
    STATUS_CHOICES = [('online', 'Online'), ('offline', 'Offline')]

    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    device_type = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='offline')


class BackupLog(models.Model):
    STATUS_CHOICES = [('success', 'Success'), ('failed', 'Failed')]

    backup_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    backup_file_path = models.CharField(max_length=255)


class MaintenanceLog(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'admin'})
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
