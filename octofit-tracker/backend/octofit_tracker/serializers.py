from rest_framework import serializers
from .models import Activity, Leaderboard, Team, User, Workout

class TeamSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    def get_id(self, obj):
        return str(obj.id) if obj.id else None
    class Meta:
        model = Team
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    team = serializers.SerializerMethodField()
    def get_id(self, obj):
        return str(obj.id) if obj.id else None
    def get_team(self, obj):
        try:
            return str(obj.team.id) if obj.team and obj.team.id else None
        except Exception:
            return None
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'team']

class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    def get_id(self, obj):
        return str(obj.id) if obj.id else None
    def get_user(self, obj):
        try:
            return str(obj.user.id) if obj.user and obj.user.id else None
        except Exception:
            return None
    class Meta:
        model = Activity
        fields = ['id', 'user', 'type', 'duration', 'date']

class WorkoutSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    suggested_for = serializers.SerializerMethodField()
    def get_id(self, obj):
        return str(obj.id) if obj.id else None
    def get_suggested_for(self, obj):
        try:
            return [str(user.id) for user in obj.suggested_for.all()]
        except Exception:
            return []
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'suggested_for']

class LeaderboardSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    team = serializers.SerializerMethodField()
    def get_id(self, obj):
        return str(obj.id) if obj.id else None
    def get_team(self, obj):
        try:
            return str(obj.team.id) if obj.team and obj.team.id else None
        except Exception:
            return None
    class Meta:
        model = Leaderboard
        fields = ['id', 'team', 'points']
