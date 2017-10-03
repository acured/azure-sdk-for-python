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


class TensorFlowSettings(Model):
    """Specifies the settings for TensorFlow job.

    :param python_script_file_path: The path and file name of the python
     script to execute the job.
    :type python_script_file_path: str
    :param python_interpreter_path: The path to python interpreter.
    :type python_interpreter_path: str
    :param master_command_line_args: Specifies the command line arguments for
     the master task.
    :type master_command_line_args: str
    :param worker_command_line_args: Specifies the command line arguments for
     the worker task. This property is optional for single machine training.
    :type worker_command_line_args: str
    :param parameter_server_command_line_args: Specifies the command line
     arguments for the parameter server task. This property is optional for
     single machine training.
    :type parameter_server_command_line_args: str
    :param worker_count: The number of worker tasks. If specified, the value
     must be less than or equal to (nodeCount * numberOfGPUs per VM). If not
     specified, the default value is equal to nodeCount. This property can be
     specified only for distributed TensorFlow training
    :type worker_count: int
    :param parameter_server_count: The number of parmeter server tasks. If
     specified, the value must be less than or equal to nodeCount. If not
     specified, the default value is equal to 1 for distributed TensorFlow
     training (This property is not applicable for single machine training).
     This property can be specified only for distributed TensorFlow training.
    :type parameter_server_count: int
    """

    _validation = {
        'python_script_file_path': {'required': True},
        'master_command_line_args': {'required': True},
    }

    _attribute_map = {
        'python_script_file_path': {'key': 'pythonScriptFilePath', 'type': 'str'},
        'python_interpreter_path': {'key': 'pythonInterpreterPath', 'type': 'str'},
        'master_command_line_args': {'key': 'masterCommandLineArgs', 'type': 'str'},
        'worker_command_line_args': {'key': 'workerCommandLineArgs', 'type': 'str'},
        'parameter_server_command_line_args': {'key': 'parameterServerCommandLineArgs', 'type': 'str'},
        'worker_count': {'key': 'workerCount', 'type': 'int'},
        'parameter_server_count': {'key': 'parameterServerCount', 'type': 'int'},
    }

    def __init__(self, python_script_file_path, master_command_line_args, python_interpreter_path=None, worker_command_line_args=None, parameter_server_command_line_args=None, worker_count=None, parameter_server_count=None):
        self.python_script_file_path = python_script_file_path
        self.python_interpreter_path = python_interpreter_path
        self.master_command_line_args = master_command_line_args
        self.worker_command_line_args = worker_command_line_args
        self.parameter_server_command_line_args = parameter_server_command_line_args
        self.worker_count = worker_count
        self.parameter_server_count = parameter_server_count