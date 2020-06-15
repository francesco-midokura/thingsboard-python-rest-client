# coding: utf-8
#      Copyright 2020. ThingsBoard
#  #
#      Licensed under the Apache License, Version 2.0 (the "License");
#      you may not use this file except in compliance with the License.
#      You may obtain a copy of the License at
#  #
#          http://www.apache.org/licenses/LICENSE-2.0
#  #
#      Unless required by applicable law or agreed to in writing, software
#      distributed under the License is distributed on an "AS IS" BASIS,
#      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#      See the License for the specific language governing permissions and
#      limitations under the License.
#

import pprint
import re  # noqa: F401

import six


class Palette(object):
    """NOTE: This class is auto generated by the swagger code generator program.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'colors': 'dict(str, str)',
        'extends': 'str',
        'type': 'str'
    }

    attribute_map = {
        'colors': 'colors',
        'extends': 'extends',
        'type': 'type'
    }

    def __init__(self, colors=None, extends=None, type=None):  # noqa: E501
        """Palette - a model defined in Swagger"""  # noqa: E501

        self._colors = None
        self._extends = None
        self._type = None
        self.discriminator = None

        if colors is not None:
            self.colors = colors
        if extends is not None:
            self.extends = extends
        if type is not None:
            self.type = type

    @property
    def colors(self):
        """Gets the colors of this Palette.  # noqa: E501


        :return: The colors of this Palette.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._colors

    @colors.setter
    def colors(self, colors):
        """Sets the colors of this Palette.


        :param colors: The colors of this Palette.  # noqa: E501
        :type: dict(str, str)
        """

        self._colors = colors

    @property
    def extends(self):
        """Gets the extends of this Palette.  # noqa: E501


        :return: The extends of this Palette.  # noqa: E501
        :rtype: str
        """
        return self._extends

    @extends.setter
    def extends(self, extends):
        """Sets the extends of this Palette.


        :param extends: The extends of this Palette.  # noqa: E501
        :type: str
        """

        self._extends = extends

    @property
    def type(self):
        """Gets the type of this Palette.  # noqa: E501


        :return: The type of this Palette.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Palette.


        :param type: The type of this Palette.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(Palette, dict):
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
        if not isinstance(other, Palette):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
