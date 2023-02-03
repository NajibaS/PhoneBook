from flask import Flask,render_template, redirect
from sqldb import Database
from people_gen import People

app = Flask(__name__,static_folder='assets')
phonebook = Database('phonebook')
@app.route('/')
def start_page():
  contact = phonebook.select_all()
  return render_template('index.html',data=contact)

@app.route('/contact/<slug>')
def contact_info(slug):
  contact = phonebook.select_by_cols({"slug":slug})
  if contact:
    contact_name = f"{contact[0].pop('name')} {contact[0].pop('surname')}"
    contact[0].pop('slug')
    return render_template('contact.html', data=contact[0],name=contact_name) 
  return redirect('/')


app.run(host='0.0.0.0',port=8080)