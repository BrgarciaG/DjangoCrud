# Generated by Django 4.2.3 on 2023-07-27 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_crea_modelo_personas'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='imc',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
