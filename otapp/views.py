from django.shortcuts import render

from .bookmyOT.dashboard import dashboard
from otapp.bookmyOT.doctors import get_All_Doctors_List


# Create your views here.

def home(request):
    data = dashboard()
    return render(request, 'bookmy _ot.html', data)

def physician_list(request):

    physicians_data = get_All_Doctors_List()
    print(physicians_data)
    context = {
        'physicians_data': physicians_data,
    }
    return render(request, 'getphysician.html', context)