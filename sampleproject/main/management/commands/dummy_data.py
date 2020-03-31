from django.core.management.base import BaseCommand
from django.db import DatabaseError, transaction
from user.models import     ActivityPeriod,User

class Command(BaseCommand):
    help = 'Import Active/Inactive static data in all master tables'

    def handle(self, *srgs, **options):
        self.stdout.write(
            '_______ Began: adding to dummy data _______ '
        )
        ActivityPeriod_entry_1 = ActivityPeriod(start_time='2020-02-1 13:33:00',end_time='2020-02-1 13:54:00')
#         activity_periods= ActivityPeriod.objects.get(pk=1)
#         User_entry_1 = User(real_name='Egon Spengler',tz='America/Los_Angeles',activity_periods=activity_periods)

        try:
            with transaction.atomic():
                ActivityPeriod_entry_1.save()
#                 User_entry_1.save()
                self.stdout.write(
                    '_______ END: dummy data  added to DB successfully _______ '
                )
        except DatabaseError as db_exc:
            self.stdout.write(
                '_______ Error: in DB, failed to dumy data added to DB  _______ \n%s' % db_exc
            )
        except Exception as exc:
            self.stdout.write(
                '_______ Error: occured while added to dummy data   _______ \n%s' % exc
            )
