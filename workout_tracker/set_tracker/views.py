from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from set_tracker.models import SetTracker
from set_tracker.serializer import SetTrackerSerializer
# Create your views here.

@csrf_exempt
def tracker_list(request):
    if request.method == 'GET':
        tracker = SetTracker.objects.all()
        serializer = SetTrackerSerializer(tracker, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SetTrackerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.error_messages, status=400)
    

@csrf_exempt
def tracker_details(request, pk):
    try:
        track = SetTracker.objects.get(pk=pk)
    except track.DoesNotExist:
        return HttpResponse(status=400)
    
    if request.method == 'GET':
        serializer = SetTrackerSerializer(track)
        return JsonResponse(serializer.data, status=200)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SetTrackerSerializer(track, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.error_messages, safe=400)
    
    elif request.method == 'DELETE':
        track.delete()
        return HttpResponse(status=204)
    