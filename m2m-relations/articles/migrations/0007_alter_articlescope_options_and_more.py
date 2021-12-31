# Generated by Django 4.0 on 2021-12-31 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_articlescope_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlescope',
            options={'ordering': ['-is_main']},
        ),
        migrations.RenameField(
            model_name='articlescope',
            old_name='primary',
            new_name='is_main',
        ),
        migrations.AlterField(
            model_name='articlescope',
            name='articles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article'),
        ),
        migrations.AlterField(
            model_name='articlescope',
            name='scopes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.scope'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='articles',
            field=models.ManyToManyField(through='articles.ArticleScope', to='articles.Article', verbose_name='Статьи'),
        ),
    ]
