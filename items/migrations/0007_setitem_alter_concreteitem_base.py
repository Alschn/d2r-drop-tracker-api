# Generated by Django 4.0.3 on 2022-04-14 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_alter_item_type_alter_itembase_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='SetItem',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Set items',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('items.concreteitem',),
        ),
        migrations.AlterField(
            model_name='concreteitem',
            name='base',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='items.itembase'),
        ),
    ]
