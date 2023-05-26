# English Pronunciation Practice Assistant

This Python script is designed to help you improve your English pronunciation. It works by displaying lines of text from a file or user input and prompting you to listen or read them out loud. The script uses speech recognition technology to transcribe your spoken words and compares them with the original text. If you mispronounce any words, the script provides correct pronunciation and gives a score to your pronunciation.

## Requirements

- Python 3.x
- PyAudio
- SpeechRecognition
- pyttsx3
- gTTS

## Installation

1. Clone or download the repository.
2. Install the required packages by running `pip install -r requirements.txt` in your terminal.

## Usage

1. Put the text you want to practice in a text file and save it on your systems, preferably within the same directory as the script.
2. Run the script by executing `python english_pronunciation_practice.py` in your terminal or run the GUI version by executing `python english_pronunciation_practice_gui.py`.
3. Provide the path to the file using the "Select File" button or you can manually enter the path in the "Source File" input field in the GUI.
4. Choose your preferred settings and select the pronunciation practice level:
   - **Level 1**: The text will be read line by line for you, and you don't have to read or repeat.
   - **Level 2**: The text will be displayed line by line, and you have to read it. The script provides a score for your pronunciation at the end of each line. Mispronounced words will be highlighted in the "Source Text" field and played for you.
   - **Level 3**: Similar to Level 2, but you have to read and repeat the mispronounced words until you pronounce them correctly.
   - **Level 4**: Similar to Level 2, but you have to read the entire text again until you pronounce it correctly.
5. The script provides a score for your pronunciation based on the percentage of correctly pronounced words out of the total number of words in each line.
6. You can choose between two options for text-to-speech conversion:
   - **Offline Player**: Uses the "pyttsx3" library and offers four different player speed options: "Very Slow", "Slow", "Normal", and "Fast".
   - **Online Player**: Uses the "gTTS" library and provides two player speed options: "Slow" and "Normal". Additionally, you can choose from four different accents: British, American, Irish, and Indian.
7. You can adjust the player speed and accent settings in the GUI. Use the "Test Voice" button to listen to a sample text and change the settings if needed.
8. The "Clear Form" button resets the GUI and clears all the texts and selections in the widgets.
9. The "Select File" button opens a file dialog for you to choose a text file to practice with. Alternatively, you can manually type or paste the file path into the "Source File" input field.
10. Hover your mouse over the radio buttons in the "Choose your player" and "Choose desired assist" sections to view helpful tips for each option.

## Ideas for Improvement

- Add "Pause" and "Stop" options to give more control to the user during the pronunciation practice.
- Implement checks for the existence of a text file in the provided path before attempting to read it.
- Allow the user to type or paste text directly into the "Source Text" field for practice, instead of relying only on file input.
- Add the option of providing a short definition for the mispronounced words

## Contributing

If you find any bugs or have suggestions for

 new features, please submit an issue or pull request on GitHub.

Please feel free to make any further modifications to the README file based on your specific implementation details and preferences.