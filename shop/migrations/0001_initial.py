# Generated by Django 3.2 on 2021-07-11 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('description', models.TextField(blank=True)),
                ('category', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
    ]