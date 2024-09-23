# Generated by Django 5.1 on 2024-09-23 11:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=123, verbose_name='Имя')),
                ('phone_number', models.CharField(max_length=17, unique=True, verbose_name='Номер телефона')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Электронная почта')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Обычный пользователь'), (2, 'Менеджер'), (3, 'Консультант'), (4, 'Админ')], default=1, verbose_name='Статус пользователя')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Администратор')),
                ('bookings', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='tour.booking')),
                ('favorite_tours', models.ManyToManyField(blank=True, related_name='users', to='tour.tour')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
