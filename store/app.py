
import os, requests, json, uuid, shutil

from flask import Flask, request, send_file, abort, make_response


app = Flask(__name__)
app.config['HOST'] = "localhost"
app.config['DEBUG'] = True
app.config['PORT'] = 5999
app.config['STORAGE_FOLDER'] = '/home/cloo/store'


@app.route('/')
@app.route('/<path:path>', methods=['GET','POST','PUT','DELETE'])
def storage(path=''):
	if '..' in path or path.startswith('/'):
		abort(400)
	dir = app.config['STORAGE_FOLDER'] + '/' + path
	if path == '':
		listing = os.listdir( dir )
		resp = make_response( json.dumps( listing ) )
		resp.mimetype = "application/json"
		return resp
	elif request.method == 'DELETE' or ( request.method == 'POST' and request.form.get('submit','').lower() == 'delete' ):
		if not os.path.exists(dir):
			abort(404)
		elif os.path.isfile(dir):
			os.remove(dir)
		else:
			shutil.rmtree(dir)
		return ''
	elif request.method in ['POST','PUT'] or (request.method == 'GET' and request.args.get('url',False)):
		if request.data:
			data = request.data
		else:
			data = request.json if request.json else request.values
			
		if request.args.get('url',False):
			try:
				r = requests.get(url)
				data = r.raw
			except:
				abort(400)

		if len(data) == 0: data = False
		if isinstance(data,dict) or isinstance(data,list):
			data = json.dumps(data,indent=4)

		try:
			file = request.files['file']
		except:
			file = False
					
		if file:
			try:
				file.save(dir)
				return ''
			except:
				abort(400)
		elif data:
			try:
				out = open(dir, 'w')
				out.write(data)
				out.close()
				return ''
			except:
				abort(400)
		elif not os.path.exists(dir) and request.method == 'PUT':
			os.makedirs(dir)
			return ''
		else:
			abort(400)
			
	elif request.method == 'GET':
		if not os.path.exists(dir):
			abort(404)
		elif os.path.isfile(dir):
			return send_file(dir)
		else:
			listing = os.listdir( dir )
			resp = make_response( json.dumps( listing ) )
			resp.mimetype = "application/json"
			return resp
	else:
		abort(400)


if __name__ == "__main__":
	if not os.path.exists(app.config['STORAGE_FOLDER']):
		print 'Storage folder does not exist!'
		exit
	else:
		app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=app.config['PORT'])

