# Generated by Django 4.2 on 2023-04-08 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='description',
        ),
        migrations.AddField(
            model_name='todo',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.CreateModel(
            name='TodoItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True, null=True)),
                ('todo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.todo')),
            ],
        ),
    ]