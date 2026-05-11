import asyncio
import edge_tts
import io
import pygame

async def play_emotional_speech(ssml):
    VOICE = "en-US-JennyNeural"
    # Wrap your text in SSML for the emotion

    communicate = edge_tts.Communicate(ssml, VOICE)
    
    # Collect chunks into a byte buffer
    audio_data = b""
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_data += chunk["data"]

    # Play the bytes using Pygame
    pygame.mixer.init()
    audio_stream = io.BytesIO(audio_data)
    pygame.mixer.music.load(audio_stream)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

if __name__ == "__main__":
    asyncio.run(play_emotional_speech(f"""The sun had just begun to dip below the horizon, painting the sky in vibrant shades of orange and deep purple. A gentle breeze rustled through the autumn leaves, creating a soft, rhythmic crunching sound that echoed down the empty street. Somewhere in the distance, a lone dog barked, signaling the end of a long day and the quiet arrival of the evening. It was one of those rare moments where everything felt perfectly still, as if the world were holding its breath just to enjoy the fading light."""))
