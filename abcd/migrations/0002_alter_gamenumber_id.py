# Generated by Django 3.2.3 on 2021-05-24 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abcd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamenumber',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
