from flask import Flask, jsonify
app = Flask(__name__)
books = [
    {'id': 1, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
    {'id': 2, 'title': '1984', 'author': 'George Orwell'},
    {'id': 3, 'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger'},
]
@app.route('/books')
def get_books():
    return jsonify({'books': books})
if __name__ == '__main__':
    app.run(debug=True)
    
    
    
