# Generated by Django 3.1.2 on 2020-10-16 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('instructions', models.TextField()),
                ('time_required', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='img')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_app.author')),
            ],
        ),
    ]
