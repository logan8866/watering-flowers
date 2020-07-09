from django.shortcuts import render
from django.views.generic import View
from monitor.models import Monitor_3 
from django.db.models import Q
from django.http import HttpResponse

# Create your views here.

class Monitor(View):

    def get(self,request):
        data = Monitor_3.objects.last()
        hour = data.hour
        minute = data.minute
        second = data.second
        temperature = data.temperature
        humidity = data.humidity
        standard_temperature = 40
        standard_humidity = 40
        temperature_percent = temperature/standard_temperature*100
        humidity_percent = humidity/standard_humidity*100
        data_10 = Monitor_3.objects.all()[:10]
        all_humidity = [str(i.humidity) for i in data_10]
        all_temperature = [str(i.temperature) for i in data_10]
        humidity_data = ','.join(all_humidity)
        temperature_data = ','.join(all_temperature)
        context = {
                "hour":hour,
                "minute":minute,
                "second":second,
                "temperature":temperature,
                "humidity":humidity,
                "temperature_percent":temperature_percent,
                "humidity_percent":humidity_percent,
                "humidity_data":humidity_data,
                "temperature_data":temperature_data,
        }
        return render(request,'html/index.html',context)

        

