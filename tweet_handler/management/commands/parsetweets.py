# fetches raw tweet json 
# confirms media exists
#		(throws error? tweets back? what does it do with the tweet data?)
# creates a scrubbed_text field to look for address
# saves info to DB (see models.py, there is a field that is of type image..., maybe just save the media URL at this point?)
# archives or destroys json file?