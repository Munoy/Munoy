from flask import Blueprint, render_template, request, url_for, g, flash

from pybo.models import Schedule, User

from pybo.forms import ScheduleForm

from datetime import datetime

from werkzeug.utils import redirect

from pybo.views.auth_views import login_required


from .. import db


bp = Blueprint('schedule', __name__, url_prefix='/schedule')

@bp.route('/list/')
@login_required
def _list():
    # 입력 파라미터
    page = request.args.get('page', type=int, default=1)
    kw = request.args.get('kw', type=str, default='')

    # 조회
    schedule_list = Schedule.query.order_by(Schedule.create_date.desc())
    if kw:
        search = '%%{}%%'.format(kw)
        sub_query = db.session.query(
            Schedule.creator_id, Schedule.content, User.username).join(
            Schedule, Schedule.creator_id == User.id).subquery()
        schedule_list = schedule_list \
            .join(User) \
            .outerjoin(sub_query, sub_query.c.creator_id == User.id) \
            .filter(Schedule.subject.ilike(search) #일정 제목 검색
        ).distinct()

    schedule_list = schedule_list.paginate(page, per_page=10)

    return render_template('schedule/schedule_list.html', schedule_list=schedule_list, page=page, kw=kw)


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

@bp.route('/detail/<int:schedule_id>/')
def detail(schedule_id):
    form = ScheduleForm()
    schedule = Schedule.query.get_or_404(schedule_id)
    return render_template('schedule/schedule_detail.html', schedule=schedule, form=form)

@bp.route('/delete/<int:schedule_id>')
@login_required
def delete(schedule_id):
    schedule = Schedule.query.get_or_404(schedule_id)
    if g.user != schedule.creator:
        flash('삭제권한이 없습니다')
        return redirect(url_for('schedule.detail', schedule_id=schedule_id))
    db.session.delete(schedule)
    db.session.commit()
    return redirect(url_for('schedule._list'))