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


class LinuxOsInfo(Model):
    """Information about a Linux OS.

    :param linux_os_state: The state of the Linux OS. Possible values include:
     'NonDeprovisioned', 'DeprovisionRequested', 'DeprovisionApplied'
    :type linux_os_state: str or ~azure.mgmt.devtestlabs.models.LinuxOsState
    """

    _attribute_map = {
        'linux_os_state': {'key': 'linuxOsState', 'type': 'str'},
    }

    def __init__(self, *, linux_os_state=None, **kwargs) -> None:
        super(LinuxOsInfo, self).__init__(**kwargs)
        self.linux_os_state = linux_os_state
