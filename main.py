from audio_to_chat import run_chat
from choicer import get_choicer
import config
from api_fiddler import fiddle_with_api_keys

def main(): 
    
    if config.OPENAI_API_KEY == "<YOUR_OPENAI_API_KEY>" or config.ELEVENLABS_API_KEY == "<YOUR_ELEVENLABS_API_KEY>":
        fiddle_with_api_keys()
    
    try:
        duration_of_recording, number_of_responses, choice = get_choicer()
        transcript = run_chat(duration_of_recording, number_of_responses, choice)
    except Exception as e:
        print("Something went wrong")
        print(e)
        
    with open("transcript.txt", "w") as f:
        f.write(transcript)

if __name__ == "__main__":
    main()