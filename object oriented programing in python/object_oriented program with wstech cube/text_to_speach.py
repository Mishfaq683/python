import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty("rate", 150)  # Speed of speech (words per minute)
engine.setProperty("volume", 1)  # Volume (0.0 to 1.0)

# Speak the text
text = "Hello!  my name ishfaq marwat so im exciting to the new project with the text to speech in  pyttsx3"
engine.say(text)

# Wait for speech to finish
engine.runAndWait()
# import pyttsx3
# import pdfplumber

# # Open the PDF file
# pdf_file = r"d:\BS all book\python book  ref by Naveed Abbas.pdf" # the full path of the files location or the  \\
# engine = pyttsx3.init()
# engine.setProperty("rate",800)
# engine.setProperty("volume",10)

# with pdfplumber.open(pdf_file) as pdf:
#     for page in pdf.pages:
#         text = page.extract_text()  # Extract text
#         if text:
#             print(f"Reading page {pdf.pages.index(page) + 1}...")
#             engine.say(text)
#             engine.runAndWait()


# import pyttsx3
# # the text convert  into speach 
# # intialzing  
# engine=pyttsx3.init()
# # set the value 
# engine.setProperty("rate",300)

# engine.setProperty("volume",1)

# voice = engine.getProperty("voice")
# engine.setProperty("voice",voice[1].id)
# engine.say("i,am exciting in the new about project !")
# engine.runAndWait()
# import pyttsx3

# # Initialize the text-to-speech engine
# engine = pyttsx3.init()

# # Set speech rate (default is around 200, 300 is fast)
# engine.setProperty("rate", 200)  # Adjust speed

# # Set volume (value must be between 0.0 and 1.0)
# engine.setProperty("volume", 1.0)  # 1.0 is the maximum volume

# # Get available voices
# voices = engine.getProperty("voices")  # Get list of voices

# # Set a different voice (Male: voices[0], Female: voices[1])
# engine.setProperty("voice", voices[1].id)  # Change to female voice

# # Speak the text
# engine.say("I am excited about the new project!")

# # Run the engine
# engine.runAndWait()
# import pyttsx3

# # Initialize the text-to-speech engine
# engine = pyttsx3.init()

# # Set speech rate (default is around 200, 300 is fast)
# engine.setProperty("rate", 200)  # Adjust speed

# # Set volume (value must be between 0.0 and 1.0)
# engine.setProperty("volume", 1.0)  # 1.0 is the maximum volume

# # Get available voices
# voices = engine.getProperty("voices")  # Get list of voices

# # Set a different voice (Male: voices[0], Female: voices[1])
# engine.setProperty("voice", voices[0].id)  # Change to female voice

# # Speak the text
# text="I am excited about the new project!"
# engine.say(text)

# # Run the engine
# engine.runAndWait()
# import pyttsx3
# engine=pyttsx3.init()
# engine.setProperty("rate",150)
# engine.setProperty("volume",1.0)
# voices = engine.getProperty ("voices")
# engine.setProperty("voices",voices[0].id)
# text="hello! my name is ishfaq marwat my first project in python"
# engine.say(text)
# engine.runAndWait()

# import pyttsx3
# import pdfplumber

# files_open=r"d:\BS all book\Eric_Matthes_Python_Crash_Course_A_Hands.pdf"


# engine=pyttsx3.init()

# engine.setProperty("rate",150)

# engine.setProperty("volume",50)
# with pdfplumber.open(files_open) as pdf:
#     for page in pdf.pages:
#         text=page.extract_text()
#         if text:
#             print(f"the reading of page{pdf.pages.index(page)+1 }")
# engine.say(text)


# engine.runAndWait()
# import pyttsx3
# import pdfplumber

# # Correct file path
# files_open = r"d:\BS all book\Eric_Matthes_Python_Crash_Course_A_Hands.pdf"

# # Initialize the text-to-speech engine
# engine = pyttsx3.init()

# # Set speech properties
# engine.setProperty("rate", 150)  # Speed of speech
# engine.setProperty("volume", 1.0)  # Volume (must be between 0.0 and 1.0)

# # Open and read the PDF
# with pdfplumber.open(files_open) as pdf:
#     for page_num, page in enumerate(pdf.pages, start=1):  # Correct page indexing
#         text = page.extract_text()
#         if text and text.strip():  # Ensure the text is not None or empty
#             print(f"Reading page {page_num}...")  # Show reading progress
#             engine.say(text)  # Speak the extracted text

# # Run the speech engine
# engine.runAndWait()
# import pdfplumber
# from gtts import gTTS

# # 📌 Step 1: Open the PDF and Extract Text
# pdf_file = r"d:\BS all book\Eric_Matthes_Python_Crash_Course_A_Hands.pdf"
# text = ""


# with pdfplumber.open(pdf_file) as pdf:
#     for page in pdf.pages:
#         page_text = page.extract_text()
#         if page_text:  # Avoid empty pages
#             text += page_text + "\n"  # Append text with a newline

# # 📌 Step 2: Convert Extracted Text to Speech
# if text.strip():  # Ensure there is text to convert
#     tts = gTTS(text=text, lang="en")  # Convert text to speech
#     mp3_filename = "output.mp3"  # Save as MP3 file
#     tts.save(mp3_filename)  # Save the audio file
#     print(f"MP3 file saved as: {mp3_filename}")
# else:
#     print("No text found in the PDF.")
# import os
# # os.system("start output.mp3")  # Opens the MP3 file
# import pyttsx3

# engine = pyttsx3.init()
# engine.setProperty("rate",150)
# # Save speech to a WAV file
# engine.save_to_file("Hello, i,m ishfaq marwat my first project in text convert into the text the MP3 file.", "output.wav")
# engine.runAndWait()

# print("WAV file saved as output.wav")

# import os
# os.system("start output.mp3")  # Opens the MP3 file
