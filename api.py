import spacy
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

from collections import defaultdict

nlp = spacy.load("en_core_web_sm")

@app.route('/api/v1/resources/ner-analyse', methods=['GET', 'POST'])
def api_ner():
	if request.method == 'POST':
		text = request.form['text']
		#print(type(text))
		doc = nlp(text)
		entities = defaultdict(list)
		for entity in doc.ents:
			entities[entity.label_].append(entity.text)

	return jsonify(entities)

if __name__ == "__main__":
	app.run(debug=True) 

#
