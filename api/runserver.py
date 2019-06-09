import os

from cca import create_app
from argparse import ArgumentParser
from multiprocessing import cpu_count


HOSTS = ("127.0.0.1", "0.0.0.0")


if __name__ == "__main__":
    parser = ArgumentParser(__doc__)
    parser.add_argument("-p", "--port", type=int, default=8080)
    parser.add_argument("-H", "--host", choices=HOSTS, default=HOSTS[0])
    parser.add_argument("-w", "--workers", type=int, default=cpu_count())
    parser.add_argument("-a", "--address")
    args = parser.parse_args()

    app = create_app()
    app.run(host=args.host, port=args.port, workers=args.workers, access_log=True)
