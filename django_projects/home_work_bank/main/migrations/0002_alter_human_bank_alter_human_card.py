# Generated by Django 4.2.7 on 2023-11-20 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='human',
            name='bank',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.bank'),
        ),
        migrations.AlterField(
            model_name='human',
            name='card',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.card'),
        ),
    ]