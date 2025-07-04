# Generated by Django 5.2.3 on 2025-06-27 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Establishment',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('short_title', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('adress', models.CharField(max_length=200)),
                ('tel', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('wsite', models.URLField(blank=True, null=True)),
                ('wtel', models.URLField(blank=True, null=True)),
                ('wvk', models.URLField(blank=True, null=True)),
                ('winsta', models.URLField(blank=True, null=True)),
                ('wface', models.URLField(blank=True, null=True)),
                ('wtwit', models.URLField(blank=True, null=True)),
                ('wtic', models.URLField(blank=True, null=True)),
                ('wother', models.URLField(blank=True, null=True)),
                ('icon', models.CharField(max_length=100)),
                ('prev', models.CharField(blank=True, max_length=100)),
                ('promo_medio', models.CharField(blank=True, max_length=100)),
                ('coords', models.CharField(max_length=50)),
            ],
        ),
    ]
