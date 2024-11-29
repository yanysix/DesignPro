from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DesignRequest
from .forms import DesignRequestForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DesignRequest
from .forms import DesignRequestForm
from django.contrib import messages

@login_required
def create_request(request):
    if request.method == 'POST':
        form = DesignRequestForm(request.POST)
        if form.is_valid():
            request_obj = form.save(commit=False)
            request_obj.user = request.user
            request_obj.save()
            messages.success(request, 'Заявка успешно создана!')
            return redirect('my_requests')  # Redirect to view requests page
    else:
        form = DesignRequestForm()
    return render(request, 'create_request.html', {'form': form})

@login_required
def my_requests(request):
    requests = DesignRequest.objects.filter(user=request.user)
    return render(request, 'my_requests.html', {'requests': requests})

@login_required
def delete_request(request, request_id):
    request_obj = get_object_or_404(DesignRequest, pk=request_id, user=request.user)
    if request.method == 'POST':
        request_obj.delete()
        messages.success(request, 'Заявка успешно удалена!')
        return redirect('my_requests')
    return render(request, 'delete_request.html', {'request': request_obj})


def index(request):

    return render(
        request,
        'index.html',
        #context={'':,},
    )

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'studio/register.html', { 'form': form})
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Вы успешно зарегестрировались')
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'studio/register.html', {'form': form})
