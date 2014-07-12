from django.core.management.base import BaseCommand, CommandError

# connects to twitter 
# gets json file based on #CRASHLACMA
# saves it to the static folder.


class Command(BaseCommand):
	help = 'Gets twiiter feed for hashtag #CRASHLACMA'

	def handle(self, *args, **options): #there are no args or options yet. 
		#use stdout because this will be run as cron job eventually
		#(wait isn't print() in 3.x stdout?)
		self.stdout.write('Hello There!')
		
	def test_me(): #there are no args or options yet. 
		#use stdout because this will be run as cron job eventually
		#(wait isn't print() in 3.x stdout?)
		print('Hello There!', end="")