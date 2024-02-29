from django.urls import path 
from django.urls.conf import include
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('trainees',views.TraineeVeiwSet)
router.register('sports',views.SportViewSets)
router.register('coachs',views.CoachViewSets)
# router.register('classes',views.ClassViewSets)

coachs_router = routers.NestedDefaultRouter(router, 'coachs',lookup='coach')
coachs_router.register('reviews',views.ReviewViewSet,basename ='coach-reviews')
urlpatterns = router.urls + coachs_router.urls
# urlpatterns = [
#     path('trainees/' , views.TraineeList.as_view()),
#     path('trainees/<int:pk>/',views.TraineeDetail.as_view()),
#     path('sports/',views.SportList.as_view()),
#     path('sports/<int:pk>',views.SportDatail.as_view(), name='sport-detail'),
#     path('coachs/',views.CoachList.as_view())
# ]