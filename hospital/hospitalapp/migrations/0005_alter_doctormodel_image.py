# Generated by Django 3.2.3 on 2021-07-18 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0004_auto_20210717_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctormodel',
            name='image',
            field=models.ImageField(default='', upload_to='static'),
        ),
    ]
