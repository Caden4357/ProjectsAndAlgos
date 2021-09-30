# Generated by Django 2.2 on 2021-09-29 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storylineapp', '0002_auto_20210928_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=100000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('writer_of_the_story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_of_the_story', to='storylineapp.User')),
            ],
        ),
    ]
