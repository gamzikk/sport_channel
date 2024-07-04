from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .models import Profile
from django.contrib.auth import get_user_model
User = get_user_model()
from .forms import UserRegistrationForm, LoginUserForm, ProfileForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404


# Функция регистрации пользователя.
def user_register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'users/user_profile.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'users/register.html', {'user_form': user_form})


# Функция входа в аккаунт (авторизация).
def user_login(request):
    if request.method == 'POST':
        user_form = LoginUserForm(request.POST)
        if user_form.is_valid():
            cd = user_form.cleaned_data
            user = authenticate(email=cd['email'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'main/main.html')
                else:
                    return HttpResponse('Отключённая учётная запись.')
            else:
                return HttpResponse('Неверный логин или пароль.')
    else:
        user_form = LoginUserForm()
    return render(request, 'users/login.html', {'user_form': user_form})


# Функция выхода из аккаунта.
def logout_user(request):
    logout(request)
    return redirect('main')


# class ShowProfilePageView(DetailView):
#     model = Profile
#     template_name = 'users/user_profile.html'

#     def get_context_data(self, *args, **kwargs):
#         users = Profile.objects.all()
#         context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
#         page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
#         context['page_user'] = page_user
#         return context


@login_required
def profile(request, pk):
    profile = Profile.objects.get(pk = pk)
    return render(request, 'users/user_profile.html', {'profile': profile})

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


def profile_edit(request, pk):
    profile = Profile.objects.get(pk = pk)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            return render(request, 'users/user_profile.html')
    else:
        profile_form = ProfileForm()
    return render(request, 'users/profile_edit.html', {'profile': profile, 'profile_form': profile_form})


def test_cookie(request):
    if request.method == 'POST':
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            # Веб-обозреватель поддерживает cookie
        else:
            # Веб-обозреватель не поддерживает cookie
            request.session.set_test_cookie()
    return render(request, 'users/test_cookie.html')
