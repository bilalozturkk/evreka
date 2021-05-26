# Generated by Django 3.2.3 on 2021-05-22 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_2', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='frequencies',
            constraint=models.UniqueConstraint(fields=('operation', 'bin'), name='Operaition-Bin pairs must be unique'),
        ),
    ]
