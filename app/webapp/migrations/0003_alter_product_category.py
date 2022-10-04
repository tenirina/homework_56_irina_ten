# Generated by Django 4.1.1 on 2022-10-04 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_product_category_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('other', 'Other'), ('fruits', 'Fruits'), ('vegetables', 'Vegetables'), ('prepared', 'Prepared food')], max_length=100, verbose_name='Category'),
        ),
    ]
