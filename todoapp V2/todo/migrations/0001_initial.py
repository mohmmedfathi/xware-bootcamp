# Generated by Django 4.1 on 2022-08-11 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.EmailField(max_length=100)),
                ('email', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('describtion', models.CharField(max_length=100)),
                ('finished_date', models.DateTimeField()),
                ('task_note', models.TextField()),
                ('user_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.user')),
            ],
        ),
    ]