from flask import Flask, request
from flask_restx import Resource, Api, fields
from celery.result import AsyncResult

from tasks import *


app = Flask(__name__)
app.config['ENV'] = "development"

api = Api(app, version='0.0.1',
          title='Celery', doc='/api/doc')

post_input = api.model('POST_model_input', {
    'x': fields.Integer(request=True, default=0),
    'y': fields.Integer(request=True, default=0)
})


@api.route('/get_task_info')
class Get_Task_Info(Resource):
    @api.doc(params={'id': 'id'})
    def get(self):
        taskinfo = AsyncResult(request.args.get('id'), app=celery_app)
        result = {
            'task_id': request.args.get('id'),
            'status': taskinfo.status,
            'result': taskinfo.result
        }
        return result


@api.route('/post')
class Post(Resource):
    @api.expect(post_input)
    def post(self):
        data = api.payload
        res = add.delay(data['x'], data['y'])
        result = {
            'task_id': res.id
        }
        return result


@api.route('/get')
class Get(Resource):
    @api.doc(params={'x': '0', 'y': '0'})
    def get(self):
        x = request.args.get('x', default=10)
        y = request.args.get('y', default=5)
        res = subtract.delay(int(x), int(y))
        result = {
            'task_id': res.id
        }
        return result


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
