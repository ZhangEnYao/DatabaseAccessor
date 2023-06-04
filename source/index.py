from flask import Blueprint, render_template, request, session
from flask_login import login_required

from .logic.workflow import Workflow
from .model.configuration import Configurations
from .model.database_management import get_database_management_object

index_blueprint = Blueprint("index", __name__)

@index_blueprint.route("/task=<task>", defaults={'parameters': None}, methods = ['GET', 'POST'])
@index_blueprint.route("/task=<task>&parameters=<parameters>", methods = ['GET', 'POST'])
@login_required
def index(
    task,
    parameters
):
    configuration = Configurations[task]

    table_access_object = get_database_management_object(
        configuration.host,
        configuration.port,
        configuration.database,
        configuration.user,
        configuration.password,
        configuration.schema,
        configuration.table
    )

    workflow = Workflow(
        request,
        table_access_object,
        session = session
    )
    view = workflow.execute()

    service = render_template(
        "index.html",
        attributes = tuple(column.upper() for column in view.columns),
        dataset = tuple(instance for index, instance in view.iterrows()),
        column_information = {
            'columns': f'({table_access_object.columns})',
            'necessary_columns': f'({table_access_object.necessary_columns})'
        },
        parameters = None if session.get('status') else parameters,
        primary_keys = configuration.primary_keys
    )

    session['status'] = True
    
    return service