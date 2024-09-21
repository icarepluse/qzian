from .models import cmuser
from django.core.files.storage import FileSystemStorage
from django.utils.crypto import get_random_string
import random

def usrreg(request):
    UserProfile=cmuser()
    UserProfile.unames=request.POST.get('Username')
    UserProfile.upass=request.POST.get('Password')
    UserProfile.umail=request.POST.get('email')
    suss= UserProfile.save()
    return 1