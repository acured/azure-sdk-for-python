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


class CustomImagePropertiesCustom(Model):
    """Properties for creating a custom image from a VHD.

    :param image_name: The image name.
    :type image_name: str
    :param sys_prep: Indicates whether sysprep has been run on the VHD.
    :type sys_prep: bool
    """

    _attribute_map = {
        'image_name': {'key': 'imageName', 'type': 'str'},
        'sys_prep': {'key': 'sysPrep', 'type': 'bool'},
    }

    def __init__(self, *, image_name: str=None, sys_prep: bool=None, **kwargs) -> None:
        super(CustomImagePropertiesCustom, self).__init__(**kwargs)
        self.image_name = image_name
        self.sys_prep = sys_prep
