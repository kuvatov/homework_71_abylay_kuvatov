# Generated by Django 4.1.7 on 2023-03-26 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("instagram", "0005_alter_publication_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="like",
            name="publication",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="likes",
                to="instagram.publication",
                verbose_name="Публикация",
            ),
        ),
    ]
