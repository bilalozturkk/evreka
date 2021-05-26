import json

from django.http import HttpResponse
from django.utils import timezone

from .models import Vehicle

def get_last_points_per_vehicle(request):
    last_points_per_vehicle_list = []

    query_time = timezone.now()
    for vehicle in Vehicle.objects.all():
        if vehicle.has_recent_navigation_record(query_time):
            most_recent_navigation_record = vehicle.most_recent_navigation_record(query_time)
            
            last_points_per_vehicle_list.append({
                'latitude': most_recent_navigation_record.latitude,
                'longitude': most_recent_navigation_record.longitude,
                'vehicle_plate': most_recent_navigation_record.vehicle.plate,
                'datetime': most_recent_navigation_record.datetime.strftime('%Y-%m-%d %H:%M')
            })
    
    result = {}
    result['last_points'] = last_points_per_vehicle_list
    result = json.dumps(result)
    
    return HttpResponse(result, content_type="text/json-comment-filtered")
