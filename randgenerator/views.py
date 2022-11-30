import random
from django.http import HttpResponse


def get_random(request):
    return HttpResponse(random.randint(1000, 9999))
