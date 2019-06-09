import logging

from sanic import Blueprint, response
from cca.templates import tr
from cca.config import CONFIG
from cca.lib.helpers import isotimestamp
from web3 import Web3


transaction = Blueprint("transaction", url_prefix="/transaction")
logger = logging.getLogger(__name__)


"""
Group Transaction
Transaction endpoint used to access an account's balance.
"""


@transaction.route("/", methods=["GET"])
async def get_transaction(request):
    """
    Transaction [/transaction]

    Headers: None

    Parameters: None

    /GET Get information about a transaction
    {
      "data": {
        "transaction": "<transaction_data>"
      },
      "message":"success",
      "created":"2019-06-08T22:53:02.793363",
      "status":777
    }
    :param request: Sanic Request object
    :return: Sanic JSON response
    """
    return response.json(tr.render(message="success", timestamp=isotimestamp(), status=777))


@transaction.route("/", methods=["POST"])
def post_transaction(request):
    """
    Transaction [/transaction]

    Headers: None

    Parameters: None

    /POST Initiate a transaction
    {
        "data": {
            "transaction": "<transaction_data>"
        },
        "message":"success",
        "created":"2019-06-08T22:53:02.793363",
        "status":777
    }
        :param request: Sanic Request object
        :return: Sanic JSON response
        """
    web3 = Web3(Web3.HTTPProvider(f"http://{CONFIG.host}"))
    from_addr = request.json.get("address")
    to_addr = CONFIG.address
    transaction_id = web3.eth.sendTransaction({
        "from": from_addr,
        "to": to_addr,
        "value": web3.toWei('20', 'ether'),
        "data": b"Culinary coin initial transaction"
    })
    return response.json(tr.render(transaction_id=transaction_id.hex(), message="success", timestamp=isotimestamp(), status=777))
