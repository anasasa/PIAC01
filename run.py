from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
#  return "<h1 style='color:red'>Hello World!</h1>"
  return render_template("index.html")

@app.route('/aboutme')
def aboutme():
  return render_template("aboutme.html")
  
@app.route('/contact')
def contact():
  return render_template("contact.html")

@app.route('/gallery')
def gallery():
  return render_template("gallery.html")

if __name__ == '__main__':
#  app.run(debug=True)
  app.run(host='0.0.0.0')