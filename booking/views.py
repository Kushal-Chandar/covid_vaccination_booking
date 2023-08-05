from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import VaccinationCenter, Slot
from datetime import datetime

# Create your views here.
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print('Valid')
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = UserCreationForm()

    return render(request, 'user_signup.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')  # Redirect to the desired page after login
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'user_login.html', {'form': form})


def home(request):
    query = request.GET.get('q', '')
    start_time = request.GET.get('start_time', '')
    end_time = request.GET.get('end_time', '')

    centers = VaccinationCenter.objects.all()

    if query:
        centers = centers.filter(name__icontains=query)

    if start_time and end_time:
        try:
            start_time_obj = datetime.strptime(start_time, '%H:%M').time()
            end_time_obj = datetime.strptime(end_time, '%H:%M').time()
            centers = centers.filter(working_hours_start__lte=start_time_obj, working_hours_end__gte=end_time_obj)
        except ValueError:
            messages.error(request, 'Invalid time format. Please use HH:MM format.')

    return render(request, 'home.html', {'centers': centers})

@login_required(login_url='user_login')
def confirm_slot_booking(request, center_id):
    center = get_object_or_404(VaccinationCenter, id=center_id)
    return render(request, 'confirm_slot_booking.html', {'center': center})

@login_required(login_url='user_login')
def book_slot(request, center_id):
    center = get_object_or_404(VaccinationCenter, id=center_id)
    if center.slots > 0:
        # Decrement available slots and save the center
        center.slots -= 1
        center.save()

        # Create a new Slot instance and save it
        slot = Slot(user=request.user, center=center)
        slot.save()

    return redirect('home')




