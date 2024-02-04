# Generated by Django 3.2.23 on 2024-02-03 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Menu', '0004_auto_20240203_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_costomer', to=settings.AUTH_USER_MODEL)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_food', to='Menu.food')),
            ],
        ),
    ]
