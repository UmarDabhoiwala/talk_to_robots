# AI Chatbot Program

This program uses machine learning with the OpenAI and ElevenLabs API to allow users to talk with an AI chatbot through talking. The chatbot uses natural language processing and machine learning algorithms to understand and respond to user input in a conversational manner.
Installation

To use this program, you will need to have Python 3 installed on your computer. You can download Python from the official Python website.

You will also need to install the following Python packages:

    openai: for accessing the OpenAI API
    pyaudio: for capturing audio input from the user
    playsound: for playing back the chatbot's speech output
    requests: for making HTTP requests to the ElevenLabs API
    halo: for the loading spinners
    wave: for saving the audio files 

You can install these packages using the following command:

    pip install openai pyaudio wave playsound requests halo

Note that the pyaudio package may require additional installation steps on some systems. Please refer to the pyaudio documentation for more information.

## Usage

To use the AI chatbot program, simply run the main.py file using Python:

    python3 main.py

The program will launch and prompt you to speak a message to the chatbot. After speaking your message, the program will transcribe it using OpenAI's Whisper and send it to the OpenAI API for processing with the ChatGPT. ChatGPT will respond to the message and then send the response to ElevenLabs for conversion to Audio.

You can specify the number of messages in the conversation or make it infinite (A Really Large Number). Messages are all added to history so the chatbot remembers the context. Be careful though as the OpenAI api counts the number of input tokens as price so aim to keep things short to be cheap 

## Configuration

Before running the program, you will need to configure your OpenAI and ElevenLabs API keys. The program will prompt you in the terminal to add these if they aren't set before hand. 

Alternatively, you can modify the config.py file to include your API keys directly:

    OPENAI_API_KEY = "<YOUR_OPENAI_API_KEY>"
    ELEVENLABS_API_KEY = "<YOUR_ELEVENLABS_API_KEY>"

## Contributing

This program is open source and contributions are welcome. If you find a bug or have a suggestion for a new feature, please open an issue on the project's GitHub repository. If you would like to contribute code, please submit a pull request with your changes.
License

