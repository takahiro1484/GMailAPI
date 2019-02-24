import os
import json

from oauth2client import tools
from oauth2client import client
from oauth2client.file import Storage


CONFIG_FILE_PATH = os.path.normpath(os.path.join(os.getcwd(), "config", "config.json"))

class AuthRequest:
    def __init__(self):
        self.config = self._config_loader(CONFIG_FILE_PATH)

    def get_credential(self, scope):
        # Storageから認証情報を取得する
        storage = Storage(self.config["path"]["credentials"])

        credentials = storage.get()

        if credentials is None or credentials.invalid:
            # Storageから認証情報を取得出来なかった場合、新規で認証を行う
            flow = client.flow_from_clientsecrets(self.config["path"]["client_id"], scope)
            credentials = tools.run_flow(flow, storage, tools.argparser.parse_args())

        return credentials

    def _config_loader(self, path):
        with open(path, "r", encoding="utf-8") as fh:
            config = json.load(fh)
        return config