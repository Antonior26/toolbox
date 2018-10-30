import time

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View

from .forms import PhotoForm
from .models import Photo
from django.core.urlresolvers import reverse, reverse_lazy
import string
import random
from django.views.generic import RedirectView


class AboutView(RedirectView):
    #template_name = 'home/about.html'
    url = reverse_lazy('photos:progress_bar_upload')


def generate_uniq_id(size=15, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

from django.shortcuts import redirect

def give_ID(request):
    request_path = str(request.path_info)

    random_ID = generate_uniq_id()
    response = redirect(reverse_lazy("lolo"))
    # response = redirect(request_path+"/"+random_ID)
    #response = redirect('/photos/'+random_ID)

    return response


class ProgressBarUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'photos/progress_bar_upload/index.html', {'photos': photos_list})

    def post(self, request):
        time.sleep(1)  # You don't need this line. This is just to delay the process so you can see the progress bar testing locally.
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


class DragAndDropUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'photos/drag_and_drop_upload/index.html', {'photos': photos_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


def clear_database(request):
    for photo in Photo.objects.all():
        photo.file.delete()
        photo.delete()
    return redirect(request.POST.get('next'))