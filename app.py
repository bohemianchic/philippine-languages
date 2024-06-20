from flask import Flask, render_template, request, jsonify, send_from_directory
from transformers import pipeline

app = Flask(__name__)

# Load the translation model pipeline
translator = pipeline('translation', model="facebook/nllb-200-distilled-600M", tokenizer="facebook/nllb-200-distilled-600M")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']
    src_lang = request.form['src_lang'] + '_Latn'  # Append '_Latn' to the language code
    tgt_lang = request.form['tgt_lang'] + '_Latn'  # Append '_Latn' to the language code
    
    # Perform translation
    translation = translator(text, src_lang=src_lang, tgt_lang=tgt_lang)
    translated_text = ' '.join(translation[0]['translation_text'].split()[:500])  # Limit to 500 words
    return jsonify({'translated_text': translation[0]['translation_text']})

if __name__ == "__main__":
    app.run(debug=True)