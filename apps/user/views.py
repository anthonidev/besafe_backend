from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status, generics, permissions


class GoogleLoginView(SocialLoginView):
    authentication_classes = []
    adapter_class = GoogleOAuth2Adapter
    callback_url = f'{settings.FRONTEND_URL}/api/auth/callback/google'
    client_class = OAuth2Client


class TestApiView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = self.request.user
        print(user)

        return Response({'message': 'Hello, World!'}, status=status.HTTP_200_OK)
