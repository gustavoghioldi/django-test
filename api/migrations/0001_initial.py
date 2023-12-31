# Generated by Django 4.2.6 on 2023-10-23 23:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TicketModel",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("artist", models.CharField(max_length=128)),
                ("date", models.DateTimeField()),
            ],
        ),
    ]
