#!/usr/bin/env python

# source: https://www.geeksforgeeks.org/python-reading-contents-of-pdf-using-ocr-optical-character-recognition/

# Tested in Linux Ubuntu
# installed tesseract-ocr-spa for Spanish language

#%%
from pdf2image import convert_from_path
from PIL import Image
from tempfile import TemporaryDirectory
import pytesseract

pdf_file = "example.pdf"

# output text file
text_file = "{}-text.txt".format(pdf_file)

# %%
with TemporaryDirectory() as tempdir:
    print(tempdir)

    # Read in the PDF file into images at a high DPI
    pdf_pages = convert_from_path(pdf_file,
                                  400, #DPI resolution
                                  output_folder=tempdir)

    with open(text_file, "a") as output_file:
        for page in pdf_pages:

            print(page.filename)
            # Recognize the text as string in image using pytesserct
            text = str(((pytesseract.image_to_string(page,
                                                     lang="spa"))))

            # The recognized text is stored in variable text
            # Any string processing may be applied on text
            # Here, basic formatting has been done:
            # In many PDFs, at line ending, if a word can't
            # be written fully, a 'hyphen' is added.
            # The rest of the word is written in the next line
            # Eg: This is a sample text this word here GeeksF-
            # orGeeks is half on first line, remaining on next.
            # To remove this, we replace every '-\n' to ''.
            text = text.replace("-\n", "")

            output_file.write(text)
