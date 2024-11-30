import csv
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from flask import Flask, render_template
from wtforms.validators import DataRequired, URL
from wtforms import StringField, SubmitField, URLField, TimeField, SelectField

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('Map link', validators=[DataRequired(), URL()])
    open_time = TimeField('Open', validators=[DataRequired()])
    closing_time = TimeField('Close', validators=[DataRequired()])
    coffee_rating = SelectField(
        'Coffee rating',
        choices=[(0, "✘"), (1, "☕️"), (2, "☕️"*2), (3, "☕️"*3), (4, "☕️"*4), (5, "☕️"*5)],
        validators=[DataRequired()]
    )
    wifi_rating = SelectField(
        'WiFi rating',
        choices=[(0, "✘"), (1, "💪"), (2, "💪"*2), (3, "💪"*3), (4, "💪"*4), (5, "💪"*5)],
        validators=[DataRequired()]
    )
    power_rating = SelectField(
        'Power rating',
        choices=[(0, "✘"), (1, "🔌"), (2, "🔌"*2), (3, "🔌"*3), (4, "🔌"*4), (5, "🔌"*5)],
        validators=[DataRequired()]
    )
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a', newline='') as csv_file:
            new_row = [form.cafe.data, form.location.data, form.open_time.data, form.closing_time.data,
                       form.coffee_rating.data, form.wifi_rating.data, form.power_rating.data]
            update_csv = csv.writer(csv_file)
            update_csv.writerow(new_row)
    return render_template(
        'add.html',
        form=form
    )


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template(
        'cafes.html',
        cafes=list_of_rows
    )


if __name__ == '__main__':
    app.run(debug=True)

