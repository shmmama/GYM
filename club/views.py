from django.shortcuts import get_object_or_404
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter , OrderingFilter
from rest_framework.pagination import PageNumberPagination
from .filters import SportFilter
from . models import Trainee,Sport,Coach,Review
from .serializer import TraineeSerializer, SportSerializer, CoachSerializer, ReviewSerializer

# Create your views here.
class TraineeVeiwSet(ModelViewSet):
        queryset = Trainee.objects.all()
        serializer_class = TraineeSerializer
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ['sport_id','suitable_period']      
        def get_serializer_context(self):
            return {'request': self.request}
        def destroy(self, request, *args, **kwargs):
              trainee = get_object_or_404(Trainee, pk = kwargs['pk'])
              return super().destroy(request, *args, **kwargs)
        
class SportViewSets(ModelViewSet):
        queryset = Sport.objects.annotate(trainees_count = Count('trainee')).all()
        serializer_class = SportSerializer
        filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
        filterset_class = SportFilter
        search_fields = ['name']
        ordering_fields = ['price' , 'trainees_count']
        def destroy(self, request, *args, **kwargs):
            if Trainee.objects.filter(sport_id =kwargs['pk']).count()>0: 
                return Response({'Error':'Sport can not be delete because there is a trainees in it'},status=status.HTTP_400_BAD_REQUEST)
            return super().destroy(request, *args, **kwargs)
        
class CoachViewSets(ModelViewSet):
        queryset = Coach.objects.all()
        serializer_class = CoachSerializer
        filter_backends = [SearchFilter]
        search_fields = ['first_name']

class ReviewViewSet(ModelViewSet):
      serializer_class = ReviewSerializer
      filter_backends = [OrderingFilter]
      ordering_fields = ['date', 'star'] 
      def get_queryset(self):
            return Review.objects.filter(coach_id=self.kwargs['coach_pk'])
      def get_serializer_context(self):
            return {'coach_id': self.kwargs['coach_pk']}
            

        
