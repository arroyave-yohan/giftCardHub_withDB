from urllib import request
from wsgiref.util import request_uri
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import giftCard
from .serializers import giftCardSerializer

class giftCardListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Gift Card items for given requested user
        '''
        giftCards = giftCard.objects.all()
        serializer = giftCardSerializer(giftCards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Gift Card with given Gift Card data
        '''
        data = {
            'client': request.data.get('client'), 
            'provider': request.data.get('provider'),
            'balance': request.data.get('balance'),
            'redemptionToken': request.data('redemptionToken'),
            'redemptionCode': request.data('redemptionToken'),
            'emissionDate': request.data('emissionDate'),
            'expiringDate': request.data('expiringDate')

        }
        serializer = giftCardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GiftCardDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    #Get the Gift Card object to work with it
    def get_object(self, giftCard_id):
        '''
        Helper method to get the object with given a Gift Card id
        '''
        try:
            return giftCard.objects.get(id=giftCard_id)
        except giftCard.DoesNotExist:
            return None

    #Get Gift Card by id
    def get(self, request, giftCard_id, *args, **kwargs):
        '''
        Retrieves the Gift Card with given giftCard_id
        '''
        giftCard_instance = self.get_object(giftCard_id)
        if not giftCard_instance:
            return Response(
                {"res": "Object with Gift Card id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = giftCardSerializer(giftCard_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #Update Gift Card by id
    def put(self, request, giftCard_id, *args, **kwargs):
        '''
        Updates the Gift Card item with given giftCard_id if exists
        '''
        giftCard_instance = self.get_object(giftCard_id)
        if not giftCard_instance:
            return Response(
                {"res": "Object with Gift Card id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'client': request.data.get('client'), 
            'provider': request.data.get('provider'),
            'balance': request.data.get('balance'),
            'redemptionToken': request.data('redemptionToken'),
            'redemptionCode': request.data('redemptionToken'),
            'emissionDate': request.data('emissionDate'),
            'expiringDate': request.data('expiringDate')
        }
        serializer = giftCardSerializer(instance = giftCard_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Delete Gift Card by id
    def delete(self, request, giftCard_id, *args, **kwargs):
            '''
            Deletes the Gift Card item with given id if exists
            '''
            todo_instance = self.get_object(giftCard_id)
            if not todo_instance:
                return Response(
                    {"res": "Object with Gift Card id does not exists"}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            todo_instance.delete()
            return Response(
                {"res": "Object deleted!"},
                status=status.HTTP_200_OK
            )