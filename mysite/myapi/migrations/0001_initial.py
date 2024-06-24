# Generated by Django 4.1.7 on 2023-06-19 06:44

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
import django.contrib.gis.geos.polygon
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Capital",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=60)),
                (
                    "location",
                    django.contrib.gis.db.models.fields.PointField(
                        default=django.contrib.gis.geos.point.Point(0, 0), srid=4326
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=60)),
                (
                    "description",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("photo", models.ImageField(upload_to="images/")),
                (
                    "location",
                    django.contrib.gis.db.models.fields.PointField(
                        default=django.contrib.gis.geos.point.Point(0, 0), srid=4326
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=60)),
                (
                    "location",
                    django.contrib.gis.db.models.fields.PolygonField(
                        default=django.contrib.gis.geos.polygon.Polygon(
                            ((0, 0), (0, 1), (1, 1), (1, 0), (0, 0))
                        ),
                        srid=4326,
                    ),
                ),
            ],
        ),
    ]