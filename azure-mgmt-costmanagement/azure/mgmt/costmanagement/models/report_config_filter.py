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


class ReportConfigFilter(Model):
    """The filter expression to be used in the report.

    :param and_property: The logical "AND" expression. Must have atleast 2
     items.
    :type and_property:
     list[~azure.mgmt.costmanagement.models.ReportConfigFilter]
    :param or_property: The logical "OR" expression. Must have atleast 2
     items.
    :type or_property:
     list[~azure.mgmt.costmanagement.models.ReportConfigFilter]
    :param not_property: The logical "NOT" expression.
    :type not_property: ~azure.mgmt.costmanagement.models.ReportConfigFilter
    :param dimension: Has comparison expression for a dimension
    :type dimension:
     ~azure.mgmt.costmanagement.models.ReportConfigComparisonExpression
    :param tag: Has comparison expression for a tag
    :type tag:
     ~azure.mgmt.costmanagement.models.ReportConfigComparisonExpression
    """

    _validation = {
        'and_property': {'min_items': 2},
        'or_property': {'min_items': 2},
    }

    _attribute_map = {
        'and_property': {'key': 'and', 'type': '[ReportConfigFilter]'},
        'or_property': {'key': 'or', 'type': '[ReportConfigFilter]'},
        'not_property': {'key': 'not', 'type': 'ReportConfigFilter'},
        'dimension': {'key': 'dimension', 'type': 'ReportConfigComparisonExpression'},
        'tag': {'key': 'tag', 'type': 'ReportConfigComparisonExpression'},
    }

    def __init__(self, **kwargs):
        super(ReportConfigFilter, self).__init__(**kwargs)
        self.and_property = kwargs.get('and_property', None)
        self.or_property = kwargs.get('or_property', None)
        self.not_property = kwargs.get('not_property', None)
        self.dimension = kwargs.get('dimension', None)
        self.tag = kwargs.get('tag', None)
