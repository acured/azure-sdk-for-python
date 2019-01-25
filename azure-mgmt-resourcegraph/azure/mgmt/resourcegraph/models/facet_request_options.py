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


class FacetRequestOptions(Model):
    """The options for facet evaluation.

    :param sort_order: The sorting order by the hit count. Possible values
     include: 'asc', 'desc'. Default value: "desc" .
    :type sort_order: str or ~azure.mgmt.resourcegraph.models.FacetSortOrder
    :param top: The maximum number of facet rows that should be returned.
    :type top: int
    """

    _validation = {
        'top': {'maximum': 1000, 'minimum': 1},
    }

    _attribute_map = {
        'sort_order': {'key': 'sortOrder', 'type': 'FacetSortOrder'},
        'top': {'key': '$top', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(FacetRequestOptions, self).__init__(**kwargs)
        self.sort_order = kwargs.get('sort_order', "desc")
        self.top = kwargs.get('top', None)
