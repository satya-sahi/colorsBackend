from django.urls import path
from . import views


urlpatterns = [
    path('getColors/', views.get_colour_swatches_view, name='get_colors'),
    path('brgb/<str:color>', views.get_colour_swatches_view, name='get_colors')
]