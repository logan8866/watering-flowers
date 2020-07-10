from django.shortcuts import render
from django.views.generic import View
from monitor.models import Monitor_3 
from django.db.models import Q
from django.http import HttpResponse
from django.http import JsonResponse

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

    def post(self,request):
        data = Monitor_3.objects.last()
        year = str(data.year)
        month = str(data.month)
        day = str(data.day)
        hour = str(data.hour)
        minute = str(data.minute)
        second = str(data.second)
        temperature = data.temperature
        humidity = data.humidity
        if temperature<20 and humidity<20:
            alert = "很好！你的植物不需要浇水！"
            alert_css = "alert alert-success"
        else:
            alert = "注意！！！你的植物需要浇水了！！！"
            alert_css = "alert alert-danger"
        standard_temperature = 40
        standard_humidity = 40
        temperature_percent = str(temperature/standard_temperature*100)
        humidity_percent = str(humidity/standard_humidity*100)
        if len(Monitor_3.objects.all())>10:
            data_10 = list(reversed(list(reversed(Monitor_3.objects.all()))[:10]))
        else:
            data_10 = Monitor_3.objects.all()
        all_humidity = [str(i.humidity) for i in data_10]
        all_temperature = [str(i.temperature) for i in data_10]
        humidity_data = ','.join(all_humidity)
        temperature_data = ','.join(all_temperature)
        context = {
                "year":year,
                "month":month,
                "day":day,
                "hour":hour,
                "minute":minute,
                "second":second,
                "temperature":temperature,
                "humidity":humidity,
                "temperature_percent":temperature_percent,
                "humidity_percent":humidity_percent,
                "humidity_data":humidity_data,
                "temperature_data":temperature_data,
                "alert":alert,
                "alert_css":alert_css,
        }
        return JsonResponse(context)


        

