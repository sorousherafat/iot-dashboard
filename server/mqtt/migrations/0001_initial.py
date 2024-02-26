# Generated by Django 5.0.2 on 2024-02-26 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Data",
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
                ("temperature", models.FloatField()),
                ("humidity", models.FloatField()),
                ("light", models.IntegerField()),
                ("wifi", models.CharField(max_length=256)),
                ("relay", models.BooleanField()),
                ("timestamp", models.DateTimeField(auto_now=True)),
            ],
            options={
                "indexes": [
                    models.Index(
                        fields=["timestamp"], name="mqtt_data_timesta_70ff49_idx"
                    )
                ],
            },
        ),
    ]
