from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.opening,name='open'),
    path('help',views.helppage,name='help'),
    path('signin',views.register,name='signin'),
    path('login',views.loginpage,name='login'),
    path('course',views.course,name='course'),
    path('home',views.home,name='home'),
    path('choise',views.choise,name='choise'),
    path('material/<str:name>',views.material,name='material'),
    path('materialview/<str:name>',views.material_view,name='mateview'),
    path('materialadd',views.material_add,name='materialadd'),
    path('choose',views.choose,name='choose'),
    path('homeworkz/<str:name>',views.homeworkz,name='homeworkz'),
    path('hwqtnadd',views.hwqtn_add,name='hwqtnadd'),
    path('hwqadd',views.hwansadd,name='hwqadd'),
    path('hwanswer',views.hwanswer,name='hwanswer'),
    path('index', views.index, name='index'),
    path('detail/<int:poll_id>/', views.detail, name='detail'),
    path('<int:poll_id>/results/', views.results, name='results'),
    path('<int:poll_id>/vote/', views.vote, name='vote'),
    path('del/<int:pk>',views.Dele.as_view(),name='del'),
    path('polladd',views.poll_add,name='polladd'),
    path('choiceadd',views.choice_add,name='choiceadd'),
    path('choice_add_another',views.choice_add_another,name='choadd'),
    path('quiz_entry',views.quiz_entry,name='quiz_entry'),
    path('quiz',views.quiz,name='quiz'),
    path('logout',views.logoutpage,name='logout')
]


urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)