# Generated by Django 4.1.1 on 2022-10-01 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuestBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=30, verbose_name='Имя автора')),
                ('author_email', models.EmailField(max_length=30, verbose_name='Почта автора')),
                ('text', models.TextField(max_length=400, verbose_name='Текст')),
                ('status', models.CharField(default='active', max_length=100, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('changed_at', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
            ],
        ),
    ]