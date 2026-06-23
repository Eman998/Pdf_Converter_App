# Image to PDF Converter Application

A modern, free desktop application built with Python that allows users to convert multiple images (JPG, JPEG, PNG) into a single, compiled PDF file.

## Features
* Modern User Interface using CustomTkinter
* Multiple image selection (Hold Ctrl/Cmd)
* Free and ad free downloads
* Local processing for 100% privacy and zero costs

## Resources & Documentation Used
While building this project, the following documentation and tutorials were incredibly helpful:
* [W3Schools Python Tutorial](https://www.w3schools.com/python/) - Used for basic Python loops and list methods (`.extend()`).
* [CustomTkinter Documentation](https://customtkinter.tuxpython.org/) - Used for styling the dark-mode buttons, textboxes, and window scaling.
* [Pillow (PIL) Documentation](https://pillow.readthedocs.io/) - Used for the `.convert("RGB")` and `.save()` image processing features.
* [Python tkinter.filedialog](https://docs.python.org/3/library/dialog.html) - Used for the native file exploration popups.

## Why I Built This (The Backstory)
Sometimes we ignore the basic, repetitive things in life without realizing how much time they waste. Before building this application, I used to do something incredibly tedious (I swear, this was my actual workflow): 

1. I would send raw images to myself on WhatsApp.
2. I'd open CamScanner on my phone to convert them into a PDF.
3. I would sit through long, annoying ads and constantly close subscription pop-ups just to download my own file.
4. Finally, I'd send the PDF *back* to myself on WhatsApp just to get it onto my PC.

Realizing how ridiculous this loop was, I decided to build a simple, local tool to do it instantly on my PC—no ads, no paywalls, and completely offline.
