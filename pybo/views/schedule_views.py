from flask import Blueprint, render_template, request, url_for, g

from pybo.models import Schedule

from pybo.forms import ScheduleForm

from datetime import datetime

from werkzeug.utils import redirect

from pybo.views.auth_views import login_required


from .. import db


bp = Blueprint('schedule', __name__, url_prefix='/schedule')



@bp.route('/create/', methods=('GET', 'POST'))
@login_required
def create():
    form = ScheduleForm()
    if request.method == 'POST' and form.validate_on_submit():
        schedule = Schedule(start_date=form.start_date.data,
                            end_date=form.end_date.data,
                            subject=form.subject.data,
                            content=form.content.data,
                            create_date=datetime.now(),
                            creator=g.user
                            )
        db.session.add(schedule)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('schedule/schedule_form.html', form=form)