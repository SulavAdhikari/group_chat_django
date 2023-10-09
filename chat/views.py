

# Create your views here.
# views.py
from rest_framework import viewsets
from .models import ChatGroup, Message, GroupMembership
from .serializers import GroupSerializer, MessageSerializer, GroupMembershipSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = ChatGroup.objects.all()
    serializer_class = GroupSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class GroupMembershipViewSet(viewsets.ModelViewSet):
    queryset = GroupMembership.objects.all()
    serializer_class = GroupMembershipSerializer
