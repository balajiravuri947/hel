from django.shortcuts import render
app_name='balaji'
# Create your views here.
def app2(request):
    return render(request,'app2.html')