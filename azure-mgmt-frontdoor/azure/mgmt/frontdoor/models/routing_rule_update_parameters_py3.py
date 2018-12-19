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


class RoutingRuleUpdateParameters(Model):
    """Routing rules to apply to an endpoint.

    :param route_type: Route type. Possible values include: 'Forward',
     'Redirect'
    :type route_type: str or ~azure.mgmt.frontdoor.models.FrontDoorRouteType
    :param frontend_endpoints: Frontend endpoints associated with this rule
    :type frontend_endpoints: list[~azure.mgmt.frontdoor.models.SubResource]
    :param accepted_protocols: Protocol schemes to match for this rule
    :type accepted_protocols: list[str or
     ~azure.mgmt.frontdoor.models.FrontDoorProtocol]
    :param patterns_to_match: The route patterns of the rule.
    :type patterns_to_match: list[str]
    :param custom_forwarding_path: A custom path used to rewrite resource
     paths matched by this rule. Leave empty to use incoming path.
    :type custom_forwarding_path: str
    :param forwarding_protocol: Protocol this rule will use when forwarding
     traffic to backends. Possible values include: 'HttpOnly', 'HttpsOnly',
     'MatchRequest'
    :type forwarding_protocol: str or
     ~azure.mgmt.frontdoor.models.FrontDoorForwardingProtocol
    :param cache_configuration: The caching configuration associated with this
     rule.
    :type cache_configuration: ~azure.mgmt.frontdoor.models.CacheConfiguration
    :param backend_pool: A reference to the BackendPool which this rule routes
     to.
    :type backend_pool: ~azure.mgmt.frontdoor.models.SubResource
    :param enabled_state: Whether to enable use of this rule. Permitted values
     are 'Enabled' or 'Disabled'. Possible values include: 'Enabled',
     'Disabled'
    :type enabled_state: str or
     ~azure.mgmt.frontdoor.models.FrontDoorEnabledState
    :param redirect_configuration: A reference to the redirect routing
     configuration.
    :type redirect_configuration:
     ~azure.mgmt.frontdoor.models.RedirectConfiguration
    """

    _attribute_map = {
        'route_type': {'key': 'routeType', 'type': 'str'},
        'frontend_endpoints': {'key': 'frontendEndpoints', 'type': '[SubResource]'},
        'accepted_protocols': {'key': 'acceptedProtocols', 'type': '[str]'},
        'patterns_to_match': {'key': 'patternsToMatch', 'type': '[str]'},
        'custom_forwarding_path': {'key': 'customForwardingPath', 'type': 'str'},
        'forwarding_protocol': {'key': 'forwardingProtocol', 'type': 'str'},
        'cache_configuration': {'key': 'cacheConfiguration', 'type': 'CacheConfiguration'},
        'backend_pool': {'key': 'backendPool', 'type': 'SubResource'},
        'enabled_state': {'key': 'enabledState', 'type': 'str'},
        'redirect_configuration': {'key': 'redirectConfiguration', 'type': 'RedirectConfiguration'},
    }

    def __init__(self, *, route_type=None, frontend_endpoints=None, accepted_protocols=None, patterns_to_match=None, custom_forwarding_path: str=None, forwarding_protocol=None, cache_configuration=None, backend_pool=None, enabled_state=None, redirect_configuration=None, **kwargs) -> None:
        super(RoutingRuleUpdateParameters, self).__init__(**kwargs)
        self.route_type = route_type
        self.frontend_endpoints = frontend_endpoints
        self.accepted_protocols = accepted_protocols
        self.patterns_to_match = patterns_to_match
        self.custom_forwarding_path = custom_forwarding_path
        self.forwarding_protocol = forwarding_protocol
        self.cache_configuration = cache_configuration
        self.backend_pool = backend_pool
        self.enabled_state = enabled_state
        self.redirect_configuration = redirect_configuration
