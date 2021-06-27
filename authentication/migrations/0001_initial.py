# Generated by Django 3.2.4 on 2021-06-27 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserActivity',
            fields=[
                ('user', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('last_request', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user_activity',
            },
        ),
    ]
