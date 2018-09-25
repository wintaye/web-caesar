from flask import Flask, request, redirect
import cgi
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
	<head>
		<style>
			form {{
				background-color: #eee;
				padding: 20px;
				margin: 0 auto;
				width: 540px;
				font: 16px sans-serif;
				border-radius: 10px;
			}}
			textarea {{
				margin: 10px 0;
				width: 540px;
				height: 120px;
			}}
		</style>
	</head>
	<body>
		<form action="/" method="post">
		<label for="rot">Rotate by:</label>
		<input type="number" name="rot" value="0" />
		<p class="error"></p>
		<br>
		<textarea type="text" name="text">{0}</textarea>
		<br>
		<input type="submit" name="Submit Query" />
	</body>
</html>
"""

@app.route("/")
def index():
	return form.format("Enter text")

@app.route("/", methods=['POST'])
def encrypt():
	rot = request.form['rot']
	rot = int(rot)
	text = request.form['text']
	finished = rotate_string(text, rot)

	return "<h1>" + form.format(finished) + "</h1>"


app.run()