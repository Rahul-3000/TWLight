# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-30 17:57


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("resources", "0068_auto_20190523_1250")]

    operations = [
        migrations.AddField(
            model_name="partner",
            name="description_uk",
            field=models.TextField(
                blank=True,
                help_text="Optional detailed description in addition to the short description such as collections, instructions, notes, special requirements, alternate access options, unique features, citations notes.",
                null=True,
                verbose_name=b"long description",
            ),
        ),
        migrations.AddField(
            model_name="partner",
            name="send_instructions_uk",
            field=models.TextField(
                blank=True,
                help_text="Optional instructions for sending application data to this partner.",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="partner",
            name="short_description_uk",
            field=models.TextField(
                blank=True,
                help_text="Optional short description of this partner's resources.",
                max_length=1000,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="stream",
            name="description_uk",
            field=models.TextField(
                blank=True,
                help_text="Optional description of this stream's resources.",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="textfieldtag",
            name="name_uk",
            field=models.TextField(max_length=100, null=True, verbose_name="Name"),
        ),
    ]
