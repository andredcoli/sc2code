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
- `openai` library for Python
- OpenAI API key (You need to sign up for OpenAI and obtain an API key)

### Setup
1. Install the required python libraries: ```pip install openai requests tk```

### How To Run
1. Run the application ```python sc2code.py```
2. Insert and apply your OpenAI API Key.
3. Upload a screenshot by clicking the 'Upload Screenshot' button.
4. Click 'Convert' to generate the HTML, CSS, and JavaScript code.
5. View the generated code in the respective tabs.
6. To convert a new image, simply upload a new screenshot.

### Contributions
If there are any contributions you would like to make towards this project simply just create a pull request!

## License
[MIT License](LICENSE)
