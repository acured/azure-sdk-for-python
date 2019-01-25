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


class ApplicationSettings(Model):
    """The application settings.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. The application ID.
    :type id: str
    :param is_public: Required. Setting your application as public allows
     other people to use your application's endpoint using their own keys.
    :type is_public: bool
    """

    _validation = {
        'id': {'required': True},
        'is_public': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'is_public': {'key': 'public', 'type': 'bool'},
    }

    def __init__(self, *, id: str, is_public: bool, **kwargs) -> None:
        super(ApplicationSettings, self).__init__(**kwargs)
        self.id = id
        self.is_public = is_public
