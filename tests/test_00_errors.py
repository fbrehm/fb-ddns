#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@summary: Test script (and module) for unit tests on error (exception) classes.

@author: Frank Brehm
@contact: frank@brehm-online.com
@copyright: © 2025 Frank Brehm, Berlin
@license: GPL3
"""

import logging
from pathlib import Path

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from general import FbDdnsTestcase, get_arg_verbose, init_root_logger

LOG = logging.getLogger("test_errors")


# =============================================================================
class TestFbDdnsErrors(FbDdnsTestcase):
    """Testcase class for unit tests on error (exception) classes."""

    # -------------------------------------------------------------------------
    def setUp(self):
        """Execute this on seting up before calling each particular test method."""
        if self.verbose >= 1:
            print()

    # -------------------------------------------------------------------------
    def test_import(self):
        """Test importing module fb_ddns.errors."""
        LOG.info(self.get_method_doc())

        import fb_ddns.errors

        LOG.info("Module version of fb_ddns.errors is {!r}.".format(fb_ddns.errors.__version__))

    # -------------------------------------------------------------------------
    def test_common_errors(self):
        """Test raising a DdnsConfigError and DdnsAppError exception."""
        LOG.info(self.get_method_doc())

        from fb_ddns.errors import DdnsAppError
        from fb_ddns.errors import DdnsConfigError

        for ex in (DdnsConfigError, DdnsAppError):
            if self.verbose >= 1:
                print()
            LOG.debug(f"Testing {ex.__name__} ...")
            with self.assertRaises(ex) as cm:
                raise ex(f"This is a {ex.__name__} exception.")
            e = cm.exception
            LOG.debug("%s raised: %s", e.__class__.__name__, e)

    # -------------------------------------------------------------------------
    def test_ddns_request_error(self):
        """Test raising a DdnsRequestError exception."""
        LOG.info(self.get_method_doc())

        from fb_ddns.errors import DdnsRequestError

        code = 505
        content = "Bla Blub"
        url = "https://nowhere.net"

        with self.assertRaises(DdnsRequestError) as cm:
            raise DdnsRequestError(code, content, url)
        e = cm.exception
        LOG.debug("%s raised: %s", e.__class__.__name__, e)

    # -------------------------------------------------------------------------
    def test_invalid_status_file(self):
        """Test raising an InvalidUpdateStatusFileError exception."""
        LOG.info(self.get_method_doc())

        from fb_ddns.errors import InvalidUpdateStatusFileError

        status_file = Path("/var/tmp/ddns-status.txt")

        for path in (str(status_file), status_file):
            if self.verbose >= 1:
                print()
            LOG.debug(f"Testing InvalidUpdateStatusFileError for {path!r} ...")
            with self.assertRaises(InvalidUpdateStatusFileError) as cm:
                raise InvalidUpdateStatusFileError(path, "Bla blub")
            e = cm.exception
            LOG.debug("%s raised: %s", e.__class__.__name__, e)

    # -------------------------------------------------------------------------
    def test_dir_errors(self):
        """Test raising different Work Dir exceptions."""
        LOG.info(self.get_method_doc())

        from fb_ddns.errors import WorkDirError
        from fb_ddns.errors import WorkDirAccessError
        from fb_ddns.errors import WorkDirNotDirError
        from fb_ddns.errors import WorkDirNotExistsError

        workdir = Path.cwd().resolve() / "workdir"

        for ex in (WorkDirError, WorkDirNotExistsError, WorkDirNotDirError, WorkDirAccessError):
            if self.verbose >= 1:
                print()

            for path in (str(workdir), workdir):
                LOG.debug(f"Testing {ex.__name__} for {path!r} ...")
                with self.assertRaises(ex) as cm:
                    raise ex(path, f"This is a {ex.__name__} exception.")
                e = cm.exception
                LOG.debug("%s raised: %s", e.__class__.__name__, e)


# =============================================================================
if __name__ == "__main__":

    verbose = get_arg_verbose()
    if verbose is None:
        verbose = 0
    init_root_logger(verbose)

    LOG.info("Starting tests ...")

    suite = unittest.TestSuite()

    suite.addTest(TestFbDdnsErrors("test_import", verbose))
    suite.addTest(TestFbDdnsErrors("test_common_errors", verbose))
    suite.addTest(TestFbDdnsErrors("test_ddns_request_error", verbose))
    suite.addTest(TestFbDdnsErrors("test_invalid_status_file", verbose))
    suite.addTest(TestFbDdnsErrors("test_dir_errors", verbose))

    runner = unittest.TextTestRunner(verbosity=verbose)

    result = runner.run(suite)

# =============================================================================

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
