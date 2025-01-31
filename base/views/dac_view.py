from django.shortcuts import render

def dac_view(request):
    return render(
        request,
        'base/dac.html',
    )