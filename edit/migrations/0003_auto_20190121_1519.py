# Generated by Django 2.1.5 on 2019-01-21 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edit', '0002_auto_20190121_0212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='summer_note_model',
            name='attachment_ptr',
        ),
        migrations.DeleteModel(
            name='summer_note_model',
        ),
    ]
