# Generated by Django 3.0.7 on 2020-08-15 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0003_auto_20200814_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(default='', max_length=20)),
                ('reciever', models.CharField(default='', max_length=20)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
    ]