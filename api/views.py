from django.http import HttpResponse, JsonResponse
from django.utils import timezone

from api import functions


def difference(request):
    """Returns the difference between:
    1. The sum of the squares of the first n natural numbers
    2. The square of the sum of the same first n natural numbers"""

    try:
        number = int(request.GET.get("number"))
    except ValueError:
        return HttpResponse(status=400)

    sum_of_squares = functions.sum_of_squares(number)
    square_of_sums = functions.square_of_sums(number)
    difference = abs(sum_of_squares - square_of_sums)

    return JsonResponse(
        {"datetime": timezone.now(), "difference": difference, "number": number}
    )
