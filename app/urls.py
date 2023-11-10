# ***** appppppppppppppppppppppppppppppppppp


from django.urls import path 
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('product/',views.product ),
    path('product/<int:id>',views.product),
    path('', views.index),
    path('register', views.register),
    path('getCart', views.getCart),
    path('categories',views.Category_view.as_view()),
    path('login/', TokenObtainPairView.as_view()),
]
