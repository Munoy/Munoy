from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, DateTimeField
from wtforms.validators import DataRequired, Length, EqualTo, NumberRange

class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목이 없다.')])
    content = TextAreaField('내용', validators=[DataRequired('내용이 없다.')])

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용이 없다.')])

class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])

class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])

class ScheduleForm(FlaskForm):
    start_date = DateTimeField('일정시작일')
    end_date = DateTimeField('일정종료일')
    subject = StringField('제목', validators=[DataRequired('제목이 없다.')])
    content = TextAreaField('내용', validators=[DataRequired('내용이 없다.')])

