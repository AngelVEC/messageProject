# Generated by Django 5.0.6 on 2024-07-01 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_rename_created_at_chatroom_created_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='ChatRoom',
            new_name='chat_room',
        ),
    ]