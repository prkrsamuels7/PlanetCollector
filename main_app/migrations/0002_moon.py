# Generated by Django 4.0.3 on 2022-05-12 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('namesake', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.planet')),
            ],
        ),
    ]
