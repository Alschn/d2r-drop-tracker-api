# Generated by Django 4.0.3 on 2022-04-05 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_set_level_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runeinruneword',
            name='rune',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.rune'),
        ),
        migrations.AlterField(
            model_name='runeinruneword',
            name='runeword',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.runeword'),
        ),
    ]
