from flask import Flask
import requests
from flask import request
app = Flask(__name__)
from flask import render_template

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/location')
def location():
	latitude = request.args.get('lat')
	longitude = request.args.get('lon')
	api = 'https://api.wheretheiss.at/v1/coordinates/'
	query = str(latitude) + ',' + str(longitude)
	new_api = api + query
	r = requests.get(new_api)
	print(new_api)
	d = r.json()
	return render_template('location.html', data = d)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)