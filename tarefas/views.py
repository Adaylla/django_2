from django.shortcuts import render

# Create your views here.
def index(request):
    print("conseguir chegar na view")
    return render(request, "index.html")