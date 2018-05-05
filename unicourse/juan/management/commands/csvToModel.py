from csv import DictReader
from django.core.management import BaseCommand


from juan.models import course1


class Command(BaseCommand):

    help = "loads csv data"

    def handle(self, *args, **options):
        if course1.objects.exists():
            print("already loaded")
            return

        for row in DictReader(open("./database.csv")):
            course = course1()
            course.institution = row["Institution"]
            course.name = row["Course"]
            course.label = row["Label"]
            course.mode = row["Mode"]
            course.salary = row["Salary"]
            course.avgTariff = row["avgTariff"]
            course.minTariff = row["lowerTariff"]
            course.employment = row["Employment"]
            course.url = row["URL"]
            course.save()
