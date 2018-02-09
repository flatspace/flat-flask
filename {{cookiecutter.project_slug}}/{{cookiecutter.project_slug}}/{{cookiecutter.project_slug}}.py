# -*- coding: utf-8 -*-
import connexion

{{(cookiecutter.project_slug.title()).replace('_', '')}} = connexion.App(__name__, specification_dir='swagger')
app.add_api('{{cookiecutter.project_slug}}.yaml')
