# Generated by Django 3.1.2 on 2020-10-18 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system_builder', '0002_auto_20201017_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('system_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='system_builder.systemtype')),
            ],
        ),
        migrations.AddField(
            model_name='filter',
            name='system',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='system_builder.system'),
            preserve_default=False,
        ),
    ]
