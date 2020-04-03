import requests
import os

duration = 0.1  # seconds
freq = 60000  # Hz

def rec_link():
    try:
        response = requests.get('https://api.github.com')
        var = response.status_code
        print(var)
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
    except Exception as Error:
        raise Error

rec_link()