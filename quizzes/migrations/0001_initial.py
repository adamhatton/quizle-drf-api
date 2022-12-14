# Generated by Django 3.2.16 on 2022-11-05 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('', 'Pick a Category'), ('sport', 'Sport'), ('music', 'Music'), ('entertainment', 'Entertainment'), ('general', 'General Knowledge')], max_length=13)),
                ('time_limit_seconds', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('ans_1', models.CharField(max_length=50)),
                ('ans_2', models.CharField(max_length=50)),
                ('ans_3', models.CharField(max_length=50)),
                ('ans_4', models.CharField(max_length=50)),
                ('ans_5', models.CharField(max_length=50)),
                ('ans_6', models.CharField(max_length=50)),
                ('ans_7', models.CharField(max_length=50)),
                ('ans_8', models.CharField(max_length=50)),
                ('ans_9', models.CharField(max_length=50)),
                ('ans_10', models.CharField(max_length=50)),
                ('hint_1', models.CharField(max_length=50)),
                ('hint_2', models.CharField(max_length=50)),
                ('hint_3', models.CharField(max_length=50)),
                ('hint_4', models.CharField(max_length=50)),
                ('hint_5', models.CharField(max_length=50)),
                ('hint_6', models.CharField(max_length=50)),
                ('hint_7', models.CharField(max_length=50)),
                ('hint_8', models.CharField(max_length=50)),
                ('hint_9', models.CharField(max_length=50)),
                ('hint_10', models.CharField(max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
