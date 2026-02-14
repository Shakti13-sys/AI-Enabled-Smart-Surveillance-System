import winsound
import os
import time

_last_played = 0

def play_alert():
    global _last_played
    now = time.time()

    if now - _last_played < 2:   # cooldown
        return

    sound_path = os.path.join(
        os.path.dirname(__file__),
        "alert.wav"
    )

    winsound.PlaySound(
        sound_path,
        winsound.SND_FILENAME | winsound.SND_ASYNC
    )

    _last_played = now
