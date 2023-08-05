# Generated by Django 4.2.4 on 2023-08-05 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0003_remove_vaccinationcenter_address_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vaccinationcenter",
            name="working_hours",
        ),
        migrations.AddField(
            model_name="vaccinationcenter",
            name="working_hours_end",
            field=models.TimeField(default="00:00"),
        ),
        migrations.AddField(
            model_name="vaccinationcenter",
            name="working_hours_start",
            field=models.TimeField(default="00:00"),
        ),
        migrations.AlterField(
            model_name="vaccinationcenter",
            name="slots",
            field=models.PositiveIntegerField(default=10),
        ),
    ]