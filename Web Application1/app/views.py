from flask import render_template, flash, redirect, request
from datetime import datetime, date
from flask_sqlalchemy import SQLAlchemy
from app import app, models, db
from .models import ToDo
from .forms import create_form

#main roue: Index
@app.route('/')
def index():
    #gets all the data from the databse ToDO
    data = models.ToDo.query.all()
    return render_template('All_Assessment.html',
                           title='All Assessment',data = data)


#create assessment
@app.route('/Create', methods=['GET', 'POST'])
def createform():
    #checking if the form is submitted or not
	form = create_form()
	if form.is_submitted():
        #gets all the value from the submitted form
            title = request.form['title']
            module_code = request.form['module_code']
            deadline = request.form['deadline']
            deadtime = datetime.strptime(deadline,'%d-%m-%Y').date()
            description = request.form['description']
            #initially the status will be incomplete: Default
            status = 'INCOMPLETE'
            #stores data to be addded on the databse
            record = ToDo(title,module_code,deadtime,description,status)
            #adds the data to databse ToDO
            db.session.add(record)
            db.session.commit()
            return redirect('/')

	return render_template('Create.html',title='Create Assessment',form=form)

#uncompleted assessment
@app.route('/incomplete/<id>',methods=['POST'])
def id_incomplete(id):
    int_id = int(id)
    #if the user marks as Complete 
    if request.method == 'POST':
        #filters the data bby id
        a = ToDo.query.filter_by(id =int_id).first()
        #changes its status to Completed
        a.status = 'COMPLETED'
        db.session.commit()
        return redirect('/complete')

@app.route('/incomplete', methods=['GET', 'POST'])
def incomplete():
    #filters the data by status == 'Uncomplete'
    result = ToDo.query.filter_by(status='INCOMPLETE')
    return render_template('incomplete.html', title='Uncomplete Assessment', data=result)

#ccmpleted assessment
@app.route('/complete', methods=['GET', 'POST'])
def complete():
    #filters the data by status == 'Complete'
    result = ToDo.query.filter_by(status='COMPLETED')
    return render_template('complete.html', title='Complete Assessment',data=result)




