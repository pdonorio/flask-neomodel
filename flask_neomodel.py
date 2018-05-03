# -*- coding: utf-8 -*-

"""
Neo4j GraphDB flask connector through OGM library 'neomodel'
"""

import time
import logging
import neomodel as neomodel_package
from flask import _app_ctx_stack as stack

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class NeoModel(object):

    def __init__(self, app=None, variables=None, exit_if_fails=True):
        self.neo = neomodel_package
        self.app = app
        if variables is None:
            variables = {}
        self.variables = variables
        self.exit = exit_if_fails
        if app is not None:
            self.init_app(app)

        self.connect()
        log.info('connected')

    def init_app(self, app):
        # TODO: set any default to flask config?
        # app.config.setdefault('GRAPH_DATABASE', ':memory:')
        app.teardown_appcontext(self.teardown)

    def connect(self):

        # Set URI
        self.uri = "bolt://%s:%s@%s:%s" % \
            (
                # User:Password
                self.variables.get('user', 'neo4j'),
                self.variables.get('password', 'test'),
                # Host:Port
                self.variables.get('host', 'localhost'),
                self.variables.get('port', 7687),
            )
        log.debug("Connection uri: %s" % self.uri)

        # Try until it's connected
        self.retry()
        self.graph_db = self.neo.db
        log.info("Connected! %s" % self.graph_db)

        return self.graph_db

    def retry(self, retry_interval=2, max_retries=-1):
        retry_count = 0
        while max_retries != 0 or retry_count < max_retries:
            retry_count += 1
            if self.test_connection():
                break
            else:
                log.info("Service not available")
                if self.exit:
                    raise ValueError('No connection available')
                time.sleep(retry_interval)

    def test_connection(self, retry_interval=5, max_retries=0):
        try:
            self.neo.config.DATABASE_URL = self.uri
            self.neo.db.url = self.uri
            self.neo.db.set_connection(self.uri)
            return True
        except BaseException as e:
            log.warning("Failed: %s", e)
            return False

    def teardown(self, exception):
        ctx = stack.top
        if hasattr(ctx, 'graph_db'):
            log.info("Tearing down")
            # neo does not have an 'open' connection that needs closing
            # ctx.graphdb.close()
            ctx.graph_db = None

    @property
    def connection(self):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'graphdb'):
                ctx.graphdb = self.connect()
            return ctx.graphdb
