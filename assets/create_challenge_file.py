#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# MIT License
#
# Copyright (c) 2023 Victor Calderon
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Created       : 2023-03-07
# Last Modified : 2023-03-07

import argparse
import logging
from argparse import ArgumentParser, HelpFormatter
from operator import attrgetter
from typing import Dict

import numpy as np

__author__ = ["Victor Calderon"]
__copyright__ = ["Copyright 2023"]
__maintainer__ = ["Victor Calderon"]
__all__ = []

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
)
logger.setLevel(logging.INFO)

# ----------------------------- INPUT PARAMETERS ------------------------------


def _str2bool(v):
    if v.lower() in ("yes", "true", "t", "y", "1"):
        return True
    elif v.lower() in ("no", "false", "f", "n", "0"):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean value expected.")


class SortingHelpFormatter(HelpFormatter):
    def add_arguments(self, actions):
        """
        Modifier for `argparse` help parameters, that sorts them alphabetically
        """
        actions = sorted(actions, key=attrgetter("option_strings"))
        super(SortingHelpFormatter, self).add_arguments(actions)


def get_parser():
    """
    Function to get the input parameters to the script.
    """
    description = ""
    parser = ArgumentParser(
        description=description,
        formatter_class=SortingHelpFormatter,
    )
    # Name of the company
    parser.add_argument(
        "--company",
        dest="company_name",
        default="general",
        type=str,
        help="""
        Name of the company, to which one is applying
        [Default: '%(default)s']
        """,
    )
    # Problem type
    parser.add_argument(
        "--problem-type",
        dest="problem_type",
        default="general",
        type=str,
        help="""
        Type of coding problem.
        [Default: '%(default)s']
        """,
    )
    # Year of submission
    parser.add_argument(
        "--year",
        dest="submission_year",
        default="2023",
        type=str,
        help="""
        Year of submission
        [Default: '%(default)s']
        """,
    )
    # Title of the coding problem
    parser.add_argument(
        "--title",
        dest="title",
        default="",
        type=str,
        help="""
        Title to use for the coding problem.
        [Default: '%(default)s']
        """,
    )

    return parser.parse_args()


# ---------------------------- GENERAL FUNCTIONS ------------------------------


def _show_params(params_dict: Dict):
    """
    Function to show the defined of the class.
    """
    msg = "-" * 50 + "\n"
    msg += "\t---- INPUT PARAMETERS ----" + "\n"
    msg += "" + "\n"
    # Keys to omit
    columns_to_omit = []
    # Sorting keys of dictionary
    keys_sorted = np.sort(list(params_dict.keys()))
    for key_ii in keys_sorted:
        if key_ii not in columns_to_omit:
            msg += f"\t>>> {key_ii} : {params_dict[key_ii]}\n"
    #
    msg += "\n" + "-" * 50 + "\n"
    logger.info(msg)

    return


# ------------------------------ MAIN FUNCTION --------------------------------


def main(params_dict: Dict):
    """
    Main function of the script.
    """
    _show_params(params_dict=params_dict)

    return


if __name__ == "__main__":
    # Initializing dictionary
    params_dict = vars(get_parser())
    # Sending to main function
    main(params_dict=params_dict)
