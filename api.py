from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/getReposts")
def getResposts():
    return "100 reposts"

@app.route("/getLikes")
def getLikes():
    return "200 likes"

@app.route("/getBookmarks")
def getBookmarks():
    return "300 bookmarks"

if __name__ == "__main__":
    app.run(debug=True)