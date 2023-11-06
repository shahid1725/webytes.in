from django.urls import path
from . import views

urlpatterns=[
    path('',views.Dashboard.as_view(),name="dashboard"),
    path('login', views.Login.as_view(), name="login"),
    path('logout', views.signout, name="logout"),
    path('base', views.base, name='base'),
    path('enquiries', views.ListEnquiryView.as_view(), name='enquiries'),
    path('enquiries/edit/<int:id>', views.EditEnquiryView.as_view(), name='edit_enquiries'),



#-------------------------- ENQUIRIES -----------------------------------
    path('enquiries', views.ListEnquiryView.as_view(), name="enquiries"),
    path('pending/enquiries', views.ListAttendedEnquiryView.as_view(), name="attended_enquiries"),
    path('enquiries/edit/<str:id>', views.EditEnquiryView.as_view(), name="enquiry_edit"),
]