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

import uuid
from msrest.pipeline import ClientRawResponse
from msrestazure.azure_exceptions import CloudError
from msrest.polling.async_poller import async_poller, AsyncNoPolling
from msrestazure.polling.async_arm_polling import AsyncARMPolling

from .. import models
from .virtual_machine_scale_set_rolling_upgrades_operations import VirtualMachineScaleSetRollingUpgradesOperations as _VirtualMachineScaleSetRollingUpgradesOperations


class VirtualMachineScaleSetRollingUpgradesOperations(_VirtualMachineScaleSetRollingUpgradesOperations):


    async def _cancel_initial_async(
            self, resource_group_name, vm_scale_set_name, *, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.cancel_async.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'vmScaleSetName': self._serialize.url("vm_scale_set_name", vm_scale_set_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200, 202]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('OperationStatusResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    async def cancel_async(
            self, resource_group_name, vm_scale_set_name, *, custom_headers=None, raw=False, polling=True, **operation_config):
        """Cancels the current virtual machine scale set rolling upgrade.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param vm_scale_set_name: The name of the VM scale set.
        :type vm_scale_set_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for AsyncARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of OperationStatusResponse or
         ClientRawResponse<OperationStatusResponse> if raw==True
        :rtype:
         ~~azure.mgmt.compute.v2017_12_01.models.OperationStatusResponse or
         ~msrest.pipeline.ClientRawResponse[~azure.mgmt.compute.v2017_12_01.models.OperationStatusResponse]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        raw_result = await self._cancel_initial_async(
            resource_group_name=resource_group_name,
            vm_scale_set_name=vm_scale_set_name,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            deserialized = self._deserialize('OperationStatusResponse', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = AsyncARMPolling(lro_delay, lro_options={'final-state-via': 'azure-async-operation'}, **operation_config)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    cancel_async.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/rollingUpgrades/cancel'}


    async def _start_os_upgrade_initial_async(
            self, resource_group_name, vm_scale_set_name, *, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.start_os_upgrade_async.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'vmScaleSetName': self._serialize.url("vm_scale_set_name", vm_scale_set_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200, 202]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('OperationStatusResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    async def start_os_upgrade_async(
            self, resource_group_name, vm_scale_set_name, *, custom_headers=None, raw=False, polling=True, **operation_config):
        """Starts a rolling upgrade to move all virtual machine scale set
        instances to the latest available Platform Image OS version. Instances
        which are already running the latest available OS version are not
        affected.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param vm_scale_set_name: The name of the VM scale set.
        :type vm_scale_set_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for AsyncARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of OperationStatusResponse or
         ClientRawResponse<OperationStatusResponse> if raw==True
        :rtype:
         ~~azure.mgmt.compute.v2017_12_01.models.OperationStatusResponse or
         ~msrest.pipeline.ClientRawResponse[~azure.mgmt.compute.v2017_12_01.models.OperationStatusResponse]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        raw_result = await self._start_os_upgrade_initial_async(
            resource_group_name=resource_group_name,
            vm_scale_set_name=vm_scale_set_name,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            deserialized = self._deserialize('OperationStatusResponse', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = AsyncARMPolling(lro_delay, lro_options={'final-state-via': 'azure-async-operation'}, **operation_config)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    start_os_upgrade_async.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/osRollingUpgrade'}

    async def get_latest_async(
            self, resource_group_name, vm_scale_set_name, *, custom_headers=None, raw=False, **operation_config):
        """Gets the status of the latest virtual machine scale set rolling
        upgrade.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param vm_scale_set_name: The name of the VM scale set.
        :type vm_scale_set_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: RollingUpgradeStatusInfo or ClientRawResponse if raw=true
        :rtype:
         ~azure.mgmt.compute.v2017_12_01.models.RollingUpgradeStatusInfo or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = self.get_latest_async.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'vmScaleSetName': self._serialize.url("vm_scale_set_name", vm_scale_set_name, 'str'),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('RollingUpgradeStatusInfo', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_latest_async.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/rollingUpgrades/latest'}
