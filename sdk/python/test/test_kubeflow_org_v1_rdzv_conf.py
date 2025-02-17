# coding: utf-8

"""
    Kubeflow Training SDK

    Python SDK for Kubeflow Training  # noqa: E501

    The version of the OpenAPI document: v1.4.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

from kubeflow.training.models import *
from kubeflow.training.models.kubeflow_org_v1_rdzv_conf import KubeflowOrgV1RDZVConf  # noqa: E501
from kubeflow.training.rest import ApiException

class TestKubeflowOrgV1RDZVConf(unittest.TestCase):
    """KubeflowOrgV1RDZVConf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test KubeflowOrgV1RDZVConf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubeflow.training.models.kubeflow_org_v1_rdzv_conf.KubeflowOrgV1RDZVConf()  # noqa: E501
        if include_optional :
            return KubeflowOrgV1RDZVConf(
                key = '0', 
                value = '0'
            )
        else :
            return KubeflowOrgV1RDZVConf(
        )

    def testKubeflowOrgV1RDZVConf(self):
        """Test KubeflowOrgV1RDZVConf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
