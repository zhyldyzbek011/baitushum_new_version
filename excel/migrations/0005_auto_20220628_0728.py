# Generated by Django 3.2.7 on 2022-06-28 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('excel', '0004_auto_20220628_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='month',
            name='branch',
            field=models.CharField(choices=[('1_ГО', '1_ГО'), ('2_ОФ', '2_ОФ'), ('3_ЖАФ', '3_ЖАФ'), ('4_БФ', '4_БФ'), ('5_ТФ', '5_ТФ'), ('6_НФ', '6_НФ'), ('7_КФ', '7_КФ'), ('8_БатФ', '8_БатФ')], max_length=300, verbose_name='Филиал'),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='month',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='date', to='excel.date'),
        ),
    ]
