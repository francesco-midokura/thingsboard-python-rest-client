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


class Customer(object):
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
        'customer_id': 'CustomerId',
        'email': 'str',
        'id': 'CustomerId',
        'name': 'str',
        'owner_id': 'EntityId',
        'parent_customer_id': 'CustomerId',
        'phone': 'str',
        'state': 'str',
        'tenant_id': 'TenantId',
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
        'customer_id': 'customerId',
        'email': 'email',
        'id': 'id',
        'name': 'name',
        'owner_id': 'ownerId',
        'parent_customer_id': 'parentCustomerId',
        'phone': 'phone',
        'state': 'state',
        'tenant_id': 'tenantId',
        'title': 'title',
        'zip': 'zip'
    }

    def __init__(self, additional_info=None, address=None, address2=None, city=None, country=None, created_time=None, customer_id=None, email=None, id=None, name=None, owner_id=None, parent_customer_id=None, phone=None, state=None, tenant_id=None, title=None, zip=None):  # noqa: E501
        """Customer - a model defined in Swagger"""  # noqa: E501

        self._additional_info = None
        self._address = None
        self._address2 = None
        self._city = None
        self._country = None
        self._created_time = None
        self._customer_id = None
        self._email = None
        self._id = None
        self._name = None
        self._owner_id = None
        self._parent_customer_id = None
        self._phone = None
        self._state = None
        self._tenant_id = None
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
        if customer_id is not None:
            self.customer_id = customer_id
        if email is not None:
            self.email = email
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if owner_id is not None:
            self.owner_id = owner_id
        if parent_customer_id is not None:
            self.parent_customer_id = parent_customer_id
        if phone is not None:
            self.phone = phone
        if state is not None:
            self.state = state
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if title is not None:
            self.title = title
        if zip is not None:
            self.zip = zip

    @property
    def additional_info(self):
        """Gets the additional_info of this Customer.  # noqa: E501


        :return: The additional_info of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this Customer.


        :param additional_info: The additional_info of this Customer.  # noqa: E501
        :type: str
        """

        self._additional_info = additional_info

    @property
    def address(self):
        """Gets the address of this Customer.  # noqa: E501


        :return: The address of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Customer.


        :param address: The address of this Customer.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def address2(self):
        """Gets the address2 of this Customer.  # noqa: E501


        :return: The address2 of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this Customer.


        :param address2: The address2 of this Customer.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def city(self):
        """Gets the city of this Customer.  # noqa: E501


        :return: The city of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Customer.


        :param city: The city of this Customer.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this Customer.  # noqa: E501


        :return: The country of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Customer.


        :param country: The country of this Customer.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def created_time(self):
        """Gets the created_time of this Customer.  # noqa: E501


        :return: The created_time of this Customer.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this Customer.


        :param created_time: The created_time of this Customer.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def customer_id(self):
        """Gets the customer_id of this Customer.  # noqa: E501


        :return: The customer_id of this Customer.  # noqa: E501
        :rtype: CustomerId
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this Customer.


        :param customer_id: The customer_id of this Customer.  # noqa: E501
        :type: CustomerId
        """

        self._customer_id = customer_id

    @property
    def email(self):
        """Gets the email of this Customer.  # noqa: E501


        :return: The email of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Customer.


        :param email: The email of this Customer.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def id(self):
        """Gets the id of this Customer.  # noqa: E501


        :return: The id of this Customer.  # noqa: E501
        :rtype: CustomerId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Customer.


        :param id: The id of this Customer.  # noqa: E501
        :type: CustomerId
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Customer.  # noqa: E501


        :return: The name of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Customer.


        :param name: The name of this Customer.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def owner_id(self):
        """Gets the owner_id of this Customer.  # noqa: E501


        :return: The owner_id of this Customer.  # noqa: E501
        :rtype: EntityId
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this Customer.


        :param owner_id: The owner_id of this Customer.  # noqa: E501
        :type: EntityId
        """

        self._owner_id = owner_id

    @property
    def parent_customer_id(self):
        """Gets the parent_customer_id of this Customer.  # noqa: E501


        :return: The parent_customer_id of this Customer.  # noqa: E501
        :rtype: CustomerId
        """
        return self._parent_customer_id

    @parent_customer_id.setter
    def parent_customer_id(self, parent_customer_id):
        """Sets the parent_customer_id of this Customer.


        :param parent_customer_id: The parent_customer_id of this Customer.  # noqa: E501
        :type: CustomerId
        """

        self._parent_customer_id = parent_customer_id

    @property
    def phone(self):
        """Gets the phone of this Customer.  # noqa: E501


        :return: The phone of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Customer.


        :param phone: The phone of this Customer.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def state(self):
        """Gets the state of this Customer.  # noqa: E501


        :return: The state of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Customer.


        :param state: The state of this Customer.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Customer.  # noqa: E501


        :return: The tenant_id of this Customer.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Customer.


        :param tenant_id: The tenant_id of this Customer.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def title(self):
        """Gets the title of this Customer.  # noqa: E501


        :return: The title of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Customer.


        :param title: The title of this Customer.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def zip(self):
        """Gets the zip of this Customer.  # noqa: E501


        :return: The zip of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this Customer.


        :param zip: The zip of this Customer.  # noqa: E501
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
        if issubclass(Customer, dict):
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
        if not isinstance(other, Customer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
