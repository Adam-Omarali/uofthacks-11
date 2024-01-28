from flask import Flask, request, jsonify
import os
from img_to_text import get_image_description, get_narraration, generate, save, Voice, VoiceSettings

app = Flask(__name__)

@app.route('/process-image', methods=['POST'])
def process_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Save the file temporarily
    filepath = 'temp_image.jpg'
    file.save(filepath)

    # Use your existing functions
    desc = get_image_description(filepath)
    narration = get_narraration(desc)

    voice = generate(
        text=narration[12:],
        voice=Voice(
            voice_id='GEM8FZRZ0Q7qZPaI8pju',
            settings=VoiceSettings(stability=0.3, similarity_boost=0.5, style=0.25, use_speaker_boost=True)
        )
    )

    audio_file_path = './audio/generated_audio.mp3'
    save(voice, audio_file_path)

    # Remove the temporary file if necessary
    os.remove(filepath)

    return jsonify({'audio_path': audio_file_path})

if __name__ == '__main__':
    app.run(debug=True)
