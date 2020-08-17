# Generated by Django 3.0.7 on 2020-08-17 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageFlag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag_type', models.CharField(choices=[('Suicidal', 'Suicidal Ideation'), ('Violent', 'Potential Violence'), ('Harassment', 'Harassment')], max_length=32)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('flagged_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='profile.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='profile.Profile')),
            ],
        ),
    ]
