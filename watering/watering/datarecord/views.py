from django.shortcuts import render
from django.views.generic import View
from monitor.models import Monitor_2 as Monitor
from django.db.models import Q
from django.http import HttpResponse

# Create your views here.

class Datarecord(View):

    def get(self,request):
        time_info = request.GET.get("time_info")
        list_1 = Monitor.objects.filter(month=int(time_info))
        data_list = []
        day = [i.day for i in list_1]
        day = set(day)
        day_data_list = []
        href = ["One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve"]
        for index,j in enumerate(day):
            day_list = Monitor.objects.filter(Q(month=int(time_info))&Q(day=j))
            day_data_list = []
            for i in day_list:
                time = str(i.day)+"/"+str(i.hour)+":"+str(i.minute)
                humidity = i.humidity
                temperature = i.temperature
                day_data_list.append({"time":time,"humidity":humidity,"temperature":temperature})
            data_list.append({"day":j,"href":"#collapse"+str(href[index]),"id":"collapse"+str(href[index]),"list":day_data_list})
        context = {
                "month":time_info,
                "data_list":data_list,
        }
        return render(request,'html/table.html',context)




