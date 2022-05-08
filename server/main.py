from flask import Flask
from flask_restful import Api, Resource, request
import requests
import part_db

app = Flask(__name__)
api = Api(app)


class Victor(Resource):
    def post(self):
        num = int(request.form['question_num'])
        if num > 0:
            count = 0
            while count < num:
                a = requests.get('https://jservice.io/api/random?count=1')[0]
                b = part_db.insert_post(a)
                count += b
            return part_db.output_post(num)
        else:
            return []


api.add_resource(Victor, 'main')
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, port=3000, host='127.0.0.1')
