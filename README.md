# SC-2-CODE

## Description
This application converts screenshots into HTML, CSS, and JavaScript code. It uses OpenAI's GPT-4 Vision API to analyze an image of a webpage or UI component and generates corresponding front-end code. It's built using Python and tkinter for the GUI.

## Features
- Upload screenshots in common image formats (JPG, JPEG, PNG).
- Convert images to HTML, CSS, and JavaScript code.
- Display the generated code in separate tabs for HTML, CSS, and JavaScript.
- Option to remove the uploaded image and upload a new one for conversion.

## Known Issues
- Biggest issue so far is associated with the AI response to the prompt, the "JavaScript Code" is sometimes cut out.

## Installation

### Prerequisites
- Python 3.x
- `tkinter` library for Python
- `requests` library for Python
- OpenAI API key (You need to sign up for OpenAI and obtain an API key)

### Setup
1. Clone the repository: git clone https://github.com/andredcoli/sc2code
