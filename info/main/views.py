from django.shortcuts import render


def info_main(request):
    return render(request, 'main/info_main.html')


