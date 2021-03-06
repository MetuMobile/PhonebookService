from flask import Flask, jsonify#, request, render_template
import sys
from Config import Config
from Phonebook import Phonebook

class PhonebookService:
    serviceName = "phonebook"

    def __init__(self):
        self._initializeService()
        self.app.add_url_rule('/phonebook', '', self.getPhonebook)
        self._runService()

    def getPhonebook(self):
        return jsonify(Phonebook=Phonebook().get())

    def _addLogger(self):
        import logging
        handler = logging.FileHandler(Config.loggerPath)  # errors logged to this file
        handler.setLevel(logging.ERROR)  # only log errors and above
        self.app.logger.addHandler(handler)  # attach the handler to the app's logger

    def _runService(self):
        self.app.run(debug=Config.debug, host='0.0.0.0', port=Config.services[self.serviceName]['port'], threaded=True)
        print(str(self.serviceName) + " service is started.")

    def _initializeService(self):
        sys.stdout.flush()
        self.app = Flask(__name__)
        self._addLogger()
        self.app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


if __name__ == "__main__":
    service = PhonebookService()

