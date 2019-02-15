# Generated by Django 2.1.5 on 2019-02-13 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='apply_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='apply_user', to=settings.AUTH_USER_MODEL),
        ),
    ]