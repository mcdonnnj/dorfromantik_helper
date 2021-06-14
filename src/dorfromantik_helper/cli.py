"""Provide an entry-point to the package functionality."""

# Standard Python Libraries
import argparse
import os

from . import constants
from .ui import App


def main():
    parser = argparse.ArgumentParser(
        description="Board suggestions for the game Dorfromantik."
    )

    # Use the script name even if this is called with `python -m dorfromantik_helper`
    if parser.prog == "__main__.py":
        parser.prog = "dorfromantik-helper"

    parser.add_argument(
        "--load", "-l", action="store_true", help="Load data from last manual save"
    )
    parser.add_argument(
        "--height",
        "-y",
        type=int,
        default=1000,
        help="Pixel height of the board display",
    )
    parser.add_argument(
        "--width", "-x", type=int, default=1300, help="Pixel width of the board display"
    )
    args = parser.parse_args()

    from_npz = constants.MANUAL_SAVE_FILEPATH if args.load else None
    if not os.path.exists(constants.SAVE_DIR):
        os.mkdir(constants.SAVE_DIR)

    app = App(from_npz=from_npz, pix_height=args.height, pix_width=args.width)
    app.mainloop()
