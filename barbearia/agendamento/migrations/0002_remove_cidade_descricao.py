# Generated by Django 2.1.7 on 2019-11-30 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agendamento', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cidade',
            name='descricao',
        ),
    ]