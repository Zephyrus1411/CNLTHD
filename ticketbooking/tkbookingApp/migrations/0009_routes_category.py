# Generated by Django 4.0.4 on 2022-05-04 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tkbookingApp', '0008_remove_buses_type_alter_ticketbooking_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='routes',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tkbookingApp.category'),
        ),
    ]
