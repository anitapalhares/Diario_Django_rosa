from django.db import models

class Entry(models.Model):
    date = models.DateField()
    day_summary = models.TextField()  # Descrição do dia
    entry_text = models.TextField()  # Texto do diário

    def __str__(self):
        return f"Entrada de {self.date}"

class Mood(models.Model):
    date = models.DateField()
    mood = models.CharField(max_length=100)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name="moods")

    def __str__(self):
        return f"Mood {self.mood} em {self.date}"

class MoodOverTime(models.Model):
    date = models.DateField()
    moment = models.CharField(max_length=100)  # Manhã, Tarde, Noite
    mood = models.CharField(max_length=100)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name="mood_over_time")

    def __str__(self):
        return f"Mood {self.mood} durante {self.moment} em {self.date}"
