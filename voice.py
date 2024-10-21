from tkinter import *
from gtts import gTTS
import playsound

def generate_voice():
    user_text = text_field.get("1.0", "end").strip()
    
    if user_text:
        tts = gTTS(text=user_text, lang='en')
        tts.save("output.mp3")
        playsound.playsound("output.mp3")
        status_label.config(text="Voice recorded!")
    else:
        status_label.config(text="Please enter a message.")


root = Tk()
root.title("Voice Recorder")
root.geometry("300x150")


text_field = Text(root, height=4, width=30)
text_field.pack(pady=10)

Button(root, text="Generate Voice", command=generate_voice).pack(pady=5)


status_label = Label(root, text="")
status_label.pack(pady=10)

root.mainloop()
