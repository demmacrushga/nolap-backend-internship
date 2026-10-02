import random
from django.core.management.base import BaseCommand
from grades.models import Student, Course, Score


FIRST_NAMES = [
    'Ama', 'Kofi', 'Efua', 'Kwame', 'Abena', 'Yaw', 'Akosua', 'Kwabena',
    'Adwoa', 'Kojo', 'Afia', 'Kwaku', 'Esi', 'Kwadwo', 'Akua', 'Fiifi',
    'Maame', 'Nana', 'Yaa', 'Kweku',
]

LAST_NAMES = [
    'Mensah', 'Owusu', 'Asante', 'Boateng', 'Addo', 'Appiah', 'Osei',
    'Agyemang', 'Frimpong', 'Acheampong', 'Darko', 'Amponsah', 'Gyasi',
    'Sarpong', 'Tetteh', 'Opoku', 'Annan', 'Kusi', 'Amoako', 'Yeboah',
]

COURSES = [
    ('Introduction to Programming', 'CS101'),
    ('Data Structures and Algorithms', 'CS201'),
    ('Database Systems', 'CS301'),
    ('Web Development', 'CS210'),
    ('Operating Systems', 'CS305'),
]


class Command(BaseCommand):
    help = 'Seeds the database with sample students, courses, and scores'

    def handle(self, *args, **options):
        self.stdout.write('Clearing existing data...')
        Score.objects.all().delete()
        Student.objects.all().delete()
        Course.objects.all().delete()

        self.stdout.write('Creating courses...')
        courses = []
        for name, code in COURSES:
            course = Course.objects.create(name=name, code=code)
            courses.append(course)

        self.stdout.write('Creating students...')
        students = []
        names = list(zip(FIRST_NAMES, LAST_NAMES))
        random.shuffle(names)
        for i, (first, last) in enumerate(names[:18]):
            student = Student.objects.create(
                first_name=first,
                last_name=last,
                email=f'{first.lower()}.{last.lower()}{i}@example.com',
            )
            students.append(student)

        self.stdout.write('Creating scores...')
        for student in students:
            # each student takes 3 to 5 of the courses, randomly
            enrolled_courses = random.sample(courses, k=random.randint(3, 5))
            for course in enrolled_courses:
                # realistic spread: mostly 40-95, occasionally lower or higher
                score_value = round(random.triangular(30, 100, 72), 2)
                Score.objects.create(student=student, course=course, score=score_value)

        self.stdout.write(self.style.SUCCESS(
            f'Seeded {len(students)} students, {len(courses)} courses, '
            f'and {Score.objects.count()} scores.'
        ))