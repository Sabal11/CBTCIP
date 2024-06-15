import sounddevice as sd
import wave

# Parameters
CHANNELS = 1
RATE = 44100
DURATION = 10  # seconds
OUTPUT_FILENAME = r"C:\Users\HP\Desktop\recording.wav"

print("Recording...")
audio_data = sd.rec(int(DURATION * RATE), samplerate=RATE, channels=CHANNELS, dtype='int16')
sd.wait()
print("Recording finished.")

try:
    with wave.open(OUTPUT_FILENAME, 'w') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2)  # 2 bytes for int16
        wf.setframerate(RATE)
        wf.writeframes(audio_data.tobytes())
    print(f"File saved successfully at {OUTPUT_FILENAME}")
except Exception as e:
    print(f"Error saving file: {e}")