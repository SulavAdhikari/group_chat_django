from channels.middleware import BaseMiddleware
from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser
from rest_framework.authtoken.models import Token

@database_sync_to_async
def get_user(scope):
    try:
        token_key = scope["query_string"].decode("utf-8").split("=")[1]
        return Token.objects.get(key=token_key).user
    except (Token.DoesNotExist, IndexError):
        return AnonymousUser()

class TokenAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        scope["user"] = await get_user(scope)
        return await super().__call__(scope, receive, send)
