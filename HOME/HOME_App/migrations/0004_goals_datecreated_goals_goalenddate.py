# Generated by Django 4.1.4 on 2022-12-29 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME_App', '0003_rename_client_goals_selectclient'),
    ]

    operations = [
        migrations.AddField(
            model_name='goals',
            name='dateCreated',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='goals',
            name='goalEndDate',
            field=models.DateField(null=True),
        ),
    ]
