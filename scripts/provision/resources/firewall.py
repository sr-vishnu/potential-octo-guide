from jinja2 import FileSystemLoader , Environment
from .resource import Resource
import pathlib
    
class FireWall(Resource):
    def _load_template(self):
        searchpath = pathlib.Path(__file__).parent.parent/"templates"
        loader = FileSystemLoader(searchpath=searchpath)
        template = Environment(loader=loader).get_template("firewall.json.j2")
        return template
        
    def _get_client(self):
        return self.compute.firewalls()
    
    def _execute_request(self):
        return self._get_client().insert(
            project=self.data.get("project_name",""),
            body = self.body
        ).execute()

    def _get_operation(self):
        return (
            self
            .compute
            .globalOperations()
            .get(
                project=self.data.get("project_name",""),
                operation=self.request.get("name","")
            )
        )