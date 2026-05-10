# Vosk Setup Guide for ILLI HUD Dashboard
# Created by: Muhammad Farhan
# Email: farhanhomeschooling519@gmail.com

## Overview
This guide helps you set up Vosk for offline speech recognition in the ILLI HUD Dashboard.

## Step 1: Install Dependencies
```bash
pip install vosk
pip install pyaudio
pip install sounddevice
pip install numpy
```

## Step 2: Download Vosk Model
Download a Vosk model for your language:

### English Models:
- Small (50MB): https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
- Medium (150MB): https://alphacephei.com/vosk/models/vosk-model-en-us-0.15.zip
- Large (1.8GB): https://alphacephei.com/vosk/models/vosk-model-en-us-0.15.zip

### Other Languages:
Visit: https://alphacephei.com/vosk/models/

## Step 3: Extract Model
1. Download the model zip file
2. Extract to a folder (e.g., `vosk-model-en-us`)
3. Place the folder in your project directory

## Step 4: Update Dashboard Code
In `illi_hud_dashboard.py`, update the Vosk model path:

```python
# Replace this line:
model_path = "path/to/your/vosk-model"

# With your actual model path:
model_path = "g:/Virtual Assistant/vosk-model-en-us"
```

## Step 5: Test Microphone
Test your microphone with this simple script:

```python
import vosk
import pyaudio
import json

# Load model
model = vosk.Model("vosk-model-en-us")
recognizer = vosk.KaldiRecognizer(model, 16000)

# Start microphone
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

print("Listening...")

try:
    while True:
        data = stream.read(4000)
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            print(f"You said: {result['text']}")
except KeyboardInterrupt:
    print("Stopping...")
finally:
    stream.stop_stream()
    p.terminate()
```

## Step 6: Run Dashboard
```bash
python illi_hud_dashboard.py
```

## Troubleshooting

### Microphone Not Working:
1. Check microphone permissions
2. Try different microphone index
3. Install audio drivers

### Model Not Loading:
1. Verify model path is correct
2. Ensure model is fully extracted
3. Check model compatibility

### Performance Issues:
1. Use smaller model for faster recognition
2. Adjust audio buffer size
3. Close other audio applications

## Advanced Configuration

### Custom Wake Word:
Add wake word detection to reduce false positives.

### Multiple Languages:
Download models for different languages and switch between them.

### Custom Commands:
Add custom voice commands in the process_command function.

## Model Recommendations

### For Testing:
- Small model (50MB) - Fast, less accurate

### For Production:
- Medium model (150MB) - Good balance of speed and accuracy

### For Best Accuracy:
- Large model (1.8GB) - Slower, most accurate

## Audio Settings

### Optimal Settings:
- Sample Rate: 16000 Hz
- Channels: 1 (mono)
- Format: 16-bit PCM
- Buffer Size: 4000 samples

### Microphone Placement:
- Keep microphone 6-12 inches away
- Reduce background noise
- Use directional microphone if possible

## Integration with ILLI

The dashboard includes:
- Voice command processing
- Text-to-speech responses
- System integration
- Modular command system

## Support

For issues:
1. Check Vosk documentation: https://alphacephei.com/vosk/
2. Review audio setup
3. Test with different models
4. Check system permissions

## Future Enhancements

Planned features:
- Wake word detection
- Noise cancellation
- Multiple language support
- Custom vocabulary training
- Real-time transcription
