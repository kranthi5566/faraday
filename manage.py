#!/usr/bin/env python


from flask_script import Manager

from server.web import app
from server.importer import ImportCouchDB
from server.commands import DatabaseSchema

manager = Manager(app)


if __name__ == "__main__":
    manager.add_command('import-from-couchdb', ImportCouchDB())
    manager.add_command('generate_database_schemas', DatabaseSchema())
    manager.run()
