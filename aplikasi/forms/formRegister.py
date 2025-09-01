from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, BooleanField, EmailField, TelField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo, InputRequired    

class RegisterForm(FlaskForm):
    nama_depan = StringField('Nama Depan', validators=[InputRequired('Input Required!')])
    nama_belakang = StringField('Nama Belakang', validators=[InputRequired('Input Required!')])
    email= EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), 
                                                        Length(6, 30, 'Password minimal %(min)d dan maksimal %(max)d digit')
                                                        ])
    confirm_pass = PasswordField('Password', validators=[DataRequired(), 
                                                        Length(6, 30, 'Password minimal %(min)d dan maksimal %(max)d digit'),
                                                        EqualTo('Password', 'Konfirmasi password salah!')                                                        
                                                        ])                                     
    phone_number = TelField('Phone Number', validators=[DataRequired(),
                                                        Length(6,15, 'Nomer telepon terlalu pendek atau terlalu panjang!')
                                                        ])
    submit = SubmitField('Login')