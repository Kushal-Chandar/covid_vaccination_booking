# Generated by Django 4.2.4 on 2023-08-05 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0002_delete_vaccinationslot"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vaccinationcenter",
            name="address",
        ),
        migrations.AddField(
            model_name="vaccinationcenter",
            name="slots",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
