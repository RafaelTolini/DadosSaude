from django.shortcuts import render

def neo_view(request):
    return render(
        request,
        'base/neo.html',
    )