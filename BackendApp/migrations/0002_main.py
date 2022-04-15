# Generated by Django 3.2.13 on 2022-04-15 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BackendApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='BackendApp.event')),
            ],
        ),
    ]