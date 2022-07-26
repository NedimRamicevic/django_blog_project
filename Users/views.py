from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account created for ' + user)
            return redirect('blog-home')
        else:
            return redirect('register')
    else:
        form = UserCreationForm()
        return render(request, 'users/register.html', {'form': form})
