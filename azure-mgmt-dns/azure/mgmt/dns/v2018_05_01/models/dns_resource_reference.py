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


class DnsResourceReference(Model):
    """Represents a single Azure resource and its referencing DNS records.

    :param dns_resources: A list of dns Records
    :type dns_resources: list[~azure.mgmt.dns.v2018_05_01.models.SubResource]
    :param target_resource: A reference to an azure resource from where the
     dns resource value is taken.
    :type target_resource: ~azure.mgmt.dns.v2018_05_01.models.SubResource
    """

    _attribute_map = {
        'dns_resources': {'key': 'dnsResources', 'type': '[SubResource]'},
        'target_resource': {'key': 'targetResource', 'type': 'SubResource'},
    }

    def __init__(self, **kwargs):
        super(DnsResourceReference, self).__init__(**kwargs)
        self.dns_resources = kwargs.get('dns_resources', None)
        self.target_resource = kwargs.get('target_resource', None)
