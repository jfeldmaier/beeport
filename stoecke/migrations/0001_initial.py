# Generated by Django 4.2.17 on 2025-01-09 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stoecke',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('colony_type', models.CharField(choices=[('W', 'Wirtschaftsvolk'), ('A', 'Ableger'), ('J', 'Jungvolk'), ('S', 'Schwarm'), ('F', 'Flugling')], max_length=1)),
                ('date_created', models.DateField()),
                ('date_queen_added', models.DateField()),
                ('queen_color', models.CharField(max_length=20)),
                ('queen_number', models.IntegerField()),
                ('bee_race', models.CharField(max_length=50)),
            ],
        ),
    ]