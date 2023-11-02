from django.http import HttpResponse, JsonResponse
from django.utils import timezone

from api import functions
from api.models import DifferenceRequest


def difference(request):
    """Returns the difference between:
    1. The sum of the squares of the first n natural numbers
    2. The square of the sum of the same first n natural numbers"""
    try:
        number = int(request.GET.get("number"))
    except ValueError:
        return HttpResponse(status=400)

    if last_request := DifferenceRequest.objects.first():
        difference = last_request.difference
        last_datetime = last_request.created_at
    else:
        sum_of_squares = functions.sum_of_squares(number)
        square_of_sums = functions.square_of_sums(number)
        difference = abs(sum_of_squares - square_of_sums)
        last_datetime = None

    DifferenceRequest.objects.create(number=number, difference=difference)

    return JsonResponse({
        "datetime": timezone.now(),
        "difference": difference,
        "number": number,
        "occurrences": DifferenceRequest.objects.count(),
        "last_datetime": last_datetime
    })
