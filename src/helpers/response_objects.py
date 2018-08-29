'''
 This file contains the response object for all the routes.

'''

from flask_restplus import fields
from chanakya.src import app, api


option_obj = api.model('options',{
    "hi_text": fields.String,
    "en_text": fields.String,
    "correct": fields.Boolean(default=False)
})


question_obj = api.model('questions',{
    'id': fields.Integer,
    'en_text': fields.String,
    'hi_text': fields.String,
    'difficulty': fields.String(enum=[attr.value for attr in app.config['QUESTION_DIFFICULTY']]),
    'topic': fields.String(enum=[attr.value for attr in app.config['QUESTION_TOPIC']]),
    'type': fields.String(enum=[attr.value for attr in app.config['QUESTION_TYPE']]),
    'options': fields.List(fields.Nested(option_obj))
})
