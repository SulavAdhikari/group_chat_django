# consumers.py
async def connect(self):
    self.group_id = self.scope['url_route']['kwargs']['group_id']
    self.group = get_object_or_404(Group, pk=self.group_id)
    if self.scope["user"].is_authenticated and self.scope["user"] in self.group.members.all():
        await self.channel_layer.group_add(
            f"group_{self.group_id}",
            self.channel_name
        )
        await self.accept()
    else:
        await self.close()

async def disconnect(self, close_code):
    await self.channel_layer.group_discard(
        f"group_{self.group_id}",
        self.channel_name
    )

async def receive(self, text_data):
    text_data_json = json.loads(text_data)
    message = text_data_json['message']

    # Save the message to the database
    author = self.scope["user"]
    Message.objects.create(
        group=self.group,
        author=author,
        content=message
    )

    # Broadcast the message to all members of the group
    await self.channel_layer.group_send(
        f"group_{self.group_id}",
        {
            "type": "chat.message",
            "message": message,
            "author": author.username
        }
    )

async def chat_message(self, event):
    message = event['message']
    author = event['author']

    # Send the message to the WebSocket
    await self.send(text_data=json.dumps({
        'message': message,
        'author': author
    }))
