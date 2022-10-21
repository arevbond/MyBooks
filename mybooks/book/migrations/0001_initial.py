# Generated by Django 4.1.2 on 2022-10-19 10:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название книги')),
                ('author', models.CharField(max_length=100, verbose_name='Автор книги')),
                ('category', models.CharField(choices=[('artistic', 'Художественная литература'), ('non_artistic', 'Не художественная литература')], max_length=50, verbose_name='Категория')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Обложка')),
                ('review', models.TextField(verbose_name='Рецензия')),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)], verbose_name='Оценка')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создание')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('favorite', models.BooleanField(default=False, verbose_name='Любимая книга')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]