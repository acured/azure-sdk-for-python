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


class SecurityTaskParameters(Model):
    """Changing set of properties, depending on the task type that is derived from
    the name field.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :ivar name: Name of the task type
    :vartype name: str
    """

    _validation = {
        'name': {'readonly': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, *, additional_properties=None, **kwargs) -> None:
        super(SecurityTaskParameters, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.name = None
