import speech_recognition as sr
import pyttsx3 
import pyaudio
  
r = sr.Recognizer() 
print("Speak Now:")
# creating a function to convert text to speech
def SpeakText(command):
    
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()
      
# Looping for the user to speak
  
while(1):    
      
    try:
          
        # Enabling the microphone to accept sound
        rr = sr.Microphone(device_index=1)
        with rr as source13:
              
            # adjusting surrounding noise level 
            r.adjust_for_ambient_noise(source13, duration=0.2)
            
            audio2 = r.listen(source13)
              
            # Using google's audio recognition system to recognize audio and convert it to text
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
  
            # Confirm with the user whether the converted text is error-free
            print("Did you say "+MyText)
            SpeakText(MyText)
              
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
          
    except sr.UnknownValueError:
        print("unknown error occured")
