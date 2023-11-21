# Generated by Django 4.2.7 on 2023-11-21 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('login', models.CharField(max_length=255)),
                ('pswrd', models.CharField(max_length=128, verbose_name='password')),
            ],
        ),
    ]
