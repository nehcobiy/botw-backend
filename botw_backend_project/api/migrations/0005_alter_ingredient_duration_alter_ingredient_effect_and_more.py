# Generated by Django 4.2.2 on 2023-06-27 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_ingredient_unique_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='duration',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='effect',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='hearts',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='image',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='type',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='duration',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredient2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='i2', to='api.ingredient'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredient3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='i3', to='api.ingredient'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredient4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='i4', to='api.ingredient'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredient5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='i5', to='api.ingredient'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='notes',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='strength',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='type_image',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]