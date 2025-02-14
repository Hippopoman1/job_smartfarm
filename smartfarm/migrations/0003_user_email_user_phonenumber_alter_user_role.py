# Generated by Django 5.1.3 on 2025-02-06 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartfarm', '0002_backuplog_weatherdata_remove_device_token_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phonenumber',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('farmer', 'Farmer')], default='Farmer', max_length=10),
        ),
    ]
