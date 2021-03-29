########################################################
# WTW to Code Session 2 Week 3 Pair Project
########################################################

# TODO Import your event module
import wtwtc_week2_pair2 as wt
from datetime import datetime
####################################################
# TODO Make these functions work
def addEvent():
  print('adding event')
  # Name: 'Lunch Meeting'
  name =input()
  # Date: '2015-04-01'
  date = datetime.strptime(input(), '%Y-%m-%d')
  # Location: 'Beta C Cafe'
  location =input()
  # Description: 'Go over the offsite event for next month with Susan.'
  description =input()
  # Event Added.
  event = wt.Event(date,name,location,description)
  calendar.append(event)
  #event.getEventInfo()

def listEvents():
  print('listing events')
  dt = datetime.strptime(input(), '%Y-%m-%d')
  for e in calendar:
    e.listevents(dt)
  
def displayEventInfo():
  print('event info here')
  name =input()
  print(name)
  #print(calendar)
  for e in calendar:
    e.getEventInfo(name)

####################################################
intro_prompt = 'Welcome to Event Calendar:\n'
options = {
	'add': 'add an event',
	'list': 'list events for a date',
	'info': 'see information on an event',
	'quit': 'quit the program'
}

options_prompt = ''
for (option, description) in sorted(options.items()):
	options_prompt += '\t' + option + ': ' + description + '\n'

prompt = intro_prompt + options_prompt
calendar = []

keep_running = True

while keep_running:
  # Get what the user wants to do
  raw_action = raw_input(prompt)
  action = (raw_action.strip()).lower()

  # Add an event
  if action == 'add':
    addEvent()

  # List events for a date
  elif action == 'list':
    listEvents()

  # See information on an event
  elif action == 'info':
    displayEventInfo()

  # User wants to leave
  elif action == 'quit':
    print('Goodbye!')
    break

  # User types something that is not supported
  else:
    print('I don\'t know what you mean.')

  print('') # Add an extra line of space for readability
