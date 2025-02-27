# Generated by Django 4.2 on 2025-02-27 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='tags',
        ),
        migrations.AddField(
            model_name='tag',
            name='tags',
            field=models.ManyToManyField(blank=True, to='livros.tag'),
        ),
        migrations.AlterField(
            model_name='book',
            name='available_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='BookCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='codes', to='livros.book')),
            ],
        ),
    ]
