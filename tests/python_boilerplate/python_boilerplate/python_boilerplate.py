# -*- coding: utf-8 -*-
import connexion
from python_boilerplate import log_config

app = connexion.App(__name__, specification_dir='swagger')
app.add_api('python_boilerplate_api.yaml')

if __name__ == '__main__':
    log_config.setup(app, "python_boilerplate", None)
    app.run(host='0.0.0.0', port=80, debug=True)
