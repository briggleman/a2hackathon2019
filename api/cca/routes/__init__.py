from sanic import Blueprint
from cca.config import CONFIG
from cca.routes.v1 import health, balance, transaction

v1 = Blueprint.group(health, balance, transaction, url_prefix=f"{CONFIG.route}/v1")