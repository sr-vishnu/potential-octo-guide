from jinja2 import FileSystemLoader , Environment
from .resource import Resource
import pathlib
    
class Instance(Resource):
    def _load_template(self):
        searchpath = pathlib.Path(__file__).parent.parent/"templates"
        loader = FileSystemLoader(searchpath=searchpath)
        template = Environment(loader=loader).get_template("instance.json.j2")
        return template
        
    def _get_client(self):
        return self.compute.instances()
    
    def _execute_request(self):
        return self._get_client().insert(
            project=self.data.get("project_name",""),
            zone=self.data.get("zone_name",""),
            body = self.body
        ).execute()

    def _get_operation(self):
        return (
            self
            .compute
            .zoneOperations()
            .get(
                project=self.data.get("project_name",""),
                zone=self.data.get("zone_name",""),
                operation=self.request.get("name","")
            )
        )
    def get_ip(self):
        response = self._get_client().get(
            project=self.data.get("project_name",""),
            zone=self.data.get("zone_name",""),
            instance=self.data.get("instance_name","")
        ).execute()

        return {
            "private": (
                response
                .get("networkInterfaces",[])[0]
                .get("networkIP","")
            ),
            "public": (
                response
                .get("networkInterfaces",[])[0]
                .get("accessConfigs",[])[0]
                .get("natIP","")
            )
        }