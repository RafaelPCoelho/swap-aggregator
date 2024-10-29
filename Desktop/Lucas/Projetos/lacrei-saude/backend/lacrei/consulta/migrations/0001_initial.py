# Generated by Django 5.1.2 on 2024-10-28 20:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profissional', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('profissional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profissional.profissional')),
            ],
        ),
    ]
