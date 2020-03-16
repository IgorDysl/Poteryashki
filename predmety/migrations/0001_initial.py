# Generated by Django 3.0.3 on 2020-03-16 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Predmet',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='Предмет')),
                ('image', models.ImageField(blank=True, upload_to='photos', verbose_name='Фото')),
                ('text', models.TextField(verbose_name='Текст')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50, verbose_name='Автор')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('predmet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='predmety.Predmet')),
            ],
        ),
    ]
