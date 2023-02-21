from django.shortcuts import render
from django.http import HttpResponse

user_list = []

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        temp = {'user': username, 'pwd': password}
        user_list.append(temp)

    return render(request, 'index.html', {'data': user_list})
    # return HttpResponse('TEST TEST TEST')

# Create your views here.
