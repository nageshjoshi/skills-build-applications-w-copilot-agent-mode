from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pass', team=team)
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(str(user.team), 'Test Team')

    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pass', team=team)
        activity = Activity.objects.create(user=user, type='Run', duration=30, calories=200)
        self.assertEqual(str(activity), 'testuser - Run')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='desc', duration=45)
        self.assertEqual(str(workout), 'Test Workout')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pass', team=team)
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(str(leaderboard), 'testuser: 100')
