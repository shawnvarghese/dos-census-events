# Generated by Django 2.2.7 on 2019-12-05 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0014_auto_20191204_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_private_event',
            field=models.BooleanField(default=False, help_text='Would you like to hide this event from the public?', verbose_name='Private Event'),
        ),
    ]
