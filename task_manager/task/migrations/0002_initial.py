# Generated by Django 4.2.7 on 2023-12-10 06:30

from django.conf import settings
from django.db import migrations, models
from django.db.models.deletion import PROTECT


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('label', '0001_initial'),
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='author',
            field=models.ForeignKey(on_delete=PROTECT,
                                    related_name='author',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task',
            name='executor',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=PROTECT,
                                    related_name='executor',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(blank=True,
                                         related_name='labels',
                                         to='label.label'),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.ForeignKey(on_delete=PROTECT,
                                    related_name='status',
                                    to='status.status'),
        ),
    ]
