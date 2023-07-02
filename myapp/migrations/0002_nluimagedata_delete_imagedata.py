# Generated by Django 4.2.2 on 2023-07-02 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="nluImageData",
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
                ("Name", models.CharField(max_length=50)),
                ("Image", models.ImageField(upload_to="img/")),
                ("Resume", models.FileField(upload_to="resume/")),
            ],
        ),
        migrations.DeleteModel(name="ImageData",),
    ]