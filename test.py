# -*- coding: utf-8 -*-

from flask import Flask
from flask_neomodel import NeoModel

app = Flask('neomodel APIs')
neomodel = NeoModel(app)


class Test(neomodel.neo.StructuredNode):
    name = neomodel.neo.StringProperty(unique_index=True)


@app.route('/')
def test_neomodel():
    app.logger.debug("graph db object: %s" % neomodel.graph_db)
    test = Test(name="just a test").save()  # Create a new node
    app.logger.info("created test object: %s" % test)
    return 'Hello World!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
