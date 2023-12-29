# Generated by Django 3.1.5 on 2021-02-24 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speechtext_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('age', models.IntegerField()),
                ('phone', models.BigIntegerField()),
                ('message', models.TextField(max_length=1000)),
                ('experiences', models.CharField(choices=[('E', 'Excellent'), ('G', 'Good'), ('B', 'Bad')], max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Registration',
        ),
    ]