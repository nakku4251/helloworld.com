# Generated by Django 3.0 on 2021-02-05 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0003_category_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreatedAt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='作成日')),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='diaries.CreatedAt', verbose_name='作成日'),
        ),
    ]
