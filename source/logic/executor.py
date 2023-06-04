from dataclasses import dataclass
from flask import flash
from pandas import read_csv


    
@dataclass(frozen=True)
class ConductorDefaults(object):
    default_columns: str = '*'
    default_condition: str = ''
    default_ordering: str = ''

class Executor(object):

    def __init__(self, database_manage_object):
        self.database_manage_object = database_manage_object

    def conduct(self, form_values, request, session):

        if form_values is not None:
            
            if form_values['Copy'] == 'Copy':
                file = request.files['file_for_copy']
                file = read_csv(file)
                self.database_manage_object.copy(
                    self.database_manage_object.schema,
                    self.database_manage_object.table,
                    file
                )

            if form_values['Insert'] == 'Insert':
                self.database_manage_object.create(
                    self.database_manage_object.schema,
                    self.database_manage_object.table,
                    form_values['instances'],
                    form_values['target_columns']
                )
                    
            if form_values['Delete'] == 'Delete':
                self.database_manage_object.delete(
                    self.database_manage_object.schema,
                    self.database_manage_object.table,
                    form_values['condition']
                )

            if form_values['Update'] == 'Update':
                self.database_manage_object.update(
                    self.database_manage_object.schema,
                    self.database_manage_object.table,
                    form_values['modification'],
                    form_values['condition']
                )