# Generated by Django 4.2.7 on 2023-11-02 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PythagoreanTripletRequest',
            fields=[
                ('apirequest_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.apirequest')),
                ('a', models.IntegerField()),
                ('b', models.IntegerField()),
                ('c', models.IntegerField()),
                ('is_triplet', models.BooleanField(default=False)),
                ('product', models.IntegerField()),
            ],
            bases=('api.apirequest',),
        ),
    ]