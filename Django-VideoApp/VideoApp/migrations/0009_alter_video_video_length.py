# Generated by Django 4.0.6 on 2022-07-21 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VideoApp', '0008_alter_video_video_size_in_mb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_length',
            field=models.TimeField(editable=False, null=True),
        ),
    ]
