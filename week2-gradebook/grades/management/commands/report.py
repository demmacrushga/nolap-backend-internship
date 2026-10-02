from django.core.management.base import BaseCommand
from django.db.models import Avg
from grades.models import Student, Course, Score


class Command(BaseCommand):
    help = 'Runs the required gradebook reports'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n=== Top 3 scorers in each course ===\n'))
        for course in Course.objects.all():
            self.stdout.write(f'{course.name} ({course.code}):')
            top_scores = (
                Score.objects.filter(course=course)
                .select_related('student')
                .order_by('-score')[:3]
            )
            for rank, score in enumerate(top_scores, start=1):
                self.stdout.write(f'  {rank}. {score.student} - {score.score}')
            self.stdout.write('')

        self.stdout.write(self.style.SUCCESS('\n=== Students below the pass mark (50) ===\n'))
        failing_scores = (
            Score.objects.filter(score__lt=50)
            .select_related('student', 'course')
            .order_by('student__last_name')
        )
        for score in failing_scores:
            self.stdout.write(f'{score.student} - {score.course}: {score.score}')

        self.stdout.write(self.style.SUCCESS(
            '\n=== Average score per course (highest to lowest) ===\n'
        ))
        course_averages = (
            Course.objects.annotate(avg_score=Avg('scores__score'))
            .order_by('-avg_score')
        )
        for course in course_averages:
            self.stdout.write(f'{course.name} ({course.code}): {course.avg_score:.2f}')