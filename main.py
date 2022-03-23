from flask import Flask,render_template,request,make_response

app=Flask(__name__,static_folder="static",static_url_path="/static")

@app.route("/")
def home():
    #return "fefe"
     return render_template("index.html")

if __name__=="__main__":
    app.run()