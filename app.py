from flask import render_template, request,Flask, url_for
from database  import all_books, add_book
app=Flask(__name__)


@app.route("/recommendations", methods=["GET","POST"])
def recommendations():
    if request.method=="GET":
        return render_template("add_book.html")
    else:
        book_name = request.form["book_name"]
        author=request.form["author"]
        genre=request.form["genre"]
        recommendation=request.form["recommendation"]
        add_book(book_name,author,genre,recommendation)
        return render_template("add_book.html")

@app.route("/")
def homepage():
    return render_template("homepage.html")
    

@app.route('/allbooks')
def show_books():
    books=all_books()
    return render_template("showbooks.html",books=books)

if __name__ == '__main__':

    app.run(debug=True)
