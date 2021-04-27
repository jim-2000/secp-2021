# Generated by Django 3.2 on 2021-04-27 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='album/photos/')),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
