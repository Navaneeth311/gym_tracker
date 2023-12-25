# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from set_tracker.models import SetTracker
from set_tracker.serializer import SetTrackerSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def tracker_list(request, format=None):
    if request.method == 'GET':
        tracker = SetTracker.objects.all()
        serializer = SetTrackerSerializer(tracker, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = SetTrackerSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def tracker_details(request, pk, format=None):
    try:
        track = SetTracker.objects.get(pk=pk)
    except track.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SetTrackerSerializer(track)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = SetTrackerSerializer(track, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        track.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
    