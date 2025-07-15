from django.shortcuts import render
from gtts import gTTS
import os

def cartoon_view(request):
    story_text = ''
    audio_file = ''

    try:
        with open('story.txt', 'r') as f:
            story_text = f.read()
            tts = gTTS(text=story_text, lang='en')
            audio_file = 'media/sample_audio.mp3'
            tts.save(audio_file)
    except:
        story_text = 'Story not found or audio generation failed.'

    return render(request, 'cartoon.html', {
        'story': story_text,
        'audio_path': '/' + audio_file
    })
