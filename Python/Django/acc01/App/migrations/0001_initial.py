# Generated by Django 4.2.7 on 2023-11-19 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []
    # 生成的Model迁移文件
    operations = [
        migrations.CreateModel(
            name="Appuser",
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
                ("name", models.CharField(max_length=10)),
                ("age", models.IntegerField()),
                ("sex", models.CharField(max_length=10)),
            ],
        ),
    ]
