# Generated by Django 2.2.6 on 2020-04-14 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0002_auto_20200414_0418'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill',
            old_name='boolean_due_date',
            new_name='bill_due_date',
        ),
        migrations.RenameField(
            model_name='bill',
            old_name='boolean_generated',
            new_name='bill_generated',
        ),
        migrations.RenameField(
            model_name='bill',
            old_name='boolean_invoiced',
            new_name='bill_invoiced',
        ),
        migrations.RenameField(
            model_name='bill',
            old_name='boolean_paid',
            new_name='bill_paid',
        ),
    ]
