# Generated by Django 5.1.6 on 2025-03-06 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_testimonial_rating_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='user_image',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
