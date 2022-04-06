# Generated by Django 4.0.3 on 2022-04-04 09:56

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('characters', '0001_initial'),
        ('items', '0001_initial'),
        ('areas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemFind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sold_for', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01000000000000000020816681711721685132943093776702880859375'))])),
                ('sold_at', models.DateTimeField(blank=True, null=True)),
                ('sold_to', models.URLField(blank=True, null=True)),
                ('statistics', models.JSONField(blank=True, default=dict, null=True)),
                ('found_at', models.DateTimeField(blank=True, null=True)),
                ('found_on_difficulty', models.CharField(blank=True, choices=[('normal', 'Normal'), ('nightmare', 'Nightmare'), ('hell', 'Hell')], max_length=9, null=True)),
                ('found_on_players', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)])),
                ('found_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='characters.character')),
                ('found_in', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='areas.area')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.item')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
