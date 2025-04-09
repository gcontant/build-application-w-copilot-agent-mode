from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(email='thundergod@mhigh.edu', name='Thor', age=30),
            User(email='metalgeek@mhigh.edu', name='Tony Stark', age=35),
            User(email='zerocool@mhigh.edu', name='Steve Rogers', age=32),
            User(email='crashoverride@mhigh.edu', name='Natasha Romanoff', age=28),
            User(email='sleeptoken@mhigh.edu', name='Bruce Banner', age=40),
        ]
        for user in users:
            user.save()

        # Create teams
        team1 = Team(name='Blue Team')
        team2 = Team(name='Gold Team')
        team1.save()
        team2.save()
        team1.members.set(users[:3])
        team2.members.set(users[3:])

        # Create activities
        activities = [
            Activity(user=users[0], activity_type='Cycling', duration=60, calories_burned=500, date='2025-04-01'),
            Activity(user=users[1], activity_type='Crossfit', duration=90, calories_burned=700, date='2025-04-02'),
            Activity(user=users[2], activity_type='Running', duration=45, calories_burned=400, date='2025-04-03'),
            Activity(user=users[3], activity_type='Swimming', duration=30, calories_burned=300, date='2025-04-04'),
            Activity(user=users[4], activity_type='Strength Training', duration=120, calories_burned=800, date='2025-04-05'),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(user=users[0], points=100, rank=1),
            Leaderboard(user=users[1], points=90, rank=2),
            Leaderboard(user=users[2], points=85, rank=3),
            Leaderboard(user=users[3], points=80, rank=4),
            Leaderboard(user=users[4], points=75, rank=5),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event', duration=60, calories=500),
            Workout(name='Crossfit', description='High-intensity interval training', duration=90, calories=700),
            Workout(name='Running Training', description='Training for a marathon', duration=45, calories=400),
            Workout(name='Swimming Training', description='Training for a swimming competition', duration=30, calories=300),
            Workout(name='Strength Training', description='Weightlifting and resistance training', duration=120, calories=800),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
