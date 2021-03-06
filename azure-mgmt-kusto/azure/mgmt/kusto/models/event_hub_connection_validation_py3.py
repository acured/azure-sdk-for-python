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


class EventHubConnectionValidation(Model):
    """Class representing an event hub connection validation.

    All required parameters must be populated in order to send to Azure.

    :param eventhub_connection_name: The name of the event hub connection.
    :type eventhub_connection_name: str
    :param event_hub_resource_id: Required. The resource ID of the event hub
     to be used to create a data connection.
    :type event_hub_resource_id: str
    :param consumer_group: Required. The event hub consumer group.
    :type consumer_group: str
    :param table_name: The table where the data should be ingested. Optionally
     the table information can be added to each message.
    :type table_name: str
    :param mapping_rule_name: The mapping rule to be used to ingest the data.
     Optionally the mapping information can be added to each message.
    :type mapping_rule_name: str
    :param data_format: The data format of the message. Optionally the data
     format can be added to each message. Possible values include: 'MULTIJSON',
     'JSON', 'CSV'
    :type data_format: str or ~azure.mgmt.kusto.models.DataFormat
    """

    _validation = {
        'event_hub_resource_id': {'required': True},
        'consumer_group': {'required': True},
    }

    _attribute_map = {
        'eventhub_connection_name': {'key': 'eventhubConnectionName', 'type': 'str'},
        'event_hub_resource_id': {'key': 'properties.eventHubResourceId', 'type': 'str'},
        'consumer_group': {'key': 'properties.consumerGroup', 'type': 'str'},
        'table_name': {'key': 'properties.tableName', 'type': 'str'},
        'mapping_rule_name': {'key': 'properties.mappingRuleName', 'type': 'str'},
        'data_format': {'key': 'properties.dataFormat', 'type': 'str'},
    }

    def __init__(self, *, event_hub_resource_id: str, consumer_group: str, eventhub_connection_name: str=None, table_name: str=None, mapping_rule_name: str=None, data_format=None, **kwargs) -> None:
        super(EventHubConnectionValidation, self).__init__(**kwargs)
        self.eventhub_connection_name = eventhub_connection_name
        self.event_hub_resource_id = event_hub_resource_id
        self.consumer_group = consumer_group
        self.table_name = table_name
        self.mapping_rule_name = mapping_rule_name
        self.data_format = data_format
