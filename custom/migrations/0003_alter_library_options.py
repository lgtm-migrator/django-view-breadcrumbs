# Generated by Django 3.2.6 on 2021-08-04 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("custom", "0002_auto_20210804_0828"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="library",
            options={"verbose_name": "library", "verbose_name_plural": "libraries"},
        ),
    ]