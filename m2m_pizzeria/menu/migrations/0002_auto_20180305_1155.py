# Generated by Django 2.0.2 on 2018-03-05 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToppingOnPizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='toppings',
        ),
        migrations.AddField(
            model_name='toppingonpizza',
            name='pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Pizza'),
        ),
        migrations.AddField(
            model_name='toppingonpizza',
            name='topping',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Topping'),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings_through',
            field=models.ManyToManyField(through='menu.ToppingOnPizza', to='menu.Topping'),
        ),
    ]