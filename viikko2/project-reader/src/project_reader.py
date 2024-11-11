from urllib import request
from project import Project
import tomli

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        # print(content)

        toml_dict = tomli.loads(content)

        name = toml_dict["tool"]["poetry"]["name"]
        description = toml_dict["tool"]["poetry"]["description"]
        license = toml_dict["tool"]["poetry"]["license"]
        authors = toml_dict["tool"]["poetry"]["authors"]
        dependencies = list(toml_dict["tool"]["poetry"]["dependencies"].keys())
        dev_dependencies = list(toml_dict["tool"]["poetry"]["group"]["dev"]["dependencies"].keys())

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license, authors, dependencies, dev_dependencies)