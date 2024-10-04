from flask import Blueprint, render_template, request, jsonify
from chatbot.weai import get_response

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    response = get_response(user_message)
    return jsonify({'response': response})
