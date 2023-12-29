# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from rest_framework.decorators import api_view
# from rest_framework import status
from rest_framework import permissions
from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from set_tracker.models import SetTracker
from set_tracker.serializer import SetTrackerSerializer, UserSerializer
from set_tracker.permissions import IsOwnerOrReadOnly
from django.http import Http404
from django.contrib.auth.models import User

# Create your views here.

class TrackerList(generics.ListCreateAPIView):
    queryset = SetTracker.objects.all()
    serializer_class = SetTrackerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    '''Override the serializer create method to save the owner filed'''
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)
class TrackerDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = SetTracker.objects.all()
    serializer_class = SetTrackerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class TrackerList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = SetTracker.objects.all()
#     serializer_class = SetTrackerSerializer

#     def get(self, request):
#         return self.list(request)
    
#     def post(self, request):
#         return self.create(request)
    
# class TrackerDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = SetTracker.objects.all()
#     serializer_class =  SetTrackerSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# class TrackerList(APIView):
#     def get(self, request, format=None):
#         tracker = SetTracker.objects.all()
#         serializer =  SetTrackerSerializer(tracker, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request, format=None):
#         serializer = SetTrackerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
# class TrackerDetails(APIView):
#     def get_object(self, pk):
#         try:
#             return SetTracker.objects.get(pk=pk)
#         except SetTracker.DoesNotExist:
#             return Http404
            
#     def get(self, request, pk, format=None):
#         tracker = self.get_object(pk)
#         serializer = SetTrackerSerializer(tracker)
#         return Response(serializer.data, status=status.HTTP_200_OK)
        
#     def put(self, request, pk, format=None):
#         tracker =  self.get_object(pk=pk)
#         serializer = SetTrackerSerializer(tracker, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        
#     def delete(self, request, pk, format=None):
#         tracker =  self.get_object(pk=pk)
#         tracker.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        


# @api_view(['GET', 'POST'])
# def tracker_list(request, format=None):
#     if request.method == 'GET':
#         tracker = SetTracker.objects.all()
#         serializer = SetTrackerSerializer(tracker, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     elif request.method == 'POST':
#         serializer = SetTrackerSerializer(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET', 'PUT', 'DELETE'])
# def tracker_details(request, pk, format=None):
#     try:
#         track = SetTracker.objects.get(pk=pk)
#     except track.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = SetTrackerSerializer(track)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = SetTrackerSerializer(track, request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         track.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @csrf_exempt
# def tracker_list(request):
#     if request.method == 'GET':
#         tracker = SetTracker.objects.all()
#         serializer = SetTrackerSerializer(tracker, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SetTrackerSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.error_messages, status=400)
    

# @csrf_exempt
# def tracker_details(request, pk):
#     try:
#         track = SetTracker.objects.get(pk=pk)
#     except track.DoesNotExist:
#         return HttpResponse(status=400)
    
#     if request.method == 'GET':
#         serializer = SetTrackerSerializer(track)
#         return JsonResponse(serializer.data, status=200)
    
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SetTrackerSerializer(track, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.error_messages, safe=400)
    
#     elif request.method == 'DELETE':
#         track.delete()
#         return HttpResponse(status=204)
    