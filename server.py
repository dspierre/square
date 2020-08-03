from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('number', type=float, required=True)
parser.add_argument('word', required=True)
class HelloWorld(Resource):
    def get(self):
        return {'hello':'world'}

class Square(Resource):
    def post(self):
        args = parser.parse_args()
        number = args['number']
        res = number * number
        return {'square': res}, 200
class Palindrome(Resource):
    def  post(self):
        args = parser.parse_args()
        a=args['word']
        a=moulinette(a)
        def is_palindrome(a):
            for i in range(len(a) // 2):
                if a[i] != a[-i - 1]:
                    return False
            return True
        # Dictionnaire associatif des caractères accentuées en langue francophone
        car = {
            "à": "a",
            "ä": "a",
            "â": "a",
            "ç": "c",
            "é": "e",
            "è": "e",
            "ë": "e",
            "ï": "i",
            "ô": "o",
            "ù": "u",
            "ü": "u",
            "û": "u",
            " ": "",
            "-": "",
            ",": "",
            "'": "",
            "?": "",
            "!": "",
            ".": ""
        }
        # Remplacer des caractères par d'autres
        def moulinette(a):
            a = a.lower()
            for cle, valeur in car.items():
                a = a.replace(cle, valeur)
            return a
        # MAIN
        #a = moulinette(input("Entrez une phrase : "))
        if is_palindrome(a) == True:
            return "C'est un palindrome."
        else:
            return "Ce n'est pas un palindrome"
api.add_resource(HelloWorld, '/hello')
api.add_resource(Palindrome,'/palindrome')

api.add_resource(Square, '/square')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
