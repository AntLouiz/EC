# Generated by Django 2.0 on 2017-12-29 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecweb', '0003_auto_20171227_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='turn',
            field=models.CharField(choices=[('morning', 'Morning'), ('afternoon', 'Afternoon')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]
