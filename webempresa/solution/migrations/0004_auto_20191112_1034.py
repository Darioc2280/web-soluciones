# Generated by Django 2.0 on 2019-11-12 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solution', '0003_auto_20191112_0933'),
    ]

    operations = [
        migrations.RenameField(
            model_name='query',
            old_name='imagen',
            new_name='image',
        ),
    ]
