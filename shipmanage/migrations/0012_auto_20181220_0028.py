# Generated by Django 2.0.2 on 2018-12-19 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipmanage', '0011_auto_20181220_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='arrive_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='201812200028318930', editable=False, max_length=18, primary_key=True, serialize=False),
        ),
    ]
