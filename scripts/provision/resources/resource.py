from abc import ABC, abstractmethod
from alive_progress import alive_bar
import googleapiclient.discovery
import json
import time

    
class Resource(ABC):
    def __init__(self,generic_config,extended_config={}):
        self.generic_config = generic_config
        self.extended_config = extended_config
        self.compute = googleapiclient.discovery.build('compute', 'v1')
        self.data = self._process_config()
        self.body = self._process_template()
        self.request = self._execute_request()
        self.operation = self._get_operation()
        self.result = self._get_operation_status()

    @abstractmethod
    def _load_template(self):
        pass

    @abstractmethod
    def _process_config(self):
        pass

    @abstractmethod
    def _get_client(self):
        pass

    @abstractmethod
    def _execute_request(self):
        pass

    @abstractmethod
    def _get_operation(self):
        pass

    def __str__(self):
        return self.result

    def _process_template(self):
        return json.loads(
            self._load_template().render(
                data = self.data
            )
        )

    def _process_config(self):
        self.generic_config.update(self.extended_config)
        return self.generic_config

    def _get_operation_status(self):
        with alive_bar() as ar:
            while True:
                result = self.operation.execute()
                if result['status'] == 'DONE':
                    if 'error' in result:
                        print(f"[ERROR] resource creation failed with the following error: {result['error']}")
                        return ""
                    else:
                        print("resource creation complete [DONE]")
                        return result.get("targetLink","")
                time.sleep(1)
                ar()







