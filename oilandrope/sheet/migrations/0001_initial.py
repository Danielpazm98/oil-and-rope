# Generated by Django 2.2.2 on 2019-12-26 12:38

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
            name='CharacterInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Height')),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Weight')),
                ('hair_color', models.CharField(blank=True, max_length=30, null=True, verbose_name='Hair Color')),
                ('eye_color', models.CharField(blank=True, max_length=30, null=True, verbose_name='Eye Color')),
                ('height_measurement_system', models.PositiveSmallIntegerField(choices=[(0, 'Metric'), (1, 'US Standard')], default=0, verbose_name='Height Measurement System')),
                ('WEIGHT_MEASUREMENT_SYSTEM', models.PositiveSmallIntegerField(choices=[(0, 'Metric'), (1, 'US Standard')], default=0, verbose_name='Weight Measurement System')),
            ],
            options={
                'verbose_name': 'CharacterInfo',
                'verbose_name_plural': 'Charac terInfos',
            },
        ),
        migrations.CreateModel(
            name='SheetHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('character_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sheet.CharacterInfo', verbose_name='Character Info')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'sheetheader',
                'verbose_name_plural': 'sheetheaders',
            },
        ),
        migrations.CreateModel(
            name='SheetDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('start_value', models.SmallIntegerField(verbose_name='Start Value')),
                ('rollable', models.BooleanField(default=True, verbose_name='Rollable')),
                ('dice_class', models.PositiveSmallIntegerField(default=20, verbose_name='Dice Class')),
                ('dice_number', models.PositiveSmallIntegerField(default=1, verbose_name='Dice Number')),
                ('misc_bonus', models.SmallIntegerField(default=0, verbose_name='Miscelaneous Bonus')),
                ('extra_bonus_1', models.SmallIntegerField(default=0, verbose_name='Miscelaneous Bonus')),
                ('extra_bonus_2', models.SmallIntegerField(default=0, verbose_name='Miscelaneous Bonus')),
                ('sheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sheet_details', to='sheet.SheetHeader', verbose_name='Sheet Header')),
            ],
            options={
                'verbose_name': 'sheetdetail',
                'verbose_name_plural': 'sheetdetails',
            },
        ),
    ]
