# Generated by Django 2.2 on 2021-10-02 00:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('storylineapp', '0008_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=sorl.thumbnail.fields.ImageField(default=django.utils.timezone.now, upload_to='profiles'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='storylineapp.User'),
        ),
    ]
