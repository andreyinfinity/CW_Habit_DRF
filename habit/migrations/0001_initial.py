# Generated by Django 4.2 on 2024-03-10 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_of_execution', models.CharField(blank=True, max_length=256, null=True, verbose_name='место выполнения')),
                ('action', models.TextField(verbose_name='действие')),
                ('time_of_execution', models.DateTimeField(blank=True, null=True, verbose_name='время начала выполнения')),
                ('time_to_complete', models.PositiveIntegerField(blank=True, null=True, verbose_name='длительность выполнения в секундах')),
                ('periodicity_in_days', models.PositiveIntegerField(verbose_name='периодичность в днях')),
                ('award', models.CharField(blank=True, max_length=256, null=True, verbose_name='вознаграждение')),
                ('is_pleasant', models.BooleanField(verbose_name='признак приятной привычки')),
                ('is_public', models.BooleanField(verbose_name='признак публичности')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habit.habit', verbose_name='связанная привычка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='создатель')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
                'ordering': ['action'],
            },
        ),
    ]
