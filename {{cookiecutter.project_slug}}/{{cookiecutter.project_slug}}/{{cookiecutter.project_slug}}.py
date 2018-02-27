# -*- coding: utf-8 -*-
import connexion

app = connexion.App(__name__, specification_dir='swagger')
app.add_api('{{cookiecutter.project_slug}}_api.yaml')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
