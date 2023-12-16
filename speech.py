import pyttsx3
import sys

print('I use the pyttsx3 module. Thank you for using this ebook reader.')
print('Welcome to the ebook reader.')

# Check if the necessary command-line arguments are provided
if len(sys.argv) < 2:
    print('To run the command, use: python3 speech.py file.pdf')
    print('Replace "file.pdf" with the name of the PDF file you want to read.')
    sys.exit(1)

# Initialize the text-to-speech engine
engine = pyttsx3.init()

print('You can adjust the read speed from 100 to 200 (recommended).')
speedInt = int(input('Enter your desired reading speed: '))

# Get the list of available voices
voices = engine.getProperty('voices')

# Ask the user for a voice preference (male or female)
user_choice = input('Do you prefer a male or female voice? ').lower()

# Find the preferred voice
voice_to_use = None
for voice in voices:
    if user_choice in voice.name.lower():
        voice_to_use = voice
        break

# Set the preferred voice if found
if voice_to_use:
    engine.setProperty('voice', voice_to_use.id)
else:
    print('No matching voices found.')

# Read the content of the specified file
with open(sys.argv[1], 'r') as myfile:
    text = myfile.read()

    # Set the reading speed
    engine.setProperty('rate', speedInt)

    # Read the text from the file
    engine.say(text)
    engine.say('Thank you for listening.')
    engine.runAndWait()
