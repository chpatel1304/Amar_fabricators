# Generated by Django 5.0.6 on 2024-06-05 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_career'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='cv',
            field=models.FileField(upload_to='F:/Amar Project/media/cvs/'),
        ),
    ]
