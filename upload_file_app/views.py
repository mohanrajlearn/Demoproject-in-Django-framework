import csv 
import os
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout  # Import the login function
from .forms import UploadedDataForm
from .models import UploadedData
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    return render(request, "index.html") 

@login_required
def welcome(request):
    file_uploaded = False

    if request.method == 'POST':
        form = UploadedDataForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the uploaded file with the associated user
            uploaded_data = form.save(commit=False)
            uploaded_data.user = request.user
            uploaded_data.save()
            file_uploaded = True
            messages.success(request, "File Uploaded Successfully")
            return redirect('welcome')  # Redirect to the welcome page or another view after successful upload
    else:
        form = UploadedDataForm()

    # Display existing uploaded files for the current user
    file_list = UploadedData.objects.filter(user=request.user)
    return render(request, 'welcome.html', {'form': form, 'file_list': file_list, 'file_uploaded': file_uploaded})

def handle_uploaded_file(file, user):
    
    uploaded_data = UploadedData.objects.create(user=user, file=file)
    uploaded_data.save()

def get_uploaded_files():
    upload_dir = os.path.join(settings.MEDIA_ROOT, '')

    # Check if the directory exists
    if os.path.exists(upload_dir):
        return os.listdir(upload_dir)
    else:
        return []
    
def download_file(request, file_id):
    file_entry = get_object_or_404(UploadedData, pk=file_id)
    response = HttpResponse(file_entry.file, content_type='application/csv')
    response['Content-Disposition'] = f'attachment; filename="{file_entry.file.name}"'
    return response

def delete_file(request, file_id):
    file_entry = get_object_or_404(UploadedData, pk=file_id)
    file_entry.delete()
    return redirect('welcome')  # Redirect to your desired view after deletion
    
def signup_view(request):
    error_message = ''
    username = ''
    email = ''
    password1 = ''
    password2 = ''

    if request.method == 'POST':
        # Use = instead of : for assignment
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            # Create user and log in
            user = User.objects.create_user(username=username, email=email, password=password1)
            login(request, user)
            return redirect('login')  # Change 'home' to the desired redirect URL
        else:
            # Passwords don't match, handle the error
            error_message = "Passwords do not match."
            return render(request, 'signup', {'error_message': error_message})

    return render(request, 'signup.html')

def login_view(request):
    error_message = ''

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log in the user
            login(request, user)
            return redirect('welcome')  # Redirect to the welcome page or another desired page
        else:
            # Invalid login credentials, handle the error
            error_message = "Invalid username or password."

    return render(request, 'login.html', {'error_message': error_message})

def logout_view(request):
    logout(request)
    return redirect('home')