from django.urls import path
from foodutility import views
urlpatterns = [
    path('',views.home,name="homepage" ),
    path('signup/', views.signup, name='signup'),
    path('login_view/',views.login_view,name="login_view"),
    path('logout/',views.logout_view,name="logout_view"),
    path('volunteer/',views.volunteer,name="volunteer"),
    path('donator/',views.donator,name="donator"),
    path('donator/chooseDonate/money/',views.money,name="d-money"),
    path('donator/chooseDonate/',views.chooseDonate,name="choose_donate"),
    path('donator/chooseDonate/food/',views.food,name="d-food"),
    path('volunteer/history',views.history,name="history"),
]