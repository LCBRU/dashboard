from dashboard.model.projects import Project
from .. import blueprint
from flask import render_template, request
from lbrc_flask.forms import SearchForm
from lbrc_flask.database import db
from sqlalchemy import select


@blueprint.route("/")
def index():
    search_form = SearchForm(formdata=request.args, search_placeholder='Search email addresses')

    q = select(Project)

    if search_form.search.data:
        q = q.filter(Project.title.like(f'%{search_form.search.data}%'))

    projects = db.paginate(select=q)

    return render_template(
        "ui/index.html",
        projects=projects,
        search_form=search_form,
    )
