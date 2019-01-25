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

from .content_key_policy_play_ready_content_key_location_py3 import ContentKeyPolicyPlayReadyContentKeyLocation


class ContentKeyPolicyPlayReadyContentEncryptionKeyFromKeyIdentifier(ContentKeyPolicyPlayReadyContentKeyLocation):
    """Specifies that the content key ID is specified in the PlayReady
    configuration.

    All required parameters must be populated in order to send to Azure.

    :param odatatype: Required. Constant filled by server.
    :type odatatype: str
    :param key_id: Required. The content key ID.
    :type key_id: str
    """

    _validation = {
        'odatatype': {'required': True},
        'key_id': {'required': True},
    }

    _attribute_map = {
        'odatatype': {'key': '@odata\\.type', 'type': 'str'},
        'key_id': {'key': 'keyId', 'type': 'str'},
    }

    def __init__(self, *, key_id: str, **kwargs) -> None:
        super(ContentKeyPolicyPlayReadyContentEncryptionKeyFromKeyIdentifier, self).__init__(**kwargs)
        self.key_id = key_id
        self.odatatype = '#Microsoft.Media.ContentKeyPolicyPlayReadyContentEncryptionKeyFromKeyIdentifier'
