# Generated by Django 4.1.7 on 2023-06-20 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("myapi", "0002_alter_capital_location_alter_city_location_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="country",
            name="country_capital",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="country",
                to="myapi.capital",
            ),
        ),
        migrations.AddField(
            model_name="country",
            name="country_city",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="countries",
                to="myapi.city",
            ),
        ),
    ]
