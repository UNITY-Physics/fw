#!/usr/bin/env python
"""The run script"""
import logging
import sys

from flywheel_gear_toolkit import GearToolkitContext
from app.main import find_files

log = logging.getLogger(__name__)

def main(context: GearToolkitContext) -> None:
    """This parses config and run."""

    find_files()

if __name__ == "__main__":

    with GearToolkitContext() as gear_context:

        gear_context.init_logging()
        main(gear_context)
