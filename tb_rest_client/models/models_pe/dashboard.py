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


class Dashboard(object):
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
        'assigned_customers': 'list[ShortCustomerInfo]',
        'configuration': 'str',
        'created_time': 'int',
        'customer_id': 'CustomerId',
        'id': 'DashboardId',
        'name': 'str',
        'owner_id': 'EntityId',
        'tenant_id': 'TenantId',
        'title': 'str'
    }

    attribute_map = {
        'assigned_customers': 'assignedCustomers',
        'configuration': 'configuration',
        'created_time': 'createdTime',
        'customer_id': 'customerId',
        'id': 'id',
        'name': 'name',
        'owner_id': 'ownerId',
        'tenant_id': 'tenantId',
        'title': 'title'
    }

    def __init__(self, assigned_customers=None, configuration=None, created_time=None, customer_id=None, id=None, name=None, owner_id=None, tenant_id=None, title=None):  # noqa: E501
        """Dashboard - a model defined in Swagger"""  # noqa: E501

        self._assigned_customers = None
        self._configuration = None
        self._created_time = None
        self._customer_id = None
        self._id = None
        self._name = None
        self._owner_id = None
        self._tenant_id = None
        self._title = None
        self.discriminator = None

        if assigned_customers is not None:
            self.assigned_customers = assigned_customers
        if configuration is not None:
            self.configuration = configuration
        if created_time is not None:
            self.created_time = created_time
        if customer_id is not None:
            self.customer_id = customer_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if owner_id is not None:
            self.owner_id = owner_id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if title is not None:
            self.title = title

    @property
    def assigned_customers(self):
        """Gets the assigned_customers of this Dashboard.  # noqa: E501


        :return: The assigned_customers of this Dashboard.  # noqa: E501
        :rtype: list[ShortCustomerInfo]
        """
        return self._assigned_customers

    @assigned_customers.setter
    def assigned_customers(self, assigned_customers):
        """Sets the assigned_customers of this Dashboard.


        :param assigned_customers: The assigned_customers of this Dashboard.  # noqa: E501
        :type: list[ShortCustomerInfo]
        """

        self._assigned_customers = assigned_customers

    @property
    def configuration(self):
        """Gets the configuration of this Dashboard.  # noqa: E501


        :return: The configuration of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this Dashboard.


        :param configuration: The configuration of this Dashboard.  # noqa: E501
        :type: str
        """

        self._configuration = configuration

    @property
    def created_time(self):
        """Gets the created_time of this Dashboard.  # noqa: E501


        :return: The created_time of this Dashboard.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this Dashboard.


        :param created_time: The created_time of this Dashboard.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def customer_id(self):
        """Gets the customer_id of this Dashboard.  # noqa: E501


        :return: The customer_id of this Dashboard.  # noqa: E501
        :rtype: CustomerId
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this Dashboard.


        :param customer_id: The customer_id of this Dashboard.  # noqa: E501
        :type: CustomerId
        """

        self._customer_id = customer_id

    @property
    def id(self):
        """Gets the id of this Dashboard.  # noqa: E501


        :return: The id of this Dashboard.  # noqa: E501
        :rtype: DashboardId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Dashboard.


        :param id: The id of this Dashboard.  # noqa: E501
        :type: DashboardId
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Dashboard.  # noqa: E501


        :return: The name of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Dashboard.


        :param name: The name of this Dashboard.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def owner_id(self):
        """Gets the owner_id of this Dashboard.  # noqa: E501


        :return: The owner_id of this Dashboard.  # noqa: E501
        :rtype: EntityId
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this Dashboard.


        :param owner_id: The owner_id of this Dashboard.  # noqa: E501
        :type: EntityId
        """

        self._owner_id = owner_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Dashboard.  # noqa: E501


        :return: The tenant_id of this Dashboard.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Dashboard.


        :param tenant_id: The tenant_id of this Dashboard.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def title(self):
        """Gets the title of this Dashboard.  # noqa: E501


        :return: The title of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Dashboard.


        :param title: The title of this Dashboard.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if issubclass(Dashboard, dict):
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
        if not isinstance(other, Dashboard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
