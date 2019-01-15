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


class ValidationActivity(ControlActivity):
    """This activity blocks execution until a file has been validated to exist,
    with an optional minimum size, or the timeout is reached, whichever is
    earlier.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
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
    :param timeout: Specifies the timeout for the activity to run. If there is
     no value specified, it takes the value of TimeSpan.FromDays(7) which is 1
     week as default. Type: string (or Expression with resultType string),
     pattern: ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])). Type:
     string (or Expression with resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type timeout: object
    :param sleep: A delay in seconds between validation attempts. If no value
     is specified, 10 seconds will be used as the default.
    :type sleep: int
    :param minimum_size: Minimum size of a file in byte. If no value is
     specified, 0 byte will be used as the default.
    :type minimum_size: int
    :param dataset: Required. Validation activity dataset reference.
    :type dataset: ~azure.mgmt.datafactory.models.DatasetReference
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
        'dataset': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'depends_on': {'key': 'dependsOn', 'type': '[ActivityDependency]'},
        'user_properties': {'key': 'userProperties', 'type': '[UserProperty]'},
        'type': {'key': 'type', 'type': 'str'},
        'timeout': {'key': 'typeProperties.timeout', 'type': 'object'},
        'sleep': {'key': 'typeProperties.sleep', 'type': 'int'},
        'minimum_size': {'key': 'typeProperties.minimumSize', 'type': 'int'},
        'dataset': {'key': 'typeProperties.dataset', 'type': 'DatasetReference'},
    }

    def __init__(self, *, name: str, dataset, additional_properties=None, description: str=None, depends_on=None, user_properties=None, timeout=None, sleep: int=None, minimum_size: int=None, **kwargs) -> None:
        super(ValidationActivity, self).__init__(additional_properties=additional_properties, name=name, description=description, depends_on=depends_on, user_properties=user_properties, **kwargs)
        self.timeout = timeout
        self.sleep = sleep
        self.minimum_size = minimum_size
        self.dataset = dataset
        self.type = 'Validation'
