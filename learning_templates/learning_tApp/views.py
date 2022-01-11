from django.shortcuts import render


# Create your views here.

def index(request):
    contex_dict = {'text': 'hello world', 'number': 100}
    return render(request, 'index.html', contex_dict)


def other(request):
    return render(request, 'other.html')


def relative(request):
    return render(request, 'relative_url_templates.html')
