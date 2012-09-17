# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function, division

import os
import gc
import logging
import time

import pymorphy2
import pymorphy2.data
from pymorphy2 import opencorpora_dict
from pymorphy2.vendor.docopt import docopt

logger = logging.getLogger('pymorphy2')
logger.addHandler(logging.StreamHandler())

def get_mem_usage():
    import psutil
    gc.collect()
    gc.collect()
    proc = psutil.Process(os.getpid())
    return proc.get_memory_info()[0]

# ============================ Commands ===========================

def compile_dict(in_filename, out_folder=None):
    """
    Makes a Pymorphy2 dictionary from OpenCorpora .xml dictionary.
    """
    if out_folder is None:
        out_folder = 'dict'
    opencorpora_dict.to_pymorphy2_format(in_filename, out_folder)

def xml_to_json(in_filename, out_filename):
    """
    Parses XML and caches result to json.
    """
    opencorpora_dict.xml_dict_to_json(in_filename, out_filename)


def show_dict_mem_usage(dict_filename, verbose=False):
    """
    Shows dictionary memory usage.
    """
    initial_mem = get_mem_usage()
    initial_time = time.time()

    dct = pymorphy2.data.load_dict(dict_filename)

    end_time = time.time()
    mem_usage = get_mem_usage()

    logger.info('Memory usage: %0.1fM dictionary, %0.1fM total (load time %0.2fs)',
        (mem_usage-initial_mem)/(1024*1024), mem_usage/(1024*1024), end_time-initial_time)

    logger.debug("Meta: %s", dct.meta)

    if verbose:
        try:
            from guppy import hpy; hp=hpy()
            logger.debug(hp.heap())
        except ImportError:
            logger.warning('guppy is not installed, detailed info is not available')


def make_test_suite(dict_filename, out_filename, word_limit=100):
    """
    Makes a test suite from OpenCorpora dictionary.
    FIXME: it doesn't work!
    """
    return opencorpora_dict.to_test_suite(
        dict_filename, out_filename, word_limit=int(word_limit))

# =============================================================================

DOC ="""
Pymorphy2 is a Russian POS tagger and inflection engine.

Usage:
    pymorphy dict compile <IN_FILE> [--out <PATH>] [--verbose]
    pymorphy dict xml2json <IN_XML_FILE> <OUT_JSON_FILE> [--verbose]
    pymorphy dict download [--verbose]
    pymorphy dict mem_usage <PATH> [--verbose]
    pymorphy dict make_test_suite <IN_FILE> <OUT_FILE> [--limit <NUM>] [--verbose]
    pymorphy -h | --help
    pymorphy --version

Options:
    -v --verbose        Be more verbose
    -o --out <PATH>     Output folder name [default: dict]
    --limit <NUM>       Min. number of words per gram. tag

"""

def main():
    """
    Pymorphy CLI interface dispatcher
    """
    args = docopt(DOC, version=pymorphy2.__version__)

    if args['--verbose']:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    if args['dict']:
        if args['compile']:
            return compile_dict(args['<IN_FILE>'], args['--out'])
        elif args['xml2json']:
            return xml_to_json(args['<IN_XML_FILE>'], args['<OUT_JSON_FILE>'])
        elif args['mem_usage']:
            return show_dict_mem_usage(args['<PATH>'], args['--verbose'])
        elif args['make_test_suite']:
            return make_test_suite(args['<IN_FILE>'], args['<OUT_FILE>'], int(args['--limit']))
        elif args['download']:
            raise NotImplementedError()

    logger.debug(args)