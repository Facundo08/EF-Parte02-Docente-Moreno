# Generated by Django 4.2.6 on 2023-12-18 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0003_docente'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Editorial',
        ),
        migrations.DeleteModel(
            name='Pais',
        ),
    ]
