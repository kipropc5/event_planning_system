# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect
# from .models import Event , Participant
# from .forms import UserRegistrationForm
# from datetime import datetime
# from django.http import HttpResponse , JsonResponse
# from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
# from django.contrib import messages
# from .models import Event, Participant
# from .forms import EventForm, ParticipantForm  # Assuming you have forms for Event and Participant
#
#
#
# # Create your views here.
# def index(request):
#     return render(request,'index.html')
#
# @login_required
# def add_event(request):
#     if request.method == 'POST':
#         event_name = request.POST.get('e-name')
#         event_description = request.POST.get('e-description')
#         event_date = request.POST.get('e-date')
#         event_start_time = request.POST.get('e-time')
#         event_end_time = request.POST.get('e-end')
#         event_organizer = request.POST.get('e-organizer')
#         event_location = request.POST.get('e-location')
#         context={
#             "event_name":event_name,
#             "event_description":event_description,
#             "event_date":event_date,
#             "event_start_time":event_start_time,
#             "event_end_time":event_end_time,
#             "event_organizer":event_organizer,
#             "event_location":event_location,
#             "success":"Event added successfully"
#         }
#         query=Event(event_name=event_name,event_description=event_description,event_date=event_date,start_time=event_start_time,
#                     end_time=event_end_time,event_organizer=event_organizer,event_location=event_location)
#         query.save()
#         return render(request,'create_event.html',context)
#     return render(request,'create_event.html')
#
# @login_required
# def events(request):
#     all_events = Event.objects.all()
#     context = {'all_events':all_events}
#     return render(request,'event_list.html',context)
# @login_required
# def delete_event(request, event_id):
#     event = Event.objects.get(id=event_id)
#     event.delete()
#     messages.success(request, 'Event deleted successfully')
#     return redirect('all-events')
# @login_required
# def update_event(request, event_id):
#     event = Event.objects.get(id=event_id)
#     context = {'event':event}
#     if request.method == 'POST':
#         updated_name = request.POST.get('e-name')
#         updated_description = request.POST.get('e-description')
#         updated_start_time = request.POST.get('e-time')
#         updated_end_time = request.POST.get('e-end')
#         updated_organizer = request.POST.get('e-organizer')
#         updated_location = request.POST.get('e-location')
#         updated_date = request.POST.get('e-date')
#         event.name = updated_name
#         event.description = updated_description
#         event.start_time = updated_start_time
#         event.end_time = updated_end_time
#         event.organizer = updated_organizer
#         event.location = updated_location
#         event.date = updated_date
#         event.save()
#         messages.success(request, 'Event updated successfully')
#         return redirect('all-events')
#     return render(request,'update_event.html',context)
#
# @login_required
# def add_participant(request):
#     if request.method == 'POST':
#         participant_name = request.POST.get('p-name')
#         participant_email = request.POST.get('p-email')
#         participant_event_name = request.POST.get('e-name')
#         context = {
#             "participant_name":participant_name,
#             "participant_email":participant_email,
#             "participant_event_name":participant_event_name,
#             "success":"Participant added successfully"
#         }
#         query=Participant(participant_name=participant_name,participant_email=participant_email,event_name=participant_event_name)
#         query.save()
#         return render(request,'create_participants.html',context)
#     return render(request,'create_participants.html')
#
# @login_required
# def participants(request):
#     all_participants = Participant.objects.all()
#     context = {'all_participants':all_participants}
#     return render(request,'participant_list.html',context)
# @login_required
# def delete_participant(request, id):
#     participant = Participant.objects.get(id=id)
#     participant.delete()
#     messages.success(request, 'Participant deleted successfully')
#     return redirect('participants')
#
# @login_required
# def update_participant(request, id):
#     participant = Participant.objects.get(id=id)
#     context = {'participant':participant}
#     if request.method == 'POST':
#         updated_name = request.POST.get('p-name')
#         updated_email = request.POST.get('p-email')
#         updated_event_name = request.POST.get('e-name')
#         participant.name = updated_name
#         participant.email = updated_email
#         participant.event_name = updated_event_name
#         participant.save()
#         messages.success(request, 'Participant updated successfully')
#         return redirect('all-participants')
#     return render(request,'update_participants.html',context)
#
# def register(request):
#     if request.method == 'POST':
#         form=UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Registration was successful')
#             return redirect('user-registration')
#     else:
#          form=UserRegistrationForm()
#     return render(request,'delete_event.html',{'form':form})
#
#
#
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Event, Participant
from .forms import EventForm, ParticipantForm  # Assuming you have forms for Event and Participant


# # Create your views here.
def index(request):
    return render(request,'index.html')
def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event created successfully!')
            return redirect('event-list')
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})

def update_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('event-list')
    else:
        form = EventForm(instance=event)
    return render(request, 'update_event.html', {'form':form})

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted successfully!')
        return redirect('event-list')
    return render(request, 'delete_event.html', {'event': event})

def participant_list(request):
    participants = Participant.objects.all()
    return render(request, 'participant_list.html', {'participants': participants})

def create_participant(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Participant added successfully!')
            return redirect('participant-list')
    else:
        form = ParticipantForm()
    events=Event.objects.all()#fetch the events
    context={
        'form': form,
        'events': events, #pass events to the template
    }
    return render(request, 'create_participants.html', context)

def update_participant(request, participant_id):
    participant = get_object_or_404(Participant, id=participant_id)
    if request.method == 'POST':
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            messages.success(request, 'Participant updated successfully!')
            return redirect('participant-list')
    else:
        form = ParticipantForm(instance=participant)
    events=Event.objects.all()
    context={
        'form': form,
        'events': events,
        'participant': participant,#pass participant to the template
    }
    return render(request, 'update_participants.html', context)

def delete_participant(request, participant_id):
    participant = get_object_or_404(Participant, id=participant_id)
    if request.method == 'POST':
        participant.delete()
        messages.success(request, 'Participant deleted successfully!')
        return redirect('participant-list')
    return render(request, 'delete_participant.html', {'participant': participant})

