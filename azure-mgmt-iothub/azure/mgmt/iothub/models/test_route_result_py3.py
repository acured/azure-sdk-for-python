# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TestRouteResult(Model):
    """Result of testing one route.

    :param result: Result of testing route. Possible values include:
     'undefined', 'false', 'true'
    :type result: str or ~azure.mgmt.iothub.models.TestResultStatus
    :param details: Detailed result of testing route
    :type details: ~azure.mgmt.iothub.models.TestRouteResultDetails
    """

    _attribute_map = {
        'result': {'key': 'result', 'type': 'str'},
        'details': {'key': 'details', 'type': 'TestRouteResultDetails'},
    }

    def __init__(self, *, result=None, details=None, **kwargs) -> None:
        super(TestRouteResult, self).__init__(**kwargs)
        self.result = result
        self.details = details
