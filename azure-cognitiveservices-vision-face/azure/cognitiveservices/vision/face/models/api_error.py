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


class APIError(Model):
    """Error information returned by the API.

    :param error:
    :type error: ~azure.cognitiveservices.vision.face.models.Error
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'Error'},
    }

    def __init__(self, **kwargs):
        super(APIError, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class APIErrorException(HttpOperationError):
    """Server responsed with exception of type: 'APIError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(APIErrorException, self).__init__(deserialize, response, 'APIError', *args)
