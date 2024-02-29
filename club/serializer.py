from rest_framework import serializers

from club.models import Sport,Trainee, Coach,Review, Class

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ['id', 'name' , 'price','avaliable_time', 'trainees_count']
    trainees_count = serializers.IntegerField(read_only =True)

class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainee
        fields = ['id','first_name','last_name','birth_date',
                  'phone','suitable_period', 'ultimate_goal','sport']
    sport = serializers.HyperlinkedRelatedField(
            queryset = Sport.objects.all(),
            view_name='sport-detail'
        )

class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ['id', 'first_name', 'last_name', 'bio', 'suitable_period']
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','date','name','description', 'star']

    def create(self, validated_data):
        coach_id = self.context['coach_id']
        return Review.objects.create(coach_id=coach_id , **validated_data)
    