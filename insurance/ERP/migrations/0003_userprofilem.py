# Generated by Django 4.0.5 on 2022-06-11 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ERP', '0002_company_info_page_lod_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileM',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='User_image')),
                ('otp', models.CharField(blank=True, max_length=6, null=True)),
                ('Email', models.CharField(blank=True, max_length=30, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
