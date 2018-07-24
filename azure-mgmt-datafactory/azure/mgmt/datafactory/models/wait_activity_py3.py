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

from .control_activity_py3 import ControlActivity


class WaitActivity(ControlActivity):
    """This activity suspends pipeline execution for the specified interval.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Activity name.
    :type name: str
    :param description: Activity description.
    :type description: str
    :param depends_on: Activity depends on condition.
    :type depends_on: list[~azure.mgmt.datafactory.models.ActivityDependency]
    :param user_properties: Activity user properties.
    :type user_properties: list[~azure.mgmt.datafactory.models.UserProperty]
    :param type: Required. Constant filled by server.
    :type type: str
    :param wait_time_in_seconds: Required. Duration in seconds.
    :type wait_time_in_seconds: int
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
        'wait_time_in_seconds': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'depends_on': {'key': 'dependsOn', 'type': '[ActivityDependency]'},
        'user_properties': {'key': 'userProperties', 'type': '[UserProperty]'},
        'type': {'key': 'type', 'type': 'str'},
        'wait_time_in_seconds': {'key': 'typeProperties.waitTimeInSeconds', 'type': 'int'},
    }

    def __init__(self, *, name: str, wait_time_in_seconds: int, description: str=None, depends_on=None, user_properties=None, **kwargs) -> None:
        super(WaitActivity, self).__init__(name=name, description=description, depends_on=depends_on, user_properties=user_properties, **kwargs)
        self.wait_time_in_seconds = wait_time_in_seconds
        self.type = 'Wait'