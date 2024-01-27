from elevenlabs import generate, play, set_api_key, save, Voice, VoiceSettings
set_api_key("0a25b0d39eeab112228d8ebd735425f1")

voice = generate(
    text="The photo depicts two individuals posing closely together for a selfie. The person on the left appears to be drinking from a yellow can, wearing glasses and a fluffy, light-colored jacket with a lanyard that reads 'University of'. They have curly hair with lighter-colored tips. The person on the right is holding a clear plastic container that seems to contain a brownie or a similar dessert. They have short black hair and are wearing a black shirt. The background is nondescript, likely indoors with artificial lighting. Both are smiling and appear to be enjoying the moment.",
    voice= Voice(
        voice_id = 'GEM8FZRZ0Q7qZPaI8pju',
        settings=VoiceSettings(stability=0.3, similarity_boost=0.5, style=0.25, use_speaker_boost=True)
    )
)
save(voice,'test.wav')