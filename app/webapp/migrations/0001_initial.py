# Generated by Django 4.1.1 on 2022-10-03 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(max_length=2000, null=True, verbose_name='Description')),
                ('photo', models.CharField(max_length=200, verbose_name='Photo')),
                ('category', models.CharField(choices=[('other', 'Other'), ('book', 'Book')], max_length=100, verbose_name='Title')),
                ('balance', models.IntegerField(verbose_name='Balance')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date of create')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Date of create')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Delete')),
                ('deleted_at', models.DateTimeField(default=None, null=True, verbose_name='Date of delete')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
