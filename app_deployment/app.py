from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms import validators
from flask_wtf.csrf import CsrfProtect
import os
import joblib
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = 'williamsit'
csrf = CsrfProtect(app)

def load_model():
    global model
    model = joblib.load(os.path.join('Model', 'finalized_model.sav'))

load_model()


@app.route('/')
def greetings():
    return (
        f"Available Routes:<br/>"
        f"/input"
    )

@app.route('/empty')
def empty():
    return "Hello"

@app.route('/input', methods=['GET', 'POST'])
def input():
    form = InputForm()
    if form.validate_on_submit():
        temp_high_data = form.temperature_high.data
        temp_low_data = form.temperature_low.data
        zipcode_data = form.zipcode.data
        day_data = form.day.data
        month_data = form.month.data
        weekday_data = form.weekday.data
        holiday_data = form.holiday.data

        class results():
            temp_high = temp_high_data
            temp_low = temp_low_data
            zipcode_result = zipcode_data
            day_result = day_data
            weekday_result = weekday_data
            month_result = month_data
            holiday_result = holiday_data

        temp_high_array = np.array(form.temperature_high.data)
        temp_reshape = temp_high_array.reshape(1,-1)
        predict_temp_high = model.predict(temp_reshape)
        test_data = model.predict([[5]])
        
        class predicted_results():
            predicted_temp_high_data = test_data

        return render_template('results.html', form=form, results=results, predict=predicted_results)

    if not form.validate_on_submit():
        flash(form.errors)

    return render_template('submit.html', form=form)

class InputForm(FlaskForm):
    temperature_high = IntegerField("Temperature High (F)", [validators.DataRequired()])
    temperature_low = IntegerField("Temperature Low (F)", [validators.DataRequired()])
    zipcode = IntegerField("Zipcode", [validators.DataRequired()])
    day = SelectField(u'Day of Month', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),('15','15'),('16','16'),('17','17'),('18','18'),('19','19'),('20','20'),('21','21'),('22','22'),('23','23'),('24','24'),('25','25'),('26','26'),('27','27'),('28','28'),('29','29'),('30','30'),('31','31'),])
    weekday = SelectField(u'Day of Week', choices=[('Sunday','Sunday'),('Monday','Monday'),('Tuesday','Tuesday'),('Wednesday','Wednesday'),('Thursday','Thursday'),('Friday','Friday'),('Saturday','Saturday')])
    month = SelectField(u'Month', choices=[('1','January'),('2','February'),('3','March'),('4','April'),('5','May'),('6','June'),('7','July'),('8','August'),('9','September'),('10','October'),('11','November'),('12','December')])
    holiday = SelectField(u'Holiday', choices=[('Yes','Yes'),('No','No')])
    submit = SubmitField("Submit")

if __name__ == '__main__':
    app.debug = True
    app.run()