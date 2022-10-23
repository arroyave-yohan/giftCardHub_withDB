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
            'balance': request.data.get('balance'), 
        }
        serializer = giftCardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GiftCardDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, giftCard_id):
        try:
            selectedGiftCard = giftCard.objects.get(id = giftCard_id)
            serializer = giftCardSerializer(selectedGiftCard, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(
                {"Requested GiftCard doesn't exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
