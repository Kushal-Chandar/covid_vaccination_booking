# Generated by Django 4.2.4 on 2023-08-05 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking", "0006_delete_userprofile"),
    ]

    operations = [
        migrations.AddField(
            model_name="vaccinationcenter",
            name="dosage",
            field=models.CharField(default="type1", max_length=100),
            preserve_default=False,
        ),
    ]
