# Generated by Django 4.2.7 on 2023-11-20 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_human_bank_alter_human_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='human',
            name='bank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.bank'),
        ),
        migrations.AlterField(
            model_name='human',
            name='card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.card'),
        ),
    ]
