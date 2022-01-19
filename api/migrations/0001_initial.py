# Generated by Django 3.2.9 on 2022-01-19 04:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('inv_primary', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('inventory_id', models.CharField(max_length=50, unique=True)),
                ('inventory_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('wh_primary', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('warehouse_id', models.CharField(max_length=50, unique=True)),
                ('warehouse_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WarehouseInventoryRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.inventory')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.warehouse')),
            ],
        ),
    ]