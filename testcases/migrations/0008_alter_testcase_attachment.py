# Generated by Django 4.0.3 on 2022-03-06 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("testcases", "0007_alter_testcase_attachment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="testcase",
            name="attachment",
            field=models.FileField(
                blank=True, max_length=255, null=True, upload_to="uploads/%Y/%m/%d/"
            ),
        ),
    ]
