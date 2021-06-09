from flask import Flask, render_template, request
from AzureDB import AzureDB
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html", dispFooter="true")

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
