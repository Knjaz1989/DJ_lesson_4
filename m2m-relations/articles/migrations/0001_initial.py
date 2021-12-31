# Generated by Django 4.0 on 2021-12-30 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Текст')),
                ('published_at', models.DateTimeField(verbose_name='Дата публикации')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='ArticleScope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
            ],
        ),
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Тэг')),
                ('articles', models.ManyToManyField(related_name='scopes', through='articles.ArticleScope', to='articles.Article', verbose_name='Статьи')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
            },
        ),
        migrations.AddField(
            model_name='articlescope',
            name='scopes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.scope'),
        ),
    ]