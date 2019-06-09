import logging

from sanic import Blueprint, response
from cca.templates import hl
from cca.lib.helpers import isotimestamp


health = Blueprint("health", url_prefix="/health")
logger = logging.getLogger(__name__)


"""
Group Health
Health check endpoint used by cloud resources such as Load Balancers and Instance Groups.
"""


@health.route("/", methods=["GET"])
async def get_health(request):
    """
    Health [/health]

    Headers: None

    Parameters: None

    /GET Check if API is up and handling HTTP requests
    {
      "message":"healthy",
      "created":"2019-04-20T22:53:02.793363",
      "status":777
    }
    :param request: Sanic Request object
    :return: Sanic JSON response
    """
    return response.json(hl.render(message="healthy", timestamp=isotimestamp(), status=777))
