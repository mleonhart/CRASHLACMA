from io import StringIO
from unittest import TestCase
from unittest.mock import patch


from tweet_handler.management.commands import gettwitterfeed

#http://chimera.labs.oreilly.com/books/1230000000393/ch14.html#_solution_226
#other options
#http://www.obeythetestinggoat.com/how-to-log-exceptions-to-stderr-in-django.html

class TestMessagePrint(TestCase):
    def test_message_gets_to_stdout(self):
        expected_message = 'Hello There!'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            gettwitterfeed.Command.test_me()
            self.assertEqual(fake_out.getvalue(), expected_message)