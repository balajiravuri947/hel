from django.shortcuts import render
app_name='ravuri'
# Create your views here.
def app1(request):
    return render(request,'app1.html')