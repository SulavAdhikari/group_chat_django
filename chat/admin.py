from django.contrib import admin

# Register your models here.
from chat.models import ChatGroup, Message, GroupMembership

admin.site.register(ChatGroup)
admin.site.register(Message)
admin.site.register(GroupMembership)
