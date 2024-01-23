from flask import Flask


app = Flask(__name__)

@app.route("/")
def  main():
    return "<p>My name is Dany!</p"


@app.route("/sec/")
def  main2():
    return "<p>Intresting...</p"

# if __name__ == "__main__":
#     app.run(debug=True)