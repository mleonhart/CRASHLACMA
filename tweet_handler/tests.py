from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from django.core.management import call_command

from tweet_handler.management.commands import gettwitterfeed

#http://chimera.labs.oreilly.com/books/1230000000393/ch14.html#_solution_226
#http://www.obeythetestinggoat.com/how-to-log-exceptions-to-stderr-in-django.html
#http://stackoverflow.com/questions/22571320/can-django-manage-py-custom-commands-return-a-value-how-or-why-not

class TestCustomMangementScriptStdout(TestCase):
	def test_message_gets_to_stdout(self):
		expected_message = 'Hello There!\n'
		actual_message = StringIO()
		call_command('gettwitterfeed', stdout=actual_message)
		self.assertEqual(actual_message.getvalue(), expected_message)
		
class TestMessageCustomMangementScriptClassFunctionPrint(TestCase):
    def test_message_gets_to_stdout(self):
        expected_message = 'Hello There!'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            gettwitterfeed.Command.test_me()
            self.assertEqual(fake_out.getvalue(), expected_message)