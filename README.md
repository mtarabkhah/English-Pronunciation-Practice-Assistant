# English Pronunciation Practice Assistant

This Python script is designed to help you improve your English pronunciation. It works by displaying lines of text from a file and prompting you to read them out loud. The script then uses speech recognition technology to transcribe your spoken words and compare them with the original text. If you mispronounce any words, the script will give a score to your pronunciation and then display the word and provide the correct pronunciation.

## Requirements

- Python 3.x
- PyAudio
- SpeechRecognition
- pyttsx3

## Installation

1. Clone or download the repository.
2. Install the required packages by running `pip install -r requirements.txt` in your terminal.

## Usage

1. Place the text file you want to practice with in the same directory as the script and name it as `SourceText.txt`.
2. Run the script by executing `python english_pronunciation_practice.py` in your terminal.
3. Follow the prompts to read each line of text and receive feedback on your pronunciation.
4. The script will provide a score for your pronunciation at the end of each line. The score is calculated as the percentage of correctly pronounced words out of the total number of words in the line.

## Tips

- Make sure you are in a quiet environment and speak clearly into your microphone.
- Adjust the value in `duration = 2` for the `adjust_for_ambient_noise` in the script to optimize speech recognition for your microphone and voice.
- You can modify the `SourceText.txt` text file to practice with different materials.

## Contributing

If you find any bugs or have suggestions for new features, please submit an issue or pull request on GitHub.