from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, DateTimeLocalField
from wtforms.validators import DataRequired, Length, EqualTo

class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])

class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])

class ScheduleForm(FlaskForm):
    start_date = DateTimeLocalField('일정시작일', validators=[DataRequired()], format='%Y-%m-%dT%H:%M')
    end_date = DateTimeLocalField('일정종료일', validators=[DataRequired()], format='%Y-%m-%dT%H:%M')
    subject = StringField('제목', validators=[DataRequired('제목이 없다.')])
    content = TextAreaField('내용', validators=[DataRequired('내용이 없다.')])

