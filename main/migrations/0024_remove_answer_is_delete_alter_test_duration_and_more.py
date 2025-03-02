# Generated by Django 4.2.6 on 2024-12-29 13:44

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_test_is_random_test_question_count_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='is_delete',
        ),
        migrations.AlterField(
            model_name='test',
            name='duration',
            field=models.PositiveIntegerField(default=20, verbose_name='test yechish vaqti (minut hisobida)'),
        ),
        migrations.AlterField(
            model_name='test',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 30, 13, 44, 4, 969342, tzinfo=datetime.timezone.utc), verbose_name='test tugash sanasi'),
        ),
        migrations.AlterField(
            model_name='test',
            name='is_anonym',
            field=models.BooleanField(default=False, verbose_name="testni bosh menyuda ko'rsatmaslik"),
        ),
        migrations.AlterField(
            model_name='test',
            name='pass_percentage',
            field=models.PositiveIntegerField(default=60, verbose_name="testdan o'tish foizi"),
        ),
        migrations.AlterField(
            model_name='test',
            name='question_count',
            field=models.PositiveIntegerField(verbose_name='testda tushadigan savollar soni'),
        ),
        migrations.AlterField(
            model_name='test',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='test boshlanish sanasi'),
        ),
    ]
