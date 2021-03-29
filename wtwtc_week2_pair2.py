class Event(object):
	def __init__(self,date,name,location='',description=''):
		# Set class properties here.
		self.events ={}
		self.events[date] = {}
		self.events[date]['name']=name
		self.events[date]['location']=location
		self.events[date]['description']=description

	def listevents(self, date):
		# Format a string of event information to return
		if date in self.events:
			print(self.events[date]['name'])
	
	def getEventInfo(self,name):
		# print out information of an event by giving the event's name.
		for date in self.events:
			#print(self.events[date])
			if name == self.events[date]['name']:
				print('Date: ', date.strftime("%b %d %Y"))
				print('Name: ', self.events[date]['name'])
				print('Location: ', self.events[date]['location'])
				print('Description: ', self.events[date]['description'])


