# Generated by Django 4.1.7 on 2023-04-20 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AccessRecords',
            new_name='AccessRecord',
        ),
        migrations.AlterField(
            model_name='webpage',
            name='email',
            field=models.EmailField(default='cricket@gmail.com', max_length=254),
        ),
    ]