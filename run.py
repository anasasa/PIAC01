from flask import Flask, render_template, request
from AzureDB import AzureDB
import os

basedir = os.path.abspath(os.path.dirname(__file__))
data_file = os.path.join(basedir, 'static/gallery/')

app = Flask(__name__)

@app.route('/')
def index():
  print(data_file)
  files = os.listdir(data_file)
  files.sort()
  print(files)
  return render_template("index.html", dispFooter="true", files = files)

@app.route('/guestbook', methods=['GET', 'POST'])
def guestbook():
  if request.method == 'POST':
    if request.form['submit'] == 'delete':
      selected_entries = request.form.getlist("delcomments")
      for entry in selected_entries:
        with AzureDB() as a:
          a.azureDeleteData(entry)  
      with AzureDB() as a:
        data = a.azureGetData()
      return render_template("guestbook.html", data = data, mode = 'delete')
    else:
      name=request.form['name']
      text=request.form['comments']
      with AzureDB() as a:
        a.azureAddData(name, text)
        data = a.azureGetData()
      return render_template("guestbook.html", data = data)
  else:
    user=request.args.get('user')
    if user == 'panda':
      with AzureDB() as a:
        data = a.azureGetData()
      return render_template("guestbook.html", data = data, mode = 'delete')
    else:
      with AzureDB() as a:
        data = a.azureGetData()
      return render_template("guestbook.html", data = data)
  
if __name__ == '__main__':
#  app.run(debug="True",host="0.0.0.0",port=5000)
  app.run(host='0.0.0.0')
