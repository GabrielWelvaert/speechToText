import speech_recognition as sr
import os

class SpeechToText:
    def process(self):

        absoluteFilePath = input("Enter absolute filepath of directory containing files for translation: ")
        open('output.txt','w').close()

        success = 0
        failure = 0

        # Iterate over the files
        try:
            files = os.listdir(absoluteFilePath)
        except Exception  as e:
            print(f'Error: {e}')
            exit(1)

        for file in files:

            absoluteFile = os.path.join(absoluteFilePath, file)

            with sr.AudioFile(absoluteFile) as source:
                audio = sr.Recognizer().record(source)

            with open('output.txt', 'a') as f:

                #translating audio file to text
                try:
                    f.write(f"{sr.Recognizer().recognize_google(audio)} = {file}\n")
                    success += 1
                    print(f'{file} translated "successfully" by google')

                #uninterpretable audio files are matched with "ERROR"; occurs for things like screaming or grunting
                except sr.UnknownValueError:
                    f.write(f"ERROR = {file}\n")
                    failure += 1
                    print(f'{file} translated "unsuccessfully" by google')

            f.close()

        successrate = ((len(files)-failure)/len(files))*100
        if success == failure == 0:
            successrate = 0

        print(f"Task complete with {success} files translated ({successrate}% success rate). See output.txt for full translation.")


if __name__ == "__main__":
    instace = SpeechToText()
    instace.process()
