# Generated by Django 3.2.9 on 2022-01-07 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('instock', models.BooleanField(default=True)),
                ('offer_badge', models.BooleanField(default=False)),
                ('popular_items', models.BooleanField(default=False)),
                ('new_arrivals', models.BooleanField(default=False)),
                ('width_field', models.IntegerField(default=400)),
                ('height_field', models.IntegerField(default=400)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='images/', width_field='width_field')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]
