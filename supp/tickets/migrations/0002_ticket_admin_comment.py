# Generated by Django 4.0.1 on 2022-01-13 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='admin_comment',
            field=models.TextField(blank=True, max_length=500, verbose_name='Комментарий администрации'),
        ),
    ]
