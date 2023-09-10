# Johanes de Britto Krisna Arianta
# 21/473893/TK/52247
# NLP 1st Assignment

# Bengkel Bot - Garage Virtual Assistant

# Libraries
import re
import random
import webbrowser
import threading

def flat_tire_web():
    url = "https://www.wikihow.com/Change-a-Tire"
    webbrowser.open(url)

def wiper_fluid():
    url = "https://www.wikihow.com/Add-Windshield-Washer-Fluid-to-Your-Vehicle"
    webbrowser.open(url)

def jump_start():
    url = "https://www.wikihow.com/Jump-Start-a-Car"
    webbrowser.open(url)

def check_oil_leak():
    url = "https://www.wikihow.life/Know-if-Your-Car-Has-a-Fluid-Leak"
    webbrowser.open(url)

def change_lamp():
    url = "https://www.wikihow.com/Fix-a-Burned-Out-Headlight"
    webbrowser.open(url)

def radiator_fluid():
    url = "https://www.wikihow.com/Check-and-Add-Radiator-Fluid"
    webbrowser.open(url)

def maps_bengkel():
    url = "https://www.google.com/maps/search/Bengkel+Mobil+Terdekat/@-7.7998902,110.3493258,12z?entry=ttu"
    webbrowser.open(url)

# Dictionary
patterns = [
    (r'.*(engine.*not.*start).*', ["In this case you can jump-start with cables and a working vehicle", "You can use our service to inspect the starter motor and replace it", "If you can, replace the battery"]),
    (r'.*(engine.*overheat|overheat).*', ["Okay, you should regularly check coolant levels", "Well, You should avoid prolonged idling in hot weather"]),
    (r'.*(knock|ping).*', ["Well, You should adhere to the recommended octane level", "Oops, it seems like you don't follow proper maintenance schedules"]),
    (r'.*(oil.*leak).*', ["Hmm, you should regularly check your oil level", "Well, you should consult our mechanic to fix the leaks promptly"]),
    (r'.*engine.*', ["Okay, what is the problem with your engine?", "Tell me more about the engine problem", "Is the engine not working properly?"]),

    (r'.*(flat.*tire.*web|web.*flat.*tire).*', [flat_tire_web]),
    (r'.*(garage.*map).*', [maps_bengkel]),
    (r'.*(steer.*wheel|car.*not.*straight).*', ["It looks like a problem with your tire, you need to get wheels alignment", "You should take our wheel alignment service"]),
    (r'.*(tire.*flat|flat.*tire).*', ["Okay, you can try changing into the spare tire", "To prevent danger conditions, it's better to get the tire replaced"]), 
    (r'.*tire.*', ["Okay, what happened with you tire?", "Tell me more about your tire."]),
    
    (r'.*(wiper.*fluid.*web|web.*wiper.*fluid).*', [wiper_fluid]),
    (r'.*(change.*battery.*web|web.*change.*battery|web.*jump.*start).*', [jump_start]),
    (r'.*(check.*oil.*leak.*web|web.*oil.*leak).*', [check_oil_leak]),
    (r'.*(change.*light.*web|web.*change.*light).*', [change_lamp]),
    (r'.*(radiator.*web|web.*radiator).*', [radiator_fluid]),
    (r'.*(light.*not.*function).*', ["Check the bulb", "Try to replace broken bulbs", "Well, you can use our bulb replacement service"]),
    (r'.*battery.*', ["What happened?", "Is your car can't be started?", "Anything wrong with the lights?"]),
    
    (r'^(hey|hello|hi).*', ["Hello, how may I help you?", "Hey, what is your car's problem?"]),
    (r'.*(thanks|thank).*', ["Your welcome, anything else?", "No problem, happy to help you! Anything else?", "My pleasure, anything else?"]),
    (r'.*', ["Well, Can you elaborate on that?", "Can you go more specific?", "What are you trying to say?"])

    
    
]

# Chatbot responses function
def chatbot_response(user):
    for keyword, botresponses in patterns:
        if re.search(keyword, user, re.IGNORECASE):
            if callable(botresponses[0]):
                thread = threading.Thread(target=botresponses[0])
                thread.start()
                return []
            else:
                return botresponses

# Start chat function
def start_chat():
    print("Hey! I'm Your Garage Virtual Assistant")
    print("Type 'exit' to end this conversation.")

# Loop chat function
def loop_chat():
    start_chat()
    while True:
        user = input("You: ").lower()
        if user in ['no', 'no thanks', 'no thank you', 'exit', 'nope']:
            print("Bengkel Bot: Good bye! I hope your problem(s) are solved!")
            break
        response = chatbot_response(user)
        if response:
            print("Bengkel Bot:", random.choice(response))
        else:
            print("Bengkel Bot: Hold tight! I'm surfing the net...")

# Main code
loop_chat()
