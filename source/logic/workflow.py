from collections import defaultdict
from .checker import Checker
from .executor import Executor



class Workflow(object):

    def __init__(self, request, database_manage_object, session):
        self.database_manage_object = database_manage_object
        self.request = request
        self.session = session
        self.get_form_values(request)

    def get_form_values(self, request):
        if request.method == "POST":
            form_values = defaultdict(str, request.values)

        if request.method == "GET":
            form_values = None
        
        self.form_values = form_values

    def execute(
        self
    ):
        checker = Checker()
        executor = Executor(self.database_manage_object)

        reponse = checker.conduct(self.form_values, self.request, self.session)
        if reponse:
            executor.conduct(self.form_values, self.request, self.session)

        view = self.database_manage_object.read(
            f'select * from {self.database_manage_object.schema}.{self.database_manage_object.table};'
        )
        
        return view