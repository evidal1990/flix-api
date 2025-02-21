# Generated by Django 5.1.2 on 2024-11-20 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("actors", "0002_alter_actor_nationality"),
    ]

    operations = [
        migrations.AlterField(
            model_name="actor",
            name="nationality",
            field=models.CharField(
                blank=True,
                choices=[
                    ("FR", "Francês"),
                    ("US", "Americano"),
                    ("IT", "Italiano"),
                    ("JP", "Japonês"),
                    ("CH", "Chinês"),
                    ("BR", "Brasileiro"),
                    ("IN", "Indiano"),
                    ("DE", "Alemão"),
                    ("ES", "Espanhol"),
                    ("GB", "Inglês"),
                    ("MX", "Mexicano"),
                    ("AU", "Australiano"),
                    ("CA", "Canadense"),
                    ("IS", "Israelense"),
                ],
                max_length=100,
                null=True,
            ),
        ),
    ]
