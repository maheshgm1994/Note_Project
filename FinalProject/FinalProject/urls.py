"""finalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

# from FinalProject.myNote.classviews import NoteList, NoteDetails
from myNote import views
from myNote import account_views

from myNote.classviews import NoteList, NoteDetails

urlpatterns = [
    path('admin/', admin.site.urls),

    # for authentication
    path("",account_views.login_user,name="login_user"),
    path("logout_user/",account_views.logout_user,name="logout_user"),
    path("signUp/",account_views.register_user,name="signUp"),

    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # path('^', include('django.contrib.auth.urls')),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # # create retrieve update delete operations
    path("addNote/",views.addNote,name="addNote"),
    path("display/",views.display,name="display"),
    path("editNote/<int:id>",views.editNote,name="editNote"),
    path("updateNote/<int:id>",views.updateNote,name="updateNote"),
    path("deleteNote/<int:id>",views.deleteNote,name="deleteNote"),
    path("profile/",views.profile,name="profile"),

    path("contact/",views.contact,name="contact"),
    path("service/",views.service,name="service"),
    path("home/",views.home,name="home"),
    path("about/",views.about,name="about"),

    # path("displayRecentAdded/",views.displayRecentAdded),
    path("searchText/",views.searchText,name="searchText"),

    # path("listAllNotes/",views.listAllNotes,name="listAllNotes"),
    # path("editSingleNote/<int:id>",views.editSingleNote),
    # path("deleteNote/<int:id>",views.deleteNote),
    # path("displayRecentAdded/",views.displayRecentAdded),
    # path("searchNoteByText/",views.searchNoteByText,name="searchNoteByText"),



    # Rest function views
    path("api/note/", views.notes),
    path("api/notes/<int:id>", views.note_details),


    # REST class views
    #RestViews ClassBased
    path("api2/note/", NoteList.as_view()),
    path("api2/notes/<int:id>", NoteDetails.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

