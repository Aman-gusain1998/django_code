from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class loginform(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']
        labels = {'email':'address'}