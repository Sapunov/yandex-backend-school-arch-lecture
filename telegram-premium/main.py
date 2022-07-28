import logging
import argparse

import telegram.ext as tg_ext

from bot import handlers


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--token', type=str, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    application = tg_ext.Application.builder().token(args.token).build()

    handlers.setup_handlers(application)

    application.run_polling()


if __name__ == "__main__":
    main()
