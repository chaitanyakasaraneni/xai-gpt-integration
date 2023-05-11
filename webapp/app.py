import openai
import numpy as np
import json

from logging import Logger
from lime.lime_text import LimeTextExplainer
from flask import Flask, render_template, request

# Load OpenAI text completion model
model_engine = {
    "davinci": "text-davinci-002",
    "curie": "text-curie-001",
}
model_selected = None
prompt = "Convert this text into emojis:"

# Initialize logger
log = Logger(__name__)

app = Flask(__name__)

# Load the OpenAI API key from environment variable
app.config.from_file('config/local.json', load=json.load)

# Authenticate OpenAI API key
openai.api_key = app.config['SECRETS']['API_SECRET']

def generate_emoji(input_text):
    # Use OpenAI API to generate emojis for the given input text
    response = openai.Completion.create(
        engine=model_selected,
        prompt=input_text,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.8,
    )

    output_text = response.choices[0].text
    return output_text

def generate_lime_explanation(input_text):
    # Use LIME to generate an explanation for the emoji generation
    explainer = LimeTextExplainer(class_names=['emojis'])
    exp = explainer.explain_instance(input_text, generate_emoji, num_features=6)
    return exp.as_list()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emoji', methods=['POST'])
def process_text():
    global model_selected
    try:
    
        model_selected = model_engine[str(request.form["model"].lower())]
        input_text = request.form['prompt']
        prompt_upd = prompt + input_text
        emoji_output = generate_emoji(prompt_upd)
        log.debug(f"Emoji output: {emoji_output}")
        try:
            lime_explanation = generate_lime_explanation(prompt_upd)
        except Exception as e:
            log.error(f"Error generating LIME explanation: {e}")
            lime_explanation = "Unable to generate LIME explanation: " + str(e)

        return render_template('result.html',
                                input_text=input_text,
                                emoji_output=emoji_output,
                                lime_explanation=lime_explanation)

    except Exception as e:
        return render_template("error.html", error_message=e)

if __name__ == '__main__':
    app.run(debug=True)
