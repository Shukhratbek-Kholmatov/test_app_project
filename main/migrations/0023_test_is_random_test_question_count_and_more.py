# Generated by Django 4.2.6 on 2024-12-28 09:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_test_is_anonym_alter_checkquestion_is_true_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='is_random',
            field=models.BooleanField(default=False, verbose_name='savollarni random chiqarish'),
        ),
        migrations.AddField(
            model_name='test',
            name='question_count',
            field=models.PositiveIntegerField(default=5, verbose_name='savollar soni'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='test',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 29, 9, 44, 16, 208765, tzinfo=datetime.timezone.utc), verbose_name='tugash sanasi'),
        ),
        migrations.AlterField(
            model_name='test',
            name='is_anonym',
            field=models.BooleanField(default=False, verbose_name="bosh menyuda ko'rsatmaslik"),
        ),
        migrations.AlterField(
            model_name='test',
            name='maximum_attemps',
            field=models.PositiveIntegerField(verbose_name='maksimum urinishlar soni'),
        ),
        migrations.AlterField(
            model_name='test',
            name='title',
            field=models.CharField(max_length=250, verbose_name='test nomi'),
        ),
    ]
