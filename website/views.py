from flask import Blueprint, render_template, request
from . import db 
from .models import Note
from flask_login import login_required, current_user
from datetime import date


views = Blueprint('views', __name__)


@views.route('/', methods = ['GET', 'POST'])
@login_required
def home():
    Tdate = date.today()
    note_display = list(Note.query.filter_by(date = date.today()).all())
    return render_template("home.html", user = current_user, notes = note_display, date = Tdate) 
        
        #display everything for the day:
    #     note = request.form.get('item')
    #     new_note = Note(date=date.today(), text = note, user_id = current_user.id)

    #     db.session.add(new_note)
    #     db.session.commit()
        
    # notes = list(db.session.query(Note).all())
    # return render_template("home.html", user = current_user, notes =notes) 


@views.route('/save', methods = ['GET', 'POST'])
@login_required
def save():
    #get the 4 notes, save them along with the date and then display home.html which should already be having 
    #the 4 notes saved 

    
    note = request.form.get('item')
    new_note = Note(date=date.today(), text = note, user_id = current_user.id)

    db.session.add(new_note)
    db.session.commit()

    #notes = list(db.session.query(Note).all())
    return render_template("home.html", user=current_user, notes = [], date = date.today())#?