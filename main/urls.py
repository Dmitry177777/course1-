from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.decorators.cache import cache_page

from .views import *

from main.apps import MainConfig

app_name = MainConfig.name





urlpatterns = [
    path('', index.as_view(), name="index"),


    path('scheduler/', include('scheduler.urls')),

    path('MailingSetting/', MailingSettingListView.as_view(), name='MailingSetting_list'),
    path('MailingSetting_item/<int:pk>/', cache_page(60)(MailingSettingDetailView.as_view()), name='MailingSetting_item'),
    path('MailingSetting/create/', MailingSettingCreateView.as_view(), name='MailingSetting_create'),
    path('MailingSetting/update/<int:pk>/', MailingSettingUpdateView.as_view(), name='MailingSetting_update'),
    path('MailingSetting/delete/<int:pk>/', MailingSettingDeleteView.as_view(), name='MailingSetting_delete'),




    path('clients/', ClientListView.as_view(), name='client_list'),
    path('client_item/<int:pk>/', cache_page(60)(ClientDetailView.as_view()), name='client_item'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('clients/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),





    path('blog/', BlogListView.as_view(), name='blog_list'),

    path('blog_item/<str:slug>/', BlogDetailView.as_view(), name='blog_item'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),

]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)