# Generated by Django 2.1.5 on 2019-02-08 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_purchasepost_sellpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='purchasepost',
            name='post_type',
            field=models.CharField(choices=[('Buy', '구매글'), ('Sell', '판매글')], default='Buy', max_length=10),
        ),
        migrations.AddField(
            model_name='sellpost',
            name='post_type',
            field=models.CharField(choices=[('Buy', '구매글'), ('Sell', '판매글')], default='Buy', max_length=10),
        ),
    ]
