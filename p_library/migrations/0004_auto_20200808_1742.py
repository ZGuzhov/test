# Generated by Django 3.1 on 2020-08-08 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0003_auto_20200804_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publish',
            name='title',
            field=models.TextField(),
        ),
    ]