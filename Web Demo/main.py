#-*- coding:utf-8 -*-

from flask import Flask, render_template
from flask_socketio import SocketIO
import intent

from konlpy.tag import Okt

app = Flask(__name__)
socketio = SocketIO(app)

def get_noun(text):
    tokenizer = Okt()
    nouns = Okt().nouns(text)
    return [n for n in nouns]

def get_stem(text):
    tokenizer = Okt()
    stems = tokenizer.morphs(text)
    return [n for n in stems]

@app.route('/')
def sessions():
    return render_template('session.html')


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):

    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)
    handle_my_intent(str(json))

@socketio.on('my intent')
def handle_my_intent(string):

    answer = intent.intent(string)
    print("string : ", string)
    print("answer : ", answer)
    answer = 'Car : ' + answer
    socketio.emit('my intent', answer)

if __name__ == '__main__':
    socketio.run(app, debug=True)
