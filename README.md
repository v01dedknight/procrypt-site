# ProCrypt Web

ProCrypt Web is the official information portal for the ProCrypt application. It allows users to explore the program's features, download available versions, and find answers to frequently asked questions.

## Website Architecture

The site is built using Python and the Flask micro-framework. The interface is rendered using Jinja2 HTML templates. All static assets (styles, scripts, images) are organized within the static directory.

## Key Routes:

1. / — Home page with a detailed application overview.
2. /about — FAQ section and general information.
3. /download — Download center featuring all available application builds.
4. /developer — Information about the creator and the project's background.

## Available Downloads:

- ProCrypt Application: Multiple versions tailored for different platforms.
- Documentation: A comprehensive archive (ProCrypt-main.zip) for advanced users.

## Project Structure

.
├── app.py               # Main Flask application entry point
├── templates/           # Jinja2 HTML templates
├── static/              # Static assets and downloadable files
│   ├── css/  
│   ├── js/  
│   ├── images/  
│   └── files/  
├── requirements.txt     # Project dependencies
└── .gitignore           # Git exclusion rules

## Local Setup

1. Install dependencies:
   pip install -r requirements.txt

2. Run the application:
   python app.py

3. View in browser:
   http://localhost:5000/

## Tech Stack
Backend:
- Python 3  
- Flask
Frontend:
- HTML (Jinja2)  
- CSS / JS

## Deployment & Distribution
The project is lightweight and does not require a database, making it easy to run locally or host on any WSGI server (such as Gunicorn or PythonAnywhere). Virtual environments and compiled Python files are excluded from the repository via .gitignore to ensure a clean codebase.

## License
This project is provided "as is" without any warranties. Use at your own risk.
