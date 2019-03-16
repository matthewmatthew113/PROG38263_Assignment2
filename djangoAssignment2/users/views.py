#Import Various Libraries including forms for user registration and profile updating
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm

#Upon a registration the program will check to see if the request is from a POST method. Upon confirmation the form data is validated and sent to the database for storage, the user is then redirected to the login page upon completion 
def register(request):
    if request.method == 'POST':
        #Defines the form variable as the data sent in html POST form if POST method is sent
        form = UserRegisterForm(request.POST)
        #Validates form data and saves it if it is valid
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You are now able to log in')
            return redirect('/login')
    else:
        #If no POST method then form is null
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
	
#Login is required for said function, upon recieving a POST method from profile, the user sets a update form which holds the newly edited data. Upon validation of said data the user may then be able to complete their edit request
@login_required
def profile(request):
    if request.method == 'POST':
        #Defines the form variable as the data sent in html POST form if POST method is sent
        u_form = UserUpdateForm(request.POST, instance=request.user)
        #Validates form data and saves it if it is valid
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
    #If no POST method then form is null
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
    }

    return render(request, 'users/profile.html', context)
