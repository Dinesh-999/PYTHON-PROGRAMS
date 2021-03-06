# reading pdf
# making audio book extract text and make audio file
# pdf to audio
# make sure that sample.pdf file in same folder
# or keep th different pdf and rename in th program
# neuralnine


import pyttsx3
import PyPDF2

with open("sample.pdf", "rb") as book:
    full_text = ""
    reader = PyPDF2.PdfFileReader(book)
    audio_reader = pyttsx3.init()
    audio_reader.setProperty("rate", 100)
    for page in range(reader.numPages):
        next_page = reader.getPage(page)
        content = next_page.extractText()
        full_text += content

    audio_reader.save_to_file(full_text, "myaudiobook.mp3")
    audio_reader.runAndWait()