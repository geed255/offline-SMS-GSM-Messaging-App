# Generated by Django 2.2.3 on 2019-08-02 10:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_contact_marked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='marked',
        ),
        migrations.AddField(
            model_name='contact',
            name='date_registred',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]