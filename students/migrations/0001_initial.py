from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("age", models.PositiveIntegerField()),
                ("course", models.CharField(max_length=100)),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                        default="M",
                        max_length=1,
                    ),
                ),
                ("phone", models.CharField(blank=True, max_length=15)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
