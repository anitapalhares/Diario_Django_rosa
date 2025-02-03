from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Entry, Mood, MoodOverTime
from django.http import HttpResponse


def diarioapp(request):
    return render(request, "site.html")


def register_entry(request):
    if request.method == 'POST':
        date = request.POST['date']
        day_summary = request.POST['day-summary']
        entry_text = request.POST['entry']
        
        # Salvar a entrada no diário
        entry = Entry.objects.create(date=date, day_summary=day_summary, entry_text=entry_text)
        
        return redirect('register_mood', entry_id=entry.id)

def register_mood(request, entry_id):
    if request.method == 'POST':
        date = request.POST['date']
        mood = request.POST['mood']
        entry = Entry.objects.get(id=entry_id)
        
        # Salvar o mood para essa entrada
        Mood.objects.create(date=date, mood=mood, entry=entry)
        
        return redirect('register_mood_over_time', entry_id=entry.id)

def register_mood_over_time(request, entry_id):
    if request.method == 'POST':
        date = request.POST['date']
        moment = request.POST['moment']
        mood = request.POST['mood-time']
        entry = Entry.objects.get(id=entry_id)
        
        # Salvar o humor durante o dia
        MoodOverTime.objects.create(date=date, moment=moment, mood=mood, entry=entry)
        
        return HttpResponse("Humor ao longo do dia registrado com sucesso!")
