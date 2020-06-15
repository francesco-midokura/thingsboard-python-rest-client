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


class Tenant(object):
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
        'additional_info': 'str',
        'address': 'str',
        'address2': 'str',
        'city': 'str',
        'country': 'str',
        'created_time': 'int',
        'email': 'str',
        'id': 'TenantId',
        'isolated_tb_core': 'bool',
        'isolated_tb_rule_engine': 'bool',
        'name': 'str',
        'phone': 'str',
        'region': 'str',
        'state': 'str',
        'title': 'str',
        'zip': 'str'
    }

    attribute_map = {
        'additional_info': 'additionalInfo',
        'address': 'address',
        'address2': 'address2',
        'city': 'city',
        'country': 'country',
        'created_time': 'createdTime',
        'email': 'email',
        'id': 'id',
        'isolated_tb_core': 'isolatedTbCore',
        'isolated_tb_rule_engine': 'isolatedTbRuleEngine',
        'name': 'name',
        'phone': 'phone',
        'region': 'region',
        'state': 'state',
        'title': 'title',
        'zip': 'zip'
    }

    def __init__(self, additional_info=None, address=None, address2=None, city=None, country=None, created_time=None, email=None, id=None, isolated_tb_core=None, isolated_tb_rule_engine=None, name=None, phone=None, region=None, state=None, title=None, zip=None):  # noqa: E501
        """Tenant - a model defined in Swagger"""  # noqa: E501

        self._additional_info = None
        self._address = None
        self._address2 = None
        self._city = None
        self._country = None
        self._created_time = None
        self._email = None
        self._id = None
        self._isolated_tb_core = None
        self._isolated_tb_rule_engine = None
        self._name = None
        self._phone = None
        self._region = None
        self._state = None
        self._title = None
        self._zip = None
        self.discriminator = None

        if additional_info is not None:
            self.additional_info = additional_info
        if address is not None:
            self.address = address
        if address2 is not None:
            self.address2 = address2
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if created_time is not None:
            self.created_time = created_time
        if email is not None:
            self.email = email
        if id is not None:
            self.id = id
        if isolated_tb_core is not None:
            self.isolated_tb_core = isolated_tb_core
        if isolated_tb_rule_engine is not None:
            self.isolated_tb_rule_engine = isolated_tb_rule_engine
        if name is not None:
            self.name = name
        if phone is not None:
            self.phone = phone
        if region is not None:
            self.region = region
        if state is not None:
            self.state = state
        if title is not None:
            self.title = title
        if zip is not None:
            self.zip = zip

    @property
    def additional_info(self):
        """Gets the additional_info of this Tenant.  # noqa: E501


        :return: The additional_info of this Tenant.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this Tenant.


        :param additional_info: The additional_info of this Tenant.  # noqa: E501
        :type: str
        """

        self._additional_info = additional_info

    @property
    def address(self):
        """Gets the address of this Tenant.  # noqa: E501


        :return: The address of this Tenant.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Tenant.


        :param address: The address of this Tenant.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def address2(self):
        """Gets the address2 of this Tenant.  # noqa: E501


        :return: The address2 of this Tenant.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this Tenant.


        :param address2: The address2 of this Tenant.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def city(self):
        """Gets the city of this Tenant.  # noqa: E501


        :return: The city of this Tenant.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Tenant.


        :param city: The city of this Tenant.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this Tenant.  # noqa: E501


        :return: The country of this Tenant.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Tenant.


        :param country: The country of this Tenant.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def created_time(self):
        """Gets the created_time of this Tenant.  # noqa: E501


        :return: The created_time of this Tenant.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this Tenant.


        :param created_time: The created_time of this Tenant.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def email(self):
        """Gets the email of this Tenant.  # noqa: E501


        :return: The email of this Tenant.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Tenant.


        :param email: The email of this Tenant.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def id(self):
        """Gets the id of this Tenant.  # noqa: E501


        :return: The id of this Tenant.  # noqa: E501
        :rtype: TenantId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Tenant.


        :param id: The id of this Tenant.  # noqa: E501
        :type: TenantId
        """

        self._id = id

    @property
    def isolated_tb_core(self):
        """Gets the isolated_tb_core of this Tenant.  # noqa: E501


        :return: The isolated_tb_core of this Tenant.  # noqa: E501
        :rtype: bool
        """
        return self._isolated_tb_core

    @isolated_tb_core.setter
    def isolated_tb_core(self, isolated_tb_core):
        """Sets the isolated_tb_core of this Tenant.


        :param isolated_tb_core: The isolated_tb_core of this Tenant.  # noqa: E501
        :type: bool
        """

        self._isolated_tb_core = isolated_tb_core

    @property
    def isolated_tb_rule_engine(self):
        """Gets the isolated_tb_rule_engine of this Tenant.  # noqa: E501


        :return: The isolated_tb_rule_engine of this Tenant.  # noqa: E501
        :rtype: bool
        """
        return self._isolated_tb_rule_engine

    @isolated_tb_rule_engine.setter
    def isolated_tb_rule_engine(self, isolated_tb_rule_engine):
        """Sets the isolated_tb_rule_engine of this Tenant.


        :param isolated_tb_rule_engine: The isolated_tb_rule_engine of this Tenant.  # noqa: E501
        :type: bool
        """

        self._isolated_tb_rule_engine = isolated_tb_rule_engine

    @property
    def name(self):
        """Gets the name of this Tenant.  # noqa: E501


        :return: The name of this Tenant.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Tenant.


        :param name: The name of this Tenant.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def phone(self):
        """Gets the phone of this Tenant.  # noqa: E501


        :return: The phone of this Tenant.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Tenant.


        :param phone: The phone of this Tenant.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def region(self):
        """Gets the region of this Tenant.  # noqa: E501


        :return: The region of this Tenant.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this Tenant.


        :param region: The region of this Tenant.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def state(self):
        """Gets the state of this Tenant.  # noqa: E501


        :return: The state of this Tenant.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Tenant.


        :param state: The state of this Tenant.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def title(self):
        """Gets the title of this Tenant.  # noqa: E501


        :return: The title of this Tenant.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Tenant.


        :param title: The title of this Tenant.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def zip(self):
        """Gets the zip of this Tenant.  # noqa: E501


        :return: The zip of this Tenant.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this Tenant.


        :param zip: The zip of this Tenant.  # noqa: E501
        :type: str
        """

        self._zip = zip

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
        if issubclass(Tenant, dict):
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
        if not isinstance(other, Tenant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
