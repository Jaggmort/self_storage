# Generated by Django 4.2 on 2023-04-21 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField(null=True, verbose_name='Размеры')),
                ('volume', models.IntegerField(null=True, verbose_name='Объем')),
                ('paid_from', models.DateTimeField(null=True, verbose_name='Оплачено с')),
                ('paid_till', models.DateTimeField(null=True, verbose_name='Оплачено по')),
                ('description', models.TextField(null=True, verbose_name='Хранимые вещи')),
            ],
            options={
                'verbose_name': 'бокс',
                'verbose_name_plural': 'Боксы',
            },
        ),
        migrations.CreateModel(
            name='Promocodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('discount', models.IntegerField(verbose_name='Скидка в %')),
                ('valid_from', models.DateTimeField(null=True, verbose_name='С какой даты работает')),
                ('valid_till', models.DateTimeField(null=True, verbose_name='До какой даты работает')),
            ],
            options={
                'verbose_name': 'промокод',
                'verbose_name_plural': 'Промокоды',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_username', models.CharField(max_length=100, verbose_name='Никнейм в мессенджере')),
                ('chat_id', models.IntegerField(verbose_name='ID чата')),
                ('phone', models.CharField(max_length=10, null=True, verbose_name='Телефон')),
                ('address', models.TextField(null=True, verbose_name='Адрес')),
                ('utm_source', models.CharField(max_length=100, null=True, verbose_name='Откуда пришел')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='TransferRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer_type', models.IntegerField(choices=[(0, 'Забор груза'), (1, 'Доставка груза')], verbose_name='Тип трансфера')),
                ('address', models.TextField(verbose_name='Адрес забора/доставки')),
                ('time_arrive', models.DateTimeField(null=True, verbose_name='Желаемое время')),
                ('is_complete', models.BooleanField(default=False, verbose_name='Исполнено?')),
                ('is_call_needed', models.BooleanField(default=False, verbose_name='Нужен ли обратный звонок')),
                ('box_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.box', verbose_name='Бокс')),
            ],
            options={
                'verbose_name': 'трансфер',
                'verbose_name_plural': 'Трансферы',
            },
        ),
        migrations.AddField(
            model_name='box',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.user', verbose_name='Клиент'),
        ),
    ]
