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


class Cost(Model):
    """A cost item.

    :param currency_code: The currency code of the cost.
    :type currency_code: str
    :param costs: The per-day costs items of the cost.
    :type costs: list[~azure.mgmt.devtestlabs.models.CostPerDayProperties]
    :param id: The identifier of the resource.
    :type id: str
    :param name: The name of the resource.
    :type name: str
    :param type: The type of the resource.
    :type type: str
    :param location: The location of the resource.
    :type location: str
    :param tags: The tags of the resource.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'currency_code': {'key': 'properties.currencyCode', 'type': 'str'},
        'costs': {'key': 'properties.costs', 'type': '[CostPerDayProperties]'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(Cost, self).__init__(**kwargs)
        self.currency_code = kwargs.get('currency_code', None)
        self.costs = kwargs.get('costs', None)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.type = kwargs.get('type', None)
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)
