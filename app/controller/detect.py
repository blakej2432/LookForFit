from collections import defaultdict
from datetime import datetime, timedelta
import json

import boto3
from flask import Blueprint, jsonify, request, abort
from flask import render_template, get_template_attribute
from flask import current_app as app

bp = Blueprint('video', __name__, url_prefix="/video")


@bp.route("/")
def view_main():
 