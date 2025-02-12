# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.4.0-SNAPSHOT
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Customer(object):
    """NOTE: This class is auto generated by the swagger code generator program.
from tb_rest_client.api_client import ApiClient
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
        'external_id': 'CustomerId',
        'id': 'CustomerId',
        'created_time': 'int',
        'title': 'str',
        'name': 'str',
        'tenant_id': 'TenantId',
        'country': 'str',
        'state': 'str',
        'city': 'str',
        'address': 'str',
        'address2': 'str',
        'zip': 'str',
        'phone': 'str',
        'email': 'str',
        'additional_info': 'JsonNode'
    }

    attribute_map = {
        'external_id': 'externalId',
        'id': 'id',
        'created_time': 'createdTime',
        'title': 'title',
        'name': 'name',
        'tenant_id': 'tenantId',
        'country': 'country',
        'state': 'state',
        'city': 'city',
        'address': 'address',
        'address2': 'address2',
        'zip': 'zip',
        'phone': 'phone',
        'email': 'email',
        'additional_info': 'additionalInfo'
    }

    def __init__(self, external_id=None, id=None, created_time=None, title=None, name=None, tenant_id=None, country=None, state=None, city=None, address=None, address2=None, zip=None, phone=None, email=None, additional_info=None):  # noqa: E501
        """Customer - a model defined in Swagger"""  # noqa: E501
        self._external_id = None
        self._id = None
        self._created_time = None
        self._title = None
        self._name = None
        self._tenant_id = None
        self._country = None
        self._state = None
        self._city = None
        self._address = None
        self._address2 = None
        self._zip = None
        self._phone = None
        self._email = None
        self._additional_info = None
        self.discriminator = None
        if external_id is not None:
            self.external_id = external_id
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if title is not None:
            self.title = title
        if name is not None:
            self.name = name
        self.tenant_id = tenant_id
        self.country = country
        self.state = state
        self.city = city
        self.address = address
        self.address2 = address2
        self.zip = zip
        self.phone = phone
        self.email = email
        if additional_info is not None:
            self.additional_info = additional_info

    @property
    def external_id(self):
        """Gets the external_id of this Customer.  # noqa: E501


        :return: The external_id of this Customer.  # noqa: E501
        :rtype: CustomerId
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this Customer.


        :param external_id: The external_id of this Customer.  # noqa: E501
        :type: CustomerId
        """

        self._external_id = external_id

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
    def created_time(self):
        """Gets the created_time of this Customer.  # noqa: E501

        Timestamp of the customer creation, in milliseconds  # noqa: E501

        :return: The created_time of this Customer.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this Customer.

        Timestamp of the customer creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this Customer.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def title(self):
        """Gets the title of this Customer.  # noqa: E501

        Title of the customer  # noqa: E501

        :return: The title of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Customer.

        Title of the customer  # noqa: E501

        :param title: The title of this Customer.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def name(self):
        """Gets the name of this Customer.  # noqa: E501

        Name of the customer. Read-only, duplicated from title for backward compatibility  # noqa: E501

        :return: The name of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Customer.

        Name of the customer. Read-only, duplicated from title for backward compatibility  # noqa: E501

        :param name: The name of this Customer.  # noqa: E501
        :type: str
        """

        self._name = name

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
    def country(self):
        """Gets the country of this Customer.  # noqa: E501

        Country  # noqa: E501

        :return: The country of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Customer.

        Country  # noqa: E501

        :param country: The country of this Customer.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def state(self):
        """Gets the state of this Customer.  # noqa: E501

        State  # noqa: E501

        :return: The state of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Customer.

        State  # noqa: E501

        :param state: The state of this Customer.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def city(self):
        """Gets the city of this Customer.  # noqa: E501

        City  # noqa: E501

        :return: The city of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Customer.

        City  # noqa: E501

        :param city: The city of this Customer.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def address(self):
        """Gets the address of this Customer.  # noqa: E501

        Address Line 1  # noqa: E501

        :return: The address of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Customer.

        Address Line 1  # noqa: E501

        :param address: The address of this Customer.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def address2(self):
        """Gets the address2 of this Customer.  # noqa: E501

        Address Line 2  # noqa: E501

        :return: The address2 of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this Customer.

        Address Line 2  # noqa: E501

        :param address2: The address2 of this Customer.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def zip(self):
        """Gets the zip of this Customer.  # noqa: E501

        Zip code  # noqa: E501

        :return: The zip of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this Customer.

        Zip code  # noqa: E501

        :param zip: The zip of this Customer.  # noqa: E501
        :type: str
        """

        self._zip = zip

    @property
    def phone(self):
        """Gets the phone of this Customer.  # noqa: E501

        Phone number  # noqa: E501

        :return: The phone of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Customer.

        Phone number  # noqa: E501

        :param phone: The phone of this Customer.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def email(self):
        """Gets the email of this Customer.  # noqa: E501

        Email  # noqa: E501

        :return: The email of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Customer.

        Email  # noqa: E501

        :param email: The email of this Customer.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def additional_info(self):
        """Gets the additional_info of this Customer.  # noqa: E501


        :return: The additional_info of this Customer.  # noqa: E501
        :rtype: JsonNode
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this Customer.


        :param additional_info: The additional_info of this Customer.  # noqa: E501
        :type: JsonNode
        """

        self._additional_info = additional_info

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
