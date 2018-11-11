from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect

from .forms import UploadImageForm

from django.core.files.storage import FileSystemStorage

from django.conf import settings

from .models import ImageUploadModel

def first_view(request):

    return render(request, 'opencv_app/first_view.html', {})

def uimage(request):

    if request.method == 'POST':

        form = UploadImageForm(request.POST, request.FILES)

        if form.is_valid():

            myfile = request.FILES['image']

            fs = FileSystemStorage()

            filename = fs.save(myfile.name, myfile)

            uploaded_file_url = fs.url(filename)

            return render(request, 'opencv_app/uimage.html', {'form': form, 'uploaded_file_url': uploaded_file_url})

    else:

        form = UploadImageForm()

        return render(request, 'opencv_app/uimage.html', {'form': form})
