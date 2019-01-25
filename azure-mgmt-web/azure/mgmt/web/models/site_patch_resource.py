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

from .proxy_only_resource import ProxyOnlyResource


class SitePatchResource(ProxyOnlyResource):
    """ARM resource for a site.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar state: Current state of the app.
    :vartype state: str
    :ivar host_names: Hostnames associated with the app.
    :vartype host_names: list[str]
    :ivar repository_site_name: Name of the repository site.
    :vartype repository_site_name: str
    :ivar usage_state: State indicating whether the app has exceeded its quota
     usage. Read-only. Possible values include: 'Normal', 'Exceeded'
    :vartype usage_state: str or ~azure.mgmt.web.models.UsageState
    :param enabled: <code>true</code> if the app is enabled; otherwise,
     <code>false</code>. Setting this value to false disables the app (takes
     the app offline).
    :type enabled: bool
    :ivar enabled_host_names: Enabled hostnames for the app.Hostnames need to
     be assigned (see HostNames) AND enabled. Otherwise,
     the app is not served on those hostnames.
    :vartype enabled_host_names: list[str]
    :ivar availability_state: Management information availability state for
     the app. Possible values include: 'Normal', 'Limited',
     'DisasterRecoveryMode'
    :vartype availability_state: str or
     ~azure.mgmt.web.models.SiteAvailabilityState
    :param host_name_ssl_states: Hostname SSL states are used to manage the
     SSL bindings for app's hostnames.
    :type host_name_ssl_states: list[~azure.mgmt.web.models.HostNameSslState]
    :param server_farm_id: Resource ID of the associated App Service plan,
     formatted as:
     "/subscriptions/{subscriptionID}/resourceGroups/{groupName}/providers/Microsoft.Web/serverfarms/{appServicePlanName}".
    :type server_farm_id: str
    :param reserved: <code>true</code> if reserved; otherwise,
     <code>false</code>. Default value: False .
    :type reserved: bool
    :param is_xenon: Obsolete: Hyper-V sandbox. Default value: False .
    :type is_xenon: bool
    :param hyper_v: Hyper-V sandbox. Default value: False .
    :type hyper_v: bool
    :ivar last_modified_time_utc: Last time the app was modified, in UTC.
     Read-only.
    :vartype last_modified_time_utc: datetime
    :param site_config: Configuration of the app.
    :type site_config: ~azure.mgmt.web.models.SiteConfig
    :ivar traffic_manager_host_names: Azure Traffic Manager hostnames
     associated with the app. Read-only.
    :vartype traffic_manager_host_names: list[str]
    :param scm_site_also_stopped: <code>true</code> to stop SCM (KUDU) site
     when the app is stopped; otherwise, <code>false</code>. The default is
     <code>false</code>. Default value: False .
    :type scm_site_also_stopped: bool
    :ivar target_swap_slot: Specifies which deployment slot this app will swap
     into. Read-only.
    :vartype target_swap_slot: str
    :param hosting_environment_profile: App Service Environment to use for the
     app.
    :type hosting_environment_profile:
     ~azure.mgmt.web.models.HostingEnvironmentProfile
    :param client_affinity_enabled: <code>true</code> to enable client
     affinity; <code>false</code> to stop sending session affinity cookies,
     which route client requests in the same session to the same instance.
     Default is <code>true</code>.
    :type client_affinity_enabled: bool
    :param client_cert_enabled: <code>true</code> to enable client certificate
     authentication (TLS mutual authentication); otherwise, <code>false</code>.
     Default is <code>false</code>.
    :type client_cert_enabled: bool
    :param host_names_disabled: <code>true</code> to disable the public
     hostnames of the app; otherwise, <code>false</code>.
     If <code>true</code>, the app is only accessible via API management
     process.
    :type host_names_disabled: bool
    :ivar outbound_ip_addresses: List of IP addresses that the app uses for
     outbound connections (e.g. database access). Includes VIPs from tenants
     that site can be hosted with current settings. Read-only.
    :vartype outbound_ip_addresses: str
    :ivar possible_outbound_ip_addresses: List of IP addresses that the app
     uses for outbound connections (e.g. database access). Includes VIPs from
     all tenants. Read-only.
    :vartype possible_outbound_ip_addresses: str
    :param container_size: Size of the function container.
    :type container_size: int
    :param daily_memory_time_quota: Maximum allowed daily memory-time quota
     (applicable on dynamic apps only).
    :type daily_memory_time_quota: int
    :ivar suspended_till: App suspended till in case memory-time quota is
     exceeded.
    :vartype suspended_till: datetime
    :ivar max_number_of_workers: Maximum number of workers.
     This only applies to Functions container.
    :vartype max_number_of_workers: int
    :param cloning_info: If specified during app creation, the app is cloned
     from a source app.
    :type cloning_info: ~azure.mgmt.web.models.CloningInfo
    :ivar resource_group: Name of the resource group the app belongs to.
     Read-only.
    :vartype resource_group: str
    :ivar is_default_container: <code>true</code> if the app is a default
     container; otherwise, <code>false</code>.
    :vartype is_default_container: bool
    :ivar default_host_name: Default hostname of the app. Read-only.
    :vartype default_host_name: str
    :ivar slot_swap_status: Status of the last deployment slot swap operation.
    :vartype slot_swap_status: ~azure.mgmt.web.models.SlotSwapStatus
    :param https_only: HttpsOnly: configures a web site to accept only https
     requests. Issues redirect for
     http requests
    :type https_only: bool
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'state': {'readonly': True},
        'host_names': {'readonly': True},
        'repository_site_name': {'readonly': True},
        'usage_state': {'readonly': True},
        'enabled_host_names': {'readonly': True},
        'availability_state': {'readonly': True},
        'last_modified_time_utc': {'readonly': True},
        'traffic_manager_host_names': {'readonly': True},
        'target_swap_slot': {'readonly': True},
        'outbound_ip_addresses': {'readonly': True},
        'possible_outbound_ip_addresses': {'readonly': True},
        'suspended_till': {'readonly': True},
        'max_number_of_workers': {'readonly': True},
        'resource_group': {'readonly': True},
        'is_default_container': {'readonly': True},
        'default_host_name': {'readonly': True},
        'slot_swap_status': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'state': {'key': 'properties.state', 'type': 'str'},
        'host_names': {'key': 'properties.hostNames', 'type': '[str]'},
        'repository_site_name': {'key': 'properties.repositorySiteName', 'type': 'str'},
        'usage_state': {'key': 'properties.usageState', 'type': 'UsageState'},
        'enabled': {'key': 'properties.enabled', 'type': 'bool'},
        'enabled_host_names': {'key': 'properties.enabledHostNames', 'type': '[str]'},
        'availability_state': {'key': 'properties.availabilityState', 'type': 'SiteAvailabilityState'},
        'host_name_ssl_states': {'key': 'properties.hostNameSslStates', 'type': '[HostNameSslState]'},
        'server_farm_id': {'key': 'properties.serverFarmId', 'type': 'str'},
        'reserved': {'key': 'properties.reserved', 'type': 'bool'},
        'is_xenon': {'key': 'properties.isXenon', 'type': 'bool'},
        'hyper_v': {'key': 'properties.hyperV', 'type': 'bool'},
        'last_modified_time_utc': {'key': 'properties.lastModifiedTimeUtc', 'type': 'iso-8601'},
        'site_config': {'key': 'properties.siteConfig', 'type': 'SiteConfig'},
        'traffic_manager_host_names': {'key': 'properties.trafficManagerHostNames', 'type': '[str]'},
        'scm_site_also_stopped': {'key': 'properties.scmSiteAlsoStopped', 'type': 'bool'},
        'target_swap_slot': {'key': 'properties.targetSwapSlot', 'type': 'str'},
        'hosting_environment_profile': {'key': 'properties.hostingEnvironmentProfile', 'type': 'HostingEnvironmentProfile'},
        'client_affinity_enabled': {'key': 'properties.clientAffinityEnabled', 'type': 'bool'},
        'client_cert_enabled': {'key': 'properties.clientCertEnabled', 'type': 'bool'},
        'host_names_disabled': {'key': 'properties.hostNamesDisabled', 'type': 'bool'},
        'outbound_ip_addresses': {'key': 'properties.outboundIpAddresses', 'type': 'str'},
        'possible_outbound_ip_addresses': {'key': 'properties.possibleOutboundIpAddresses', 'type': 'str'},
        'container_size': {'key': 'properties.containerSize', 'type': 'int'},
        'daily_memory_time_quota': {'key': 'properties.dailyMemoryTimeQuota', 'type': 'int'},
        'suspended_till': {'key': 'properties.suspendedTill', 'type': 'iso-8601'},
        'max_number_of_workers': {'key': 'properties.maxNumberOfWorkers', 'type': 'int'},
        'cloning_info': {'key': 'properties.cloningInfo', 'type': 'CloningInfo'},
        'resource_group': {'key': 'properties.resourceGroup', 'type': 'str'},
        'is_default_container': {'key': 'properties.isDefaultContainer', 'type': 'bool'},
        'default_host_name': {'key': 'properties.defaultHostName', 'type': 'str'},
        'slot_swap_status': {'key': 'properties.slotSwapStatus', 'type': 'SlotSwapStatus'},
        'https_only': {'key': 'properties.httpsOnly', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(SitePatchResource, self).__init__(**kwargs)
        self.state = None
        self.host_names = None
        self.repository_site_name = None
        self.usage_state = None
        self.enabled = kwargs.get('enabled', None)
        self.enabled_host_names = None
        self.availability_state = None
        self.host_name_ssl_states = kwargs.get('host_name_ssl_states', None)
        self.server_farm_id = kwargs.get('server_farm_id', None)
        self.reserved = kwargs.get('reserved', False)
        self.is_xenon = kwargs.get('is_xenon', False)
        self.hyper_v = kwargs.get('hyper_v', False)
        self.last_modified_time_utc = None
        self.site_config = kwargs.get('site_config', None)
        self.traffic_manager_host_names = None
        self.scm_site_also_stopped = kwargs.get('scm_site_also_stopped', False)
        self.target_swap_slot = None
        self.hosting_environment_profile = kwargs.get('hosting_environment_profile', None)
        self.client_affinity_enabled = kwargs.get('client_affinity_enabled', None)
        self.client_cert_enabled = kwargs.get('client_cert_enabled', None)
        self.host_names_disabled = kwargs.get('host_names_disabled', None)
        self.outbound_ip_addresses = None
        self.possible_outbound_ip_addresses = None
        self.container_size = kwargs.get('container_size', None)
        self.daily_memory_time_quota = kwargs.get('daily_memory_time_quota', None)
        self.suspended_till = None
        self.max_number_of_workers = None
        self.cloning_info = kwargs.get('cloning_info', None)
        self.resource_group = None
        self.is_default_container = None
        self.default_host_name = None
        self.slot_swap_status = None
        self.https_only = kwargs.get('https_only', None)
