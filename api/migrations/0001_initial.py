# Generated by Django 2.1.7 on 2019-04-30 11:23

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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner'), ('BL', 'Brunch'), ('DT', 'Dessert')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Sa', 'Saturday'), ('Su', 'Sunday'), ('Mo', 'Monday'), ('Tu', 'Tuesday'), ('We', 'Wednesday'), ('Th', 'Thursday'), ('Fr', 'Friday')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=5)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='api.Category')),
            ],
        ),
        migrations.CreateModel(
            name='OperatingTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('day', models.ManyToManyField(to='api.Day')),
            ],
        ),
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('guests', models.IntegerField()),
            ],
            options={
                'ordering': ['-position'],
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant', models.CharField(choices=[('Japanese', 'Japanese'), ('Italian', 'Italian'), ('Mexican', 'Mexican')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='restaurant',
            name='foodtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foodtype', to='api.RestaurantType'),
        ),
        migrations.AddField(
            model_name='queue',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='queue', to='api.Restaurant'),
        ),
        migrations.AddField(
            model_name='queue',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='operatingtime',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operatingtime', to='api.Restaurant'),
        ),
        migrations.AddField(
            model_name='category',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='api.Restaurant'),
        ),
        migrations.AlterUniqueTogether(
            name='queue',
            unique_together={('position', 'restaurant'), ('restaurant', 'user')},
        ),
    ]