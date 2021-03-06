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
from msrest.exceptions import HttpOperationError


class ApiError(Model):
    """The API error.

    :param error: ApiError. The error properties.
    :type error: ~azure.mgmt.media.models.ODataError
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ODataError'},
    }

    def __init__(self, **kwargs):
        super(ApiError, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class ApiErrorException(HttpOperationError):
    """Server responsed with exception of type: 'ApiError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ApiErrorException, self).__init__(deserialize, response, 'ApiError', *args)
