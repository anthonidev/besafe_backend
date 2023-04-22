from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from apps.identify.models import Account
from apps.identify.serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        user = self.request.user
        if Account.objects.filter(user=user).exists():
            account = Account.objects.get(user=user)
            serializer = self.get_serializer(account)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No existe una cuenta'}, status=status.HTTP_400_BAD_REQUEST)
