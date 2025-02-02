# coding: utf-8

"""
    Lightly API

    Lightly.ai enables you to do self-supervised learning in an easy and intuitive way. The lightly.ai OpenAPI spec defines how one can interact with our REST API to unleash the full potential of lightly.ai  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@lightly.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from lightly.openapi_generated.swagger_client.configuration import Configuration


class DockerWorkerConfigV3Lightly(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'loader': 'DockerWorkerConfigV3LightlyLoader',
        'model': 'DockerWorkerConfigV3LightlyModel',
        'trainer': 'DockerWorkerConfigV3LightlyTrainer',
        'criterion': 'DockerWorkerConfigV3LightlyCriterion',
        'optimizer': 'DockerWorkerConfigV3LightlyOptimizer',
        'collate': 'DockerWorkerConfigV3LightlyCollate'
    }

    attribute_map = {
        'loader': 'loader',
        'model': 'model',
        'trainer': 'trainer',
        'criterion': 'criterion',
        'optimizer': 'optimizer',
        'collate': 'collate'
    }

    def __init__(self, loader=None, model=None, trainer=None, criterion=None, optimizer=None, collate=None, _configuration=None):  # noqa: E501
        """DockerWorkerConfigV3Lightly - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._loader = None
        self._model = None
        self._trainer = None
        self._criterion = None
        self._optimizer = None
        self._collate = None
        self.discriminator = None

        if loader is not None:
            self.loader = loader
        if model is not None:
            self.model = model
        if trainer is not None:
            self.trainer = trainer
        if criterion is not None:
            self.criterion = criterion
        if optimizer is not None:
            self.optimizer = optimizer
        if collate is not None:
            self.collate = collate

    @property
    def loader(self):
        """Gets the loader of this DockerWorkerConfigV3Lightly.  # noqa: E501


        :return: The loader of this DockerWorkerConfigV3Lightly.  # noqa: E501
        :rtype: DockerWorkerConfigV3LightlyLoader
        """
        return self._loader

    @loader.setter
    def loader(self, loader):
        """Sets the loader of this DockerWorkerConfigV3Lightly.


        :param loader: The loader of this DockerWorkerConfigV3Lightly.  # noqa: E501
        :type: DockerWorkerConfigV3LightlyLoader
        """

        self._loader = loader

    @property
    def model(self):
        """Gets the model of this DockerWorkerConfigV3Lightly.  # noqa: E501


        :return: The model of this DockerWorkerConfigV3Lightly.  # noqa: E501
        :rtype: DockerWorkerConfigV3LightlyModel
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this DockerWorkerConfigV3Lightly.


        :param model: The model of this DockerWorkerConfigV3Lightly.  # noqa: E501
        :type: DockerWorkerConfigV3LightlyModel
        """

        self._model = model

    @property
    def trainer(self):
        """Gets the trainer of this DockerWorkerConfigV3Lightly.  # noqa: E501


        :return: The trainer of this DockerWorkerConfigV3Lightly.  # noqa: E501
        :rtype: DockerWorkerConfigV3LightlyTrainer
        """
        return self._trainer

    @trainer.setter
    def trainer(self, trainer):
        """Sets the trainer of this DockerWorkerConfigV3Lightly.


        :param trainer: The trainer of this DockerWorkerConfigV3Lightly.  # noqa: E501
        :type: DockerWorkerConfigV3LightlyTrainer
        """

        self._trainer = trainer

    @property
    def criterion(self):
        """Gets the criterion of this DockerWorkerConfigV3Lightly.  # noqa: E501


        :return: The criterion of this DockerWorkerConfigV3Lightly.  # noqa: E501
        :rtype: DockerWorkerConfigV3LightlyCriterion
        """
        return self._criterion

    @criterion.setter
    def criterion(self, criterion):
        """Sets the criterion of this DockerWorkerConfigV3Lightly.


        :param criterion: The criterion of this DockerWorkerConfigV3Lightly.  # noqa: E501
        :type: DockerWorkerConfigV3LightlyCriterion
        """

        self._criterion = criterion

    @property
    def optimizer(self):
        """Gets the optimizer of this DockerWorkerConfigV3Lightly.  # noqa: E501


        :return: The optimizer of this DockerWorkerConfigV3Lightly.  # noqa: E501
        :rtype: DockerWorkerConfigV3LightlyOptimizer
        """
        return self._optimizer

    @optimizer.setter
    def optimizer(self, optimizer):
        """Sets the optimizer of this DockerWorkerConfigV3Lightly.


        :param optimizer: The optimizer of this DockerWorkerConfigV3Lightly.  # noqa: E501
        :type: DockerWorkerConfigV3LightlyOptimizer
        """

        self._optimizer = optimizer

    @property
    def collate(self):
        """Gets the collate of this DockerWorkerConfigV3Lightly.  # noqa: E501


        :return: The collate of this DockerWorkerConfigV3Lightly.  # noqa: E501
        :rtype: DockerWorkerConfigV3LightlyCollate
        """
        return self._collate

    @collate.setter
    def collate(self, collate):
        """Sets the collate of this DockerWorkerConfigV3Lightly.


        :param collate: The collate of this DockerWorkerConfigV3Lightly.  # noqa: E501
        :type: DockerWorkerConfigV3LightlyCollate
        """

        self._collate = collate

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DockerWorkerConfigV3Lightly, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DockerWorkerConfigV3Lightly):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DockerWorkerConfigV3Lightly):
            return True

        return self.to_dict() != other.to_dict()
