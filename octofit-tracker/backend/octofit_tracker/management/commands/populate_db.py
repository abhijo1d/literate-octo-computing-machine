from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data in a safe order for Djongo
        for model in [Activity, Workout, Leaderboard, User, Team]:
            for obj in model.objects.all():
                if getattr(obj, 'id', None):
                    obj.delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Yoga', duration=20, date=timezone.now().date())

        # Create workouts
        w1 = Workout.objects.create(name='Hero HIIT', description='High intensity interval training for heroes')
        w2 = Workout.objects.create(name='Power Yoga', description='Yoga for strength and flexibility')
        w1.suggested_for.set([users[0], users[2]])
        w2.suggested_for.set([users[1], users[3]])

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=80)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
