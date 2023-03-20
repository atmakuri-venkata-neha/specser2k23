from unicodedata import name
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path("",views.home,name='home'),
    path("aboutus",views.aboutus,name='about_us'),
    path("events/<int:id>",views.events,name='events'),
    path("events/technical",views.techevents,name='technical_events'),
    path("events/non_technical",views.nontechevents,name='non_technical_events'),
    path("user",views.user,name='user'),
    path("signin",views.login,name='signin'),
    path("updateuser",views.updateuser,name='updateuser'),
    path("events/makepayment",views.makepayment,name='makepayment'),
    path("callback/",views.handlerequest,name='callback'),
    path("events/intiatepayment",views.intiatepayment,name='intiatepayment'),
    path("sponsors",views.sponsors,name="sponsors"),
    path('workshop',views.workshop,name='ar_vr_workshop'),
    path('3dworkshop',views.mworkshop,name='3d_workshop')
    
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)