# Generated by Django 3.2.9 on 2021-11-17 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TiF', '0002_auto_20211117_2027'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subcategory',
            new_name='Foundation',
        ),
        migrations.CreateModel(
            name='TextDep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('found_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='textdep', to='TiF.foundation')),
                ('text_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='textdep', to='TiF.text')),
            ],
        ),
    ]
