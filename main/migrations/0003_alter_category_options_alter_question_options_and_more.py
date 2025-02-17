# Generated by Django 4.2.6 on 2023-10-10 11:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_alter_test_end_date_alter_test_start_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Kategoriya', 'verbose_name_plural': 'Kategoriyalar'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Savol', 'verbose_name_plural': 'Savollar'},
        ),
        migrations.AlterModelOptions(
            name='test',
            options={'verbose_name': 'Test', 'verbose_name_plural': 'Testlar'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=60, verbose_name='nomi'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_a',
            field=models.CharField(max_length=250, verbose_name='a javob'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_b',
            field=models.CharField(max_length=250, verbose_name='b javob'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_c',
            field=models.CharField(max_length=250, verbose_name='c javob'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_d',
            field=models.CharField(max_length=250, verbose_name='d javob'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=400, verbose_name='savol'),
        ),
        migrations.AlterField(
            model_name='question',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='main.test'),
        ),
        migrations.AlterField(
            model_name='question',
            name='true_answer',
            field=models.CharField(max_length=250, verbose_name="to'g'ri javob"),
        ),
        migrations.AlterField(
            model_name='test',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='avtor'),
        ),
        migrations.AlterField(
            model_name='test',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='kategoriya'),
        ),
        migrations.AlterField(
            model_name='test',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 12, 11, 46, 35, 853112, tzinfo=datetime.timezone.utc), verbose_name='tugash sanasi'),
        ),
        migrations.AlterField(
            model_name='test',
            name='maximum_attemps',
            field=models.PositiveIntegerField(verbose_name='maksimum harakatlar soni'),
        ),
        migrations.AlterField(
            model_name='test',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='boshlanish sanasi'),
        ),
        migrations.AlterField(
            model_name='test',
            name='title',
            field=models.CharField(max_length=250, verbose_name='sarlavha'),
        ),
    ]
