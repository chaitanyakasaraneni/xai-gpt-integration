# Explaining GPT Predictions

This is an example `python-flask` app that uses `LIME` algorithm to explain predictions from GPT API

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
