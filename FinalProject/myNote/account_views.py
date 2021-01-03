# from django.core.checks import messages
# from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm


def logout_user(request):
    logout(request)
    return redirect("login_user")


def login_user(request):
    if request.method == "GET":
        return render(request, 'authentication/login.html')
    else:
        username = request.POST['username']
        user = authenticate(request, username=username,
                            password=request.POST['password'])
        if user is None:
            return render(request, 'authentication/login.html',
                          {'username': username, 'message': 'Invalid Login'})
        else:
            login(request, user)
            return redirect("display")


def register_user(request):
    if request.method == "GET":
        # form = UserCreationForm()
        return render(request, 'authentication/signUp.html')
    else:
        # form = UserCreationForm(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        try:
            x=User.objects.get(username=username)
            print("user existed")
            return render(request, 'authentication/signUp.html', {'message': 'userName existed',"flag":'flagtesting'})
        except:
            if password2 == password1:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                print('User Created..')
                return redirect('login_user')
            else:
                print("password not match")
                return render(request, 'authentication/signUp.html', {'message': 'password must be same',"flag":'flagtesting'})




def change_password(request):
    if request.method == 'GET':
        form=PasswordChangeForm(request.user.password)
        return render(request,'change_password.html',{'form':form})
    else:
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            print(user)
            login(request,user)
            update_session_auth_hash(request, user)
            # messages.success(request, 'Your password was successfully updated!')
            return redirect('display')
        else:
            return render(request,'change_password.html',{'form':form,'messages':'not changed'})


# from django.shortcuts import render, redirect
# from django.contrib.auth import logout, login, authenticate
# from django.contrib.auth.forms import UserCreationForm
#
#
# def logout_user(request):
#     logout(request)
#     return redirect("login_user")
#
#
# # def login_user(request):
# #     if request.method == "GET":
# #         return render(request, 'authentication/login.html')
# #     else:
# #         username = request.POST['username']
# #         user = authenticate(request, username=username,
# #                             password=request.POST['password'])
# #         if user is None:
# #             return render(request, 'authentication/login.html',
# #                           {'username': username, 'message': 'Invalid Login'})
# #         else:
# #             login(request, user)
# #             return redirect("display")
# #         # return redirect("display")
#
#
#
#
#
# def login_user(request):
#     if request.method == "GET":
#         return render(request, 'authentication/login.html')
#     else:
#         username = request.POST['username']
#         user = authenticate(request, username=username,
#                             password=request.POST['password'])
#         if user is None:
#             return render(request, 'authentication/login.html',
#                           {'username': username,'message': 'Invalid Login Credentioals'})
#         else:
#             login(request,user)
#         return redirect("display")
#
# def signUp(request):
#     if request.method == "GET":
#         form = UserCreationForm()
#         return render(request, 'authentication/signUp.html', {'form': form})
#     else:
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             # user = form.save(commit=False)
#             login(request, user)
#             return redirect('display')
#         else:
#             return render(request, 'authentication/signUp.html', {'form': form})
#
#
#
# # from django.shortcuts import render, redirect
# # from django.contrib.auth import logout, login as inbulit_login, authenticate
# # from django.contrib.auth.forms import UserCreationForm
# #
# # # from django.contrib.auth import update_session_auth_hash
# # # from django.contrib.auth.forms import PasswordChangeForm
# #
# #
# # def logout_user(request):
# #     logout(request)
# #     return redirect("login")
# #
# #
# # def login(request):
# #     if request.method == "GET":
# #         return render(request, 'authentication/login.html')
# #     else:
# #         username = request.POST['username']
# #         user = authenticate(request, username=username,
# #                             password=request.POST['password'])
# #         if user is None:
# #             return render(request, 'authentication/login.html',
# #                           {'username': username,'message': 'Invalid Login Credentioals'})
# #         else:
# #             inbulit_login(request,user)
# #         return redirect("display")
# #
# # def signUp(request):
# #     if request.method == "GET":
# #         form = UserCreationForm()
# #         return render(request, 'authentication/signUp.html',{'form':form})
# #     else:
# #         form = UserCreationForm(request.POST)
# #         # print(form)
# #         if form.is_valid():
# #             user = form.save(commit=False)
# #             # user = form.save()
# #             login(request, user)
# #             # user.save()
# #             return redirect("display")
# #         else:
# #             return render(request, 'authentication/signUp.html',{'form':form})
# #
# #     # else:
# #     #     form = UserCreationForm(request.POST)
# #     #     if form.is_valid():
# #     #         user = form.save()
# #     #         login(request, user)
# #     #         return redirect('/pa/home/')
# #     #     else:
# #     #         return render(request, 'register.html', {'form': form})
#
# # # def change_password(request):
# # #     if request.method == 'POST':
# # #         form = PasswordChangeForm(request.user, request.POST)
# # #         if form.is_valid():
# # #             user = form.save()
# # #             update_session_auth_hash(request, user) # Important!
# # #             return render(request, 'change_password.html',{'form':form,'message': 'password changed successfully!'})
# # #         else:
# # #             return render(request, 'change_password.html',{'form': form, 'message': 'please correct the password!'})
# # #     else:
# # #         form = PasswordChangeForm(request.user)
# # #         return render(request, 'change_password.html', {'form': form})
