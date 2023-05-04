from django.urls import path

from mobile_mart_app import views

urlpatterns = [
    path('mobile/login/', views.login_view),
    path('mobile/add/', views.add_mobile_device),
    path('mobile/delete/', views.delete_mobile_device),
    path('mobile/list/', views.list_all_phones),
    path('mobile/filter/', views.list_phones_with_filters),
    path('mobile/price-range/', views.list_phones_with_price_range),
    path('mobile/order/', views.list_phones_ordered),
]