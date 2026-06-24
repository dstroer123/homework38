from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DocumentForm
from .models import Document


@login_required
def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form = DocumentForm()

    files = Document.objects.all()

    return render(
        request,
        'upload.html',
        {
            'form': form,
            'files': files
        }
    )