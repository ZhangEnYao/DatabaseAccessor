from flask import flash
from re import match


    
class Checker(object):

    def conduct(self, form_values, request, session):

        if form_values is not None:

            if form_values['Copy'] == 'Copy':
                file = request.files['file_for_copy']
                if file.filename == '':
                    flash("[Warning] File uploading is necessary!")
                    return False

            if form_values['Insert'] == 'Insert':
                if form_values['instances'] == '':
                    flash("[Warning] The instances is necessary!")
                    return False
                    
            if form_values['Delete'] == 'Delete':
                if form_values['condition'] == '':
                    flash("[Warning] The condition is necessary!")
                    return False

            if form_values['Update'] == 'Update':
                if form_values['modification'] == '' or form_values['condition'] == '':
                    flash("[Warning] The modification and condition are necessary!")
                    return False
            
            for queries in ('instances', 'condition', 'modification'):
                if (
                    match('(?:.*?;.*?)|(?:.*?--.*?)', form_values[queries]) and
                    not match("(?:.*?'.*?;.*?'.*?)|(?:.*?'.*?--.*?'.*?)", form_values[queries])
                ):
                    flash("[Fatal] Injection is forbidden!")
                    return False

        return True