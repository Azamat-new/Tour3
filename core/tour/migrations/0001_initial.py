# Generated by Django 5.1 on 2024-09-24 13:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('banner_image', models.ImageField(upload_to='banners/', verbose_name='Изображение')),
                ('is_asset', models.BooleanField(default=True, verbose_name='Активность')),
            ],
            options={
                'verbose_name': 'Баннер',
                'verbose_name_plural': 'Баннеры',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participants', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество участников')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Итоговая цена')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'В ожидании'), (2, 'Подтверждено'), (3, 'Отклонено')], verbose_name='Статус бронирования')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название категории')),
                ('description', models.TextField(verbose_name='Описание категории')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DateTour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Дата начала тура')),
                ('end_date', models.DateField(verbose_name='Дата окончания тура')),
                ('tour_type', models.CharField(choices=[('group', 'Групповой'), ('individual', 'Индивидуальный')], max_length=20, verbose_name='Тип тура')),
                ('season', models.CharField(choices=[('spring', 'Весна'), ('summer', 'Лето'), ('autumn', 'Осень'), ('winter', 'Зима')], max_length=100, verbose_name='Сезон')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('user_name', models.CharField(blank=True, max_length=100, null=True)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Оценка')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
        ),
        migrations.CreateModel(
            name='RegionTour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название региона')),
                ('description', models.TextField(verbose_name='Описание региона')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='regions_image/', verbose_name='Изображение региона')),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(max_length=500, verbose_name='Описание тура')),
                ('route_tour', models.CharField(max_length=200, verbose_name='Маршрут тура')),
                ('duration', models.IntegerField(verbose_name='Продолжительность (дни)')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена со скидкой')),
                ('discount_start_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата начала скидки')),
                ('discount_end_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания скидки')),
                ('participants_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена за участника')),
                ('max_participants', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Максимальное количество участников')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликован')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Админская')),
            ],
        ),
        migrations.CreateModel(
            name='TourImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='tours_images/', verbose_name='Изображение')),
            ],
        ),
    ]
