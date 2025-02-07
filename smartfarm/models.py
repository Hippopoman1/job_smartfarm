from django.db import models

class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('farmer', 'Farmer'),
    ]
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255,unique=True)
    # phonenumber = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES,default="Farmer")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    last_login = models.DateTimeField(null=True, blank=True)

class project(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE)

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

class WateringSchedule(models.Model):
    STATUS_CHOICES = [
        ('on', 'On'),
        ('off', 'Off'),
    ]
    
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=3, choices=STATUS_CHOICES)

class Notification(models.Model):
    STATUS_CHOICES = [
        ('sent', 'Sent'),
        ('pending', 'Pending'),
        ('failed', 'Failed'),
    ]
    
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    message = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

class WaterUsage(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    water_used = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class IoTDevice(models.Model):
    STATUS_CHOICES = [
        ('online', 'Online'),
        ('offline', 'Offline'),
    ]
    
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    device_type = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

class BackupLog(models.Model):
    STATUS_CHOICES = [
        ('success', 'Success'),
        ('failed', 'Failed'),
    ]
    
    backup_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    backup_file_path = models.CharField(max_length=255)

class MaintenanceLog(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'admin'})
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
