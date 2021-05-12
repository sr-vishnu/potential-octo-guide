from jinja2 import FileSystemLoader , Environment
from .resource import Resource
import pathlib
    
class SubNet(Resource):
    def _load_template(self):
        searchpath = pathlib.Path(__file__).parent.parent/"templates"
        loader = FileSystemLoader(searchpath=searchpath)
        template = Environment(loader=loader).get_template("subnet.json.j2")
        return template
        
    def _get_client(self):
        return self.compute.subnetworks()
    
    def _execute_request(self):
        return self._get_client().insert(
            project=self.data.get("project_name",""),
            region=self.data.get("region_name",""),
            body = self.body
        ).execute()

    def _get_operation(self):
        return (
            self
            .compute
            .regionOperations()
            .get(
                project=self.data.get("project_name",""),
                region=self.data.get("region_name",""),
                operation=self.request.get("name","")
            )
        )