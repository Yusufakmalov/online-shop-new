# Generated by Django 5.2.1 on 2025-05-22 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='product',
            name='shop_produc_created_ef211c_idx',
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('DF', 'Draft'), ('AV', 'Available')], default='DF', max_length=2),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['-available'], name='shop_produc_availab_347802_idx'),
        ),
    ]
