"""
    Lebensmittelwarnungen API

    Liste aller Lebensmittel und Produktwarnungen  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.lebensmittelwarnung.model.response_docs import ResponseDocs

from deutschland import lebensmittelwarnung

globals()["ResponseDocs"] = ResponseDocs
from deutschland.lebensmittelwarnung.model.response import Response


class TestResponse(unittest.TestCase):
    """Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResponse(self):
        """Test Response"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Response()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
