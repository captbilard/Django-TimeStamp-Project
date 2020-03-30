import datetime
import time
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request, "timestamp/index.html")
#Endpoint when a date is given in utc format
def TimeStampApi(request, date_string):
    return_value=None
    unix_date_format=None
    #check if the date is valid
    try:
        d = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        return_value = {"error" : "Invalid Date" }
        return JsonResponse(return_value)
    #assign each date it's own format
    unix_date_format = datetime.datetime.strptime(date_string, "%Y-%m-%d").timestamp()
    UTC_String_format = datetime.datetime.strftime(d, "%a %d %b %Y %H %M %S")
    return_value = {"unix":unix_date_format, "utc":UTC_String_format}
    return JsonResponse(return_value)
#empty date endpoint
def EmptyDateTimeStampApi(request):
    today_date = datetime.datetime.today().strftime("%a %d %b %Y %H %M %S")
    unix_date_format = datetime.datetime.today().timestamp()
    return_value = {"unix":unix_date_format, "utc":today_date}
    return JsonResponse(return_value)



