from django.shortcuts import render

def drc_view(request):

    return render(
        request,
        'base/drc.html',
    )