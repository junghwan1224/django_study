# Generated by Django 2.1.5 on 2019-02-15 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0008_auto_20190215_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_status',
            field=models.CharField(choices=[('Deal', '거래중'), ('End', '거래완료')], default='Deal', max_length=10),
        ),
    ]