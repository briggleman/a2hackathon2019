import logging

from web3 import Web3
from sanic import Blueprint, response
from cca.templates import bl
from cca.lib.helpers import isotimestamp
from cca.config import CONFIG


balance = Blueprint("balance", url_prefix="/balance")
logger = logging.getLogger(__name__)


"""
Group Balance
Balance endpoint used to access an account's balance.
"""


@balance.route("/", methods=["GET"])
async def get_balance(request):
    """
    Health [/balance]

    Headers: None

    Parameters: None

    /GET Check an account's balance
    {
      "data": {
        "balance": "<account_balance>"
      },
      "message":"success",
      "created":"2019-06-08T22:53:02.793363",
      "status":777
    }
    :param request: Sanic Request object
    :return: Sanic JSON response
    """
    web3 = Web3(Web3.HTTPProvider(f"http://{CONFIG.host}"))
    addr = request.args.get('address')
    acct_balance = web3.fromWei(web3.eth.getBalance(addr), 'ether')
    return response.json(bl.render(balance=acct_balance, message="success", timestamp=isotimestamp(), status=777))
