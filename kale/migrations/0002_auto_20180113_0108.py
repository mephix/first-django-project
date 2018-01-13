# Generated by Django 2.0.1 on 2018-01-13 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kale', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Yoga', 'Yoga'), ('Rockclimbing', 'Rockclimbing'), ('Tango', 'Tango'), ('Freediving', 'Freediving')], default='Yoga', max_length=200, verbose_name='type of event')),
                ('startDateTime', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=11)),
                ('min_people', models.PositiveIntegerField()),
                ('max_people', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.PositiveIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kale.Person'),
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kale.Venue'),
        ),
    ]