import os

from jinja2 import Environment, FileSystemLoader, BaseLoader, nativetypes

# initialize current directory to make Jinja Environment initialization cleaner
_dir = os.path.dirname(os.path.realpath(__file__))


# this Environment returns a native python type (usually a dict) when 'render' is called, used for JSON API responses
response_env = nativetypes.NativeEnvironment(loader=FileSystemLoader(os.path.join(_dir, "responses")))

# returned when an exception is thrown, or a request is invalid
ex = response_env.get_template("core/base.j2")
# health endpoint
hl = response_env.get_template("health/health.j2")
# balance endpoint
bl = response_env.get_template("v1/balance.j2")
# transaction endpoint
tr = response_env.get_template("v1/transaction.j2")
