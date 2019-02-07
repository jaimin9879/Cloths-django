from django.conf.urls import url, include
from .views import home, contact, profile, editprofile, deleteProfile, help, feedback, howitworks, aboutus, faq, location
from Products.views import SearchList1

urlpatterns = [
   url(r'^$', home, name='home'),
   url(r'^contact/', contact,name='contact'),
   url(r'^accounts/', include('allauth.urls')),
   url(r'^profile/$', profile, name="profile"),
   url(r'^profile/edit/', editprofile, name="profile_edit"),
   url(r'^profile/delete/(?P<pk>\d+)/$', deleteProfile, name="profile_delete"),
   url(r'^help/', help, name='help'),
   url(r'^products/', include('Products.urls')),
   url(r'^feedback/', feedback, name='feedback'),
   url(r'^cart/', include('Cart.urls', namespace="cart")),
   url(r'^howitworks/', howitworks, name='howitworks'),
   url(r'^aboutus/', aboutus, name='aboutus' ),
   url(r'^faq/', faq, name='faq' ),
   url(r'^search1/$', SearchList1.as_view(), name="search1"),
   url(r'^location/$', location, name="location"),
]