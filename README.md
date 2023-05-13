# Explaining GPT Predictions

This is an example `python-flask` app that uses `LIME` algorithm to explain predictions from GPT API.

**NOTE:** This repo is sill a work in progress

### Folder Structure

```
├── LICENSE
├── README.md
├── run.py
└── webapp
    ├── app.py
    ├── config
    │   └── local.json
    ├── static
    │   ├── app.js
    │   └── style.css
    └── templates
        ├── error.html
        ├── index.html
        └── result.html
```
**NOTE:** You need to add your OpenAI API SECRET in `config/local.json` file in order to run this basic `flask` app

### Running the app
- Install `Python` (3.7 or above)
- Create a `Python` virtual enviroment
    ```
    virtualenv venv (recommended) 
    OR
    python3 -m venv venv
    ```
- Install required packages by using `pip install -r requirements.txt` command
- Run the app using `python run.py`
- Got to `localhost:5000` in your browser to access this app

### Example Prompt
```
Summarize this for a second-grade student:

Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter. When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows, and is on average the third-brightest natural object in the night sky after the Moon and Venus.
```

