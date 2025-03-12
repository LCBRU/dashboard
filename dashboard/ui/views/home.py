import io
from dashboard.model.projects import Project
from .. import blueprint
from flask import render_template, request, send_file
from lbrc_flask.forms import SearchForm
from lbrc_flask.database import db
from sqlalchemy import select
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

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

@blueprint.route("/plothole")
def plothole():
    return render_template('ui/plothole.html')

@blueprint.route("/plot")
def plot():
    return send_file(
        plot_points(100),
        as_attachment=False,
        download_name='plot.png',
        max_age=0,
        mimetype='image/png',
    )


def plot_points(points):
    fig = Figure()
    FigureCanvas(fig)

    ax = fig.add_subplot(111)

    ax.scatter([1,2,3], [3,2,1])

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(f'There are {points} data points!')
    ax.grid(True)

    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    #clip off the xml headers from the image
    # svg_img = '<svg' + img.getvalue().split('<svg')[1]
    # unaltered_image = img.getvalue()

    # print('@'*100)
    # print(svg_img == unaltered_image)

    # print(unaltered_image)
    # print('@'*100)
    
    return img