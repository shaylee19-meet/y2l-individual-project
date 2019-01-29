from flask import render_template, request,Flask, url_for
from database  import all_books, add_book
app=Flask(__name__)

@app.route("/recommendations")
def recommendations():
    if request.method=="get":
        return render_template("addbook.html")
    else:
        book_name = request.form["book_name"]
        author=request.form["author"]
        genre=request.form["genre"]
        recommendation=request.form["recommendation"]
        add_book(book_name,author,genre,recommendation)

@app.route('/allbooks')
def show_books():
    books=all_books()
    return render_template("showbooks.html",books=books)
if __name__ == '__main__':

    app.run(debug=True)
