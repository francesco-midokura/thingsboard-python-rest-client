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


class CustomMenuItem(object):
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
        'child_menu_items': 'list[CustomMenuItem]',
        'icon_url': 'str',
        'iframe_url': 'str',
        'material_icon': 'str',
        'name': 'str',
        'set_access_token': 'bool'
    }

    attribute_map = {
        'child_menu_items': 'childMenuItems',
        'icon_url': 'iconUrl',
        'iframe_url': 'iframeUrl',
        'material_icon': 'materialIcon',
        'name': 'name',
        'set_access_token': 'setAccessToken'
    }

    def __init__(self, child_menu_items=None, icon_url=None, iframe_url=None, material_icon=None, name=None, set_access_token=None):  # noqa: E501
        """CustomMenuItem - a model defined in Swagger"""  # noqa: E501

        self._child_menu_items = None
        self._icon_url = None
        self._iframe_url = None
        self._material_icon = None
        self._name = None
        self._set_access_token = None
        self.discriminator = None

        if child_menu_items is not None:
            self.child_menu_items = child_menu_items
        if icon_url is not None:
            self.icon_url = icon_url
        if iframe_url is not None:
            self.iframe_url = iframe_url
        if material_icon is not None:
            self.material_icon = material_icon
        if name is not None:
            self.name = name
        if set_access_token is not None:
            self.set_access_token = set_access_token

    @property
    def child_menu_items(self):
        """Gets the child_menu_items of this CustomMenuItem.  # noqa: E501


        :return: The child_menu_items of this CustomMenuItem.  # noqa: E501
        :rtype: list[CustomMenuItem]
        """
        return self._child_menu_items

    @child_menu_items.setter
    def child_menu_items(self, child_menu_items):
        """Sets the child_menu_items of this CustomMenuItem.


        :param child_menu_items: The child_menu_items of this CustomMenuItem.  # noqa: E501
        :type: list[CustomMenuItem]
        """

        self._child_menu_items = child_menu_items

    @property
    def icon_url(self):
        """Gets the icon_url of this CustomMenuItem.  # noqa: E501


        :return: The icon_url of this CustomMenuItem.  # noqa: E501
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this CustomMenuItem.


        :param icon_url: The icon_url of this CustomMenuItem.  # noqa: E501
        :type: str
        """

        self._icon_url = icon_url

    @property
    def iframe_url(self):
        """Gets the iframe_url of this CustomMenuItem.  # noqa: E501


        :return: The iframe_url of this CustomMenuItem.  # noqa: E501
        :rtype: str
        """
        return self._iframe_url

    @iframe_url.setter
    def iframe_url(self, iframe_url):
        """Sets the iframe_url of this CustomMenuItem.


        :param iframe_url: The iframe_url of this CustomMenuItem.  # noqa: E501
        :type: str
        """

        self._iframe_url = iframe_url

    @property
    def material_icon(self):
        """Gets the material_icon of this CustomMenuItem.  # noqa: E501


        :return: The material_icon of this CustomMenuItem.  # noqa: E501
        :rtype: str
        """
        return self._material_icon

    @material_icon.setter
    def material_icon(self, material_icon):
        """Sets the material_icon of this CustomMenuItem.


        :param material_icon: The material_icon of this CustomMenuItem.  # noqa: E501
        :type: str
        """

        self._material_icon = material_icon

    @property
    def name(self):
        """Gets the name of this CustomMenuItem.  # noqa: E501


        :return: The name of this CustomMenuItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomMenuItem.


        :param name: The name of this CustomMenuItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def set_access_token(self):
        """Gets the set_access_token of this CustomMenuItem.  # noqa: E501


        :return: The set_access_token of this CustomMenuItem.  # noqa: E501
        :rtype: bool
        """
        return self._set_access_token

    @set_access_token.setter
    def set_access_token(self, set_access_token):
        """Sets the set_access_token of this CustomMenuItem.


        :param set_access_token: The set_access_token of this CustomMenuItem.  # noqa: E501
        :type: bool
        """

        self._set_access_token = set_access_token

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
        if issubclass(CustomMenuItem, dict):
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
        if not isinstance(other, CustomMenuItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
