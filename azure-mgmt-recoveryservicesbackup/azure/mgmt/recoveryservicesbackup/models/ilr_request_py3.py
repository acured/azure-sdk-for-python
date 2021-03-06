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


class ILRRequest(Model):
    """Parameters to restore file/folders API.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: IaasVMILRRegistrationRequest

    All required parameters must be populated in order to send to Azure.

    :param object_type: Required. Constant filled by server.
    :type object_type: str
    """

    _validation = {
        'object_type': {'required': True},
    }

    _attribute_map = {
        'object_type': {'key': 'objectType', 'type': 'str'},
    }

    _subtype_map = {
        'object_type': {'IaasVMILRRegistrationRequest': 'IaasVMILRRegistrationRequest'}
    }

    def __init__(self, **kwargs) -> None:
        super(ILRRequest, self).__init__(**kwargs)
        self.object_type = None
