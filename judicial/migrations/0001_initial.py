# Generated by Django 3.2.9 on 2021-11-15 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PartiesInvolved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PartiesInvolvedProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parties_involved', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judicial.partiesinvolved')),
            ],
            options={
                'verbose_name_plural': 'Processes and Parties Involved',
            },
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process_number', models.IntegerField()),
                ('process_class', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('judge', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parties_involved', models.ManyToManyField(blank=True, related_name='parties_involved', through='judicial.PartiesInvolvedProcess', to='judicial.PartiesInvolved')),
            ],
        ),
        migrations.AddField(
            model_name='partiesinvolvedprocess',
            name='process',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judicial.process'),
        ),
    ]
