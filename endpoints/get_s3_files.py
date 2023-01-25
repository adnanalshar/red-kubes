from flask import jsonify
from flask_restful import Resource
import boto3

s3 = boto3.client('s3')

class get_s3_files(Resource):
    def get(self):
        try:
            # list all objects in a specified bucket
            response = s3.list_objects(Bucket='red-kubes-assignment-bucket')

            # extract the file names from the respons
            file_list = [{'fileName': file['Key']} for file in response['Contents']]

            return file_list, 200
        except:
            return {'message': 'Unable to fetch file list from S3 bucket'}, 500

if __name__ == '__main__':
    app.run(debug=True)
