# Fetch the function *sleep*
from time import sleep

def get_bool(prompt):
   try:
      return {"true":True,"false":False}[input(prompt).lower()]
   except KeyError:
      print "Only enter true or false..."

print "Please get ready for party. (I'll be back in 3 minutes.)"

# Wait for 3 minutes (that is, 3*60 seconds)...
sleep(18)

print "I'm baaack :)"


ready = get_bool("Are you done? ")
while not ready:
    print "OK... I'll be back after 30 seconds..."
    sleep(3)
    ready = input("Are you done? ")

print ":) Let's get going..."