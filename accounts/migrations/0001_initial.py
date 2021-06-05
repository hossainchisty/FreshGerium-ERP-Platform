# Generated by Django 3.2.3 on 2021-05-30 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(help_text='Name of Account', max_length=25)),
                ('account_description', models.TextField()),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('account_phone', models.IntegerField()),
                ('billing_address', models.TextField()),
                ('organization_industry', models.CharField(choices=[('FINANCE', 'FINANCE'), ('HEALTHCARE', 'HEALTHCARE'), ('INSURANCE', 'INSURANCE'), ('LEGAL', 'LEGAL'), ('MANUFACTURING', 'MANUFACTURING'), ('PUBLISHING', 'PUBLISHING'), ('REAL ESTATE', 'REAL ESTATE'), ('SOFTWARE', 'SOFTWARE')], help_text='Enter Organization Industry Type: ', max_length=255)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
