# pyRadio
Radio API which plays audio from youtube videos from a queue of requests. To run, simply execute `run.sh` (it's a bash script).

## Details
This server runs through 3 _main_ threads:
1. API Thread: receives requests and create minor worker threads, which handle the requests and forward to the player controller thread;
2. Player Controller Thread: manages the queue and sends the video requests to the player thread;
3. Player Thread: resolves the youtube URL to an audio stream url, calls google translate as a TTS interface to say what is being played and who requested it, and calls vlc to play the audio stream url.

In the current version, a new player thread is created every time a video is played, and then it is closed at the end of the video. Currently working on improving this behaviour.

While running, the API thread receives POST requests at `localhost:5000/radio`. The requests should have `content-type: application/json` as a header and a json as the following example:
```json
{
    "url": "https://www.youtube.com/watch?v=NY0ffyEu6uo",
    "requester": "Anon"
}
```
A simple form for requests may be included in future commits.

## Requirements
Requires python3 and uses pip3 to install most dependencies. Requires an installation of VLC, which is used for the audio playback.
