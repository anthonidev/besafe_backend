from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, viewsets, generics
from rest_framework.response import Response

from .models import HomeGroup, Floor
from .serializers import HomeGroupSerializer

from apps.identify.models import Account
import cloudinary


class HomeView(viewsets.ModelViewSet):
    queryset = HomeGroup.objects.all()
    serializer_class = HomeGroupSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        user = self.request.user
        account = get_object_or_404(Account, user=user)

        if HomeGroup.objects.filter(members=account).exists():
            home = HomeGroup.objects.get(members=account)
            serializer = self.get_serializer(home)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No existe un grupo'}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        user = self.request.user
        data = request.data
        account = Account.objects.get(user=user)
        if HomeGroup.objects.filter(members=account).exists():
            return Response({'message': 'Ya perteneces a un grupo'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                serializer = self.get_serializer(data=data)
                serializer.is_valid(raise_exception=True)
                serializer.save().members.add(account)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            except Exception as e:
                print(e)
                return Response({'message': 'Ha ocurrido un error  intentalo mas tarde'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        user = self.request.user
        data = request.data
        account = get_object_or_404(Account, user=user)
        HomeGroup.objects.filter(members=account).update(**data)

        serializer = self.get_serializer(
            get_object_or_404(HomeGroup, members=account))
        return Response(serializer.data, status=status.HTTP_200_OK)


class FloorView(generics.GenericAPIView):
    queryset = HomeGroup.objects.all()
    serializer_class = HomeGroupSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self,  request, id, *args, **kwargs):
        user = self.request.user
        account = get_object_or_404(Account, user=user)

        data = request.data
        home = get_object_or_404(HomeGroup, id=id)
        try:
            picture = cloudinary.uploader.upload(
                data['picture']).get('public_id')
            Floor.objects.create(
                home_group=home,
                picture=picture,
                number=int(data['number']),
                safe_zone=data['safe_zone']
            )
            serializer = self.get_serializer(
                get_object_or_404(HomeGroup, members=account))
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'message': 'Ha ocurrido un error  intentalo mas tarde'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, *args, **kwargs):
        user = self.request.user
        account = get_object_or_404(Account, user=user)

        data = request.data
        floor = get_object_or_404(Floor, id=id)
        try:
            if data['picture'] != "undefined":
                image = cloudinary.uploader.upload(
                    data['picture']).get('public_id')
            else:
                image = floor.picture
            Floor.objects.filter(id=id).update(
                picture=image,
                number=int(data['number']),
                safe_zone=data['safe_zone']
            )

            serializer = self.get_serializer(
                get_object_or_404(HomeGroup, members=account)
            )
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'message': 'Ha ocurrido un error  intentalo mas tarde'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, *args, **kwargs):
        user = self.request.user
        account = get_object_or_404(Account, user=user)

        floor = get_object_or_404(Floor, id=id)
        try:
            floor.delete()
            serializer = self.get_serializer(
                get_object_or_404(HomeGroup, members=account)
            )
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'message': 'Ha ocurrido un error  intentalo mas tarde'}, status=status.HTTP_400_BAD_REQUEST)


class GuestView(generics.GenericAPIView):
    queryset = HomeGroup.objects.all()
    serializer_class = HomeGroupSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        data = request.data
        account = get_object_or_404(Account, user=user)

        home = get_object_or_404(HomeGroup, family_code=data['family_code'])

        if HomeGroup.objects.filter(members=account).exists():
            return Response({'message': 'Ya perteneces a un grupo'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                home.members.add(account)
                serializer = self.get_serializer(home)
                return Response(serializer.data, status=status.HTTP_200_OK)

            except Exception as e:
                print(e)
                return Response({'message': 'Ha ocurrido un error  intentalo mas tarde'}, status=status.HTTP_400_BAD_REQUEST)
