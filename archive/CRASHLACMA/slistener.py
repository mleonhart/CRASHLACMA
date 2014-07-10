from tweepy import StreamListener
import json, time, sys

class SListener(StreamListener):

    def __init__(self, api = None, fprefix = 'streamer'):
        self.api = api or API()
        self.filecounter = 1
        self.fprefix = fprefix
        
    def on_data(self, data):

        if  'in_reply_to_status' in data:
            self.on_status(data)
        elif 'delete' in data:
            delete = json.loads(data)['delete']['status']
            if self.on_delete(delete['id'], delete['user_id']) is False:
                return False
        elif 'limit' in data:
            if self.on_limit(json.loads(data)['limit']['track']) is False:
                return False
        elif 'warning' in data:
            warning = json.loads(data)['warnings']
            print warning['message']
            return false

    def on_status(self, status):
        

        filename = self.fprefix + '.' + time.strftime('%Y%m%d-%H%M') + '_' + str(self.filecounter) + '.json'

        self.output = open(filename, 'wb')
        print('Writing to file %s') % filename
        self.output.write(status + "\n")
        self.filecounter += 1
        self.output.close()

        return

