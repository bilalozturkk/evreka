import json

from django.http import HttpResponse

from .models import Frequencies

def get_collection_frequency_list(request):
    result = {}

    frequency_list = []
    for frequency in Frequencies.objects.all():
        frequency_list.append({
            'bin': str(frequency.bin),
            'operation': str(frequency.operation),
            'freuency': frequency.collection_frequency,
            'last_collection': frequency.last_collection.strftime("%Y-%m-%d %H:%M")
        })
    
    result['collection_frequency'] = frequency_list
    result = json.dumps(result)

    return HttpResponse(result, content_type="text/json-comment-filtered")
