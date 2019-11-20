import pytest
import json

from app import app
from repository.repository import Repository


app.testing = True
client = app.test_client()

repo = Repository()


def test_dirlist_listpoints():
    repo.url = "data/forecast"
    assert len(repo.list_points()) == len(repo.dir_list())


def test_read_and_parse():
    with client as c:
        repo.url = "data/forecast/"
        path = repo.url
        cidade = "abobora"
        cidade = str(cidade).upper().strip()
        rv = c.post("APItesteSomar/forecast?cidade=" + cidade)
        for file in repo.dir_list():
            if cidade in file:
                result = repo.read_and_parse(path, file)
        assert json.loads(rv.get_data())["data"] == result
