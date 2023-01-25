from flask import Flask
from flask_restful import Api
from endpoints.get_s3_files import get_s3_files

app = Flask(__name__)
app.config['BUNDLE ERRORS'] = True
api = Api(app, catch_all_404s=True)

api.add_resource(get_s3_files, '/files', methods=['GET'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)