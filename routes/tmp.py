from flask import Flask, render_template, Blueprint



tmp_blueprint = Blueprint('tmp', __name__, static_folder='/tmp/plots/')
