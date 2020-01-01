from django import template
from django.utils import timezone


register = template.Library()

@register.filter(name="time_left")
def time_left(value):
    timing = value - timezone.now()
    no_days, seconds = timing.days, timing.seconds
    hour = no_days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    
    timing = str(hour) + "h" + str(minutes) + "m" + str(seconds) + "s"
    
    
