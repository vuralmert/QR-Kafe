from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def LoginView(request):
    if request.method == "POST":
        # POST Methodu Değişkenlerinin Kullanıcıdan Alınması
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Başarıyla giriş yaptınız!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.warning(request, "Yanlış veya eksik bilgi girdiniz. Lütfen tekrar deneyin.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return HttpResponse("404 - Not found")


def SignupView(request):
    if request.method == "POST":
        # POST Methodu Değişkenlerinin Kullanıcıdan Alınması
        username = request.POST['username']
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        email = request.POST['email1']
        phone = request.POST['phone']
        password = request.POST['password']
        password1 = request.POST['password1']

        # Şifre Uyuşmazlık Kontrolü
        if password1 != password:
            messages.warning(request, "Girdiğiniz şifreler eşleşmiyor.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        try:
            user = User.objects.get(username=username)
            messages.warning(request, "Kullanıcı adı alınmış. Lütfen başka bir kullanıcı adı deneyin.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except User.DoesNotExist:
            # Kullanıcı Oluşturuluyor
            myuser = User.objects.create_user(username=username, email=email, password=password)
            myuser.first_name = f_name
            myuser.last_name = l_name
            myuser.phone = phone
            myuser.save()
            messages.success(request, "Hesabınız oluşturuldu!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponse("404 - Not found")


def LogoutView(request):
    logout(request)
    messages.success(request, "Başarıyla çıkış yaptınız!")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
