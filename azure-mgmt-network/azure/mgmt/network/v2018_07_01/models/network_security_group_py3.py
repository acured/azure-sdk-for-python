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

from .resource_py3 import Resource


class NetworkSecurityGroup(Resource):
    """NetworkSecurityGroup resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param security_rules: A collection of security rules of the network
     security group.
    :type security_rules:
     list[~azure.mgmt.network.v2018_07_01.models.SecurityRule]
    :param default_security_rules: The default security rules of network
     security group.
    :type default_security_rules:
     list[~azure.mgmt.network.v2018_07_01.models.SecurityRule]
    :ivar network_interfaces: A collection of references to network
     interfaces.
    :vartype network_interfaces:
     list[~azure.mgmt.network.v2018_07_01.models.NetworkInterface]
    :ivar subnets: A collection of references to subnets.
    :vartype subnets: list[~azure.mgmt.network.v2018_07_01.models.Subnet]
    :param resource_guid: The resource GUID property of the network security
     group resource.
    :type resource_guid: str
    :param provisioning_state: The provisioning state of the public IP
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
        'network_interfaces': {'readonly': True},
        'subnets': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'security_rules': {'key': 'properties.securityRules', 'type': '[SecurityRule]'},
        'default_security_rules': {'key': 'properties.defaultSecurityRules', 'type': '[SecurityRule]'},
        'network_interfaces': {'key': 'properties.networkInterfaces', 'type': '[NetworkInterface]'},
        'subnets': {'key': 'properties.subnets', 'type': '[Subnet]'},
        'resource_guid': {'key': 'properties.resourceGuid', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, location: str=None, tags=None, security_rules=None, default_security_rules=None, resource_guid: str=None, provisioning_state: str=None, etag: str=None, **kwargs) -> None:
        super(NetworkSecurityGroup, self).__init__(id=id, location=location, tags=tags, **kwargs)
        self.security_rules = security_rules
        self.default_security_rules = default_security_rules
        self.network_interfaces = None
        self.subnets = None
        self.resource_guid = resource_guid
        self.provisioning_state = provisioning_state
        self.etag = etag
