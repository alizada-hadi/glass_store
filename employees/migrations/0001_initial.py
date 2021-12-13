# Generated by Django 4.0 on 2021-12-12 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=14, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('salary', models.IntegerField(default=0)),
            ],
        ),
    ]