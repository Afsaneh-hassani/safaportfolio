from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import ContactForm
from .models import Contact

def index_view(request):
    return render(request,'website/index.html')


# Create your views here


@require_POST
def contact_view(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'status': 'success', 'message': 'پیام شما با موفقیت ارسال شد!'})
    return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)


def index(request):
    return render(request, 'website/index.html') 


def certificate(request):
    return render(request, 'website/certificate.html')


def projects(request):
    return render(request, 'website/projects.html')

def appreciation(request):
    return render(request, 'website/appreciation.html')