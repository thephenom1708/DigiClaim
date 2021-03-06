# Generated by Django 2.1.7 on 2019-04-11 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('claim_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('user_id', models.CharField(default='', max_length=100)),
                ('model_name', models.CharField(max_length=100)),
                ('brand', models.CharField(default='', max_length=100)),
                ('device_image', models.FileField(default='', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessedClaim',
            fields=[
                ('claim_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('initial_image', models.FileField(default='', upload_to='')),
                ('image_l1', models.FileField(default='', upload_to='')),
                ('image_l2', models.FileField(default='', upload_to='')),
                ('scratch_flag', models.BooleanField(default=False)),
            ],
        ),
    ]
