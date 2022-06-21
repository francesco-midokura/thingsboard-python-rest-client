# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.3.3-SNAPSHOT
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

from tb_rest_client.models.models_ce import EventFilter


class DebugRuleChainEventFilter(EventFilter):
    """
    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'error': 'bool',
        'event_type': 'str',
        'msg_direction_type': 'str',
        'server': 'str',
        'data_search': 'str',
        'metadata_search': 'str',
        'entity_name': 'str',
        'relation_type': 'str',
        'entity_id': 'str',
        'msg_type': 'str',
        'error_str': 'str'
    }
    if hasattr(EventFilter, "swagger_types"):
        swagger_types.update(EventFilter.swagger_types)

    attribute_map = {
        'error': 'error',
        'event_type': 'eventType',
        'msg_direction_type': 'msgDirectionType',
        'server': 'server',
        'data_search': 'dataSearch',
        'metadata_search': 'metadataSearch',
        'entity_name': 'entityName',
        'relation_type': 'relationType',
        'entity_id': 'entityId',
        'msg_type': 'msgType',
        'error_str': 'errorStr'
    }
    if hasattr(EventFilter, "attribute_map"):
        attribute_map.update(EventFilter.attribute_map)

    def __init__(self, error=None, event_type=None, msg_direction_type=None, server=None, data_search=None, metadata_search=None, entity_name=None, relation_type=None, entity_id=None, msg_type=None, error_str=None, *args, **kwargs):  # noqa: E501
        """DebugRuleChainEventFilter - a model defined in Swagger"""  # noqa: E501
        self._error = None
        self._event_type = None
        self._msg_direction_type = None
        self._server = None
        self._data_search = None
        self._metadata_search = None
        self._entity_name = None
        self._relation_type = None
        self._entity_id = None
        self._msg_type = None
        self._error_str = None
        self.discriminator = None
        if error is not None:
            self.error = error
        self.event_type = event_type
        if msg_direction_type is not None:
            self.msg_direction_type = msg_direction_type
        if server is not None:
            self.server = server
        if data_search is not None:
            self.data_search = data_search
        if metadata_search is not None:
            self.metadata_search = metadata_search
        if entity_name is not None:
            self.entity_name = entity_name
        if relation_type is not None:
            self.relation_type = relation_type
        if entity_id is not None:
            self.entity_id = entity_id
        if msg_type is not None:
            self.msg_type = msg_type
        if error_str is not None:
            self.error_str = error_str
        EventFilter.__init__(self, *args, **kwargs)

    @property
    def error(self):
        """Gets the error of this DebugRuleChainEventFilter.  # noqa: E501


        :return: The error of this DebugRuleChainEventFilter.  # noqa: E501
        :rtype: bool
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this DebugRuleChainEventFilter.


        :param error: The error of this DebugRuleChainEventFilter.  # noqa: E501
        :type: bool
        """

        self._error = error

    @property
    def event_type(self):
        """Gets the event_type of this DebugRuleChainEventFilter.  # noqa: E501

        String value representing the event type  # noqa: E501

        :return: The event_type of this DebugRuleChainEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this DebugRuleChainEventFilter.

        String value representing the event type  # noqa: E501

        :param event_type: The event_type of this DebugRuleChainEventFilter.  # noqa: E501
        :type: str
        """
        if event_type is None:
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501
        allowed_values = ["DEBUG_RULE_CHAIN", "DEBUG_RULE_NODE", "ERROR", "LC_EVENT", "STATS"]  # noqa: E501
        if event_type not in allowed_values:
            raise ValueError(
                "Invalid value for `event_type` ({0}), must be one of {1}"  # noqa: E501
                .format(event_type, allowed_values)
            )

        self._event_type = event_type

    @property
    def msg_direction_type(self):
        """Gets the msg_direction_type of this DebugRuleChainEventFilter.  # noqa: E501

        String value representing msg direction type (incoming to entity or outcoming from entity)  # noqa: E501

        :return: The msg_direction_type of this DebugRuleChainEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._msg_direction_type

    @msg_direction_type.setter
    def msg_direction_type(self, msg_direction_type):
        """Sets the msg_direction_type of this DebugRuleChainEventFilter.

        String value representing msg direction type (incoming to entity or outcoming from entity)  # noqa: E501

        :param msg_direction_type: The msg_direction_type of this DebugRuleChainEventFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["IN", "OUT"]  # noqa: E501
        if msg_direction_type not in allowed_values:
            raise ValueError(
                "Invalid value for `msg_direction_type` ({0}), must be one of {1}"  # noqa: E501
                .format(msg_direction_type, allowed_values)
            )

        self._msg_direction_type = msg_direction_type

    @property
    def server(self):
        """Gets the server of this DebugRuleChainEventFilter.  # noqa: E501

        String value representing the server name, identifier or ip address where the platform is running  # noqa: E501

        :return: The server of this DebugRuleChainEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this DebugRuleChainEventFilter.

        String value representing the server name, identifier or ip address where the platform is running  # noqa: E501

        :param server: The server of this DebugRuleChainEventFilter.  # noqa: E501
        :type: str
        """

        self._server = server

    @property
    def data_search(self):
        """Gets the data_search of this DebugRuleChainEventFilter.  # noqa: E501

        The case insensitive 'contains' filter based on data (key and value) for the message.  # noqa: E501

        :return: The data_search of this DebugRuleChainEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._data_search

    @data_search.setter
    def data_search(self, data_search):
        """Sets the data_search of this DebugRuleChainEventFilter.

        The case insensitive 'contains' filter based on data (key and value) for the message.  # noqa: E501

        :param data_search: The data_search of this DebugRuleChainEventFilter.  # noqa: E501
        :type: str
        """

        self._data_search = data_search

    @property
    def metadata_search(self):
        """Gets the metadata_search of this DebugRuleChainEventFilter.  # noqa: E501

        The case insensitive 'contains' filter based on metadata (key and value) for the message.  # noqa: E501

        :return: The metadata_search of this DebugRuleChainEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._metadata_search

    @metadata_search.setter
    def metadata_search(self, metadata_search):
        """Sets the metadata_search of this DebugRuleChainEventFilter.

        The case insensitive 'contains' filter based on metadata (key and value) for the message.  # noqa: E501

        :param metadata_search: The metadata_search of this DebugRuleChainEventFilter.  # noqa: E501
        :type: str
        """

        self._metadata_search = metadata_search

    @property
    def entity_name(self):
        """Gets the entity_name of this DebugRuleChainEventFilter.  # noqa: E501

        String value representing the entity type  # noqa: E501

        :return: The entity_name of this DebugRuleChainEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """Sets the entity_name of this DebugRuleChainEventFilter.

        String value representing the entity type  # noqa: E501

        :param entity_name: The entity_name of this DebugRuleChainEventFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["DEVICE"]  # noqa: E501
        if entity_name not in allowed_values:
            raise ValueError(
                "Invalid value for `entity_name` ({0}), must be one of {1}"  # noqa: E501
                .format(entity_name, allowed_values)
            )

        self._entity_name = entity_name

    @property
    def relation_type(self):
        """Gets the relation_type of this DebugRuleChainEventFilter.  # noqa: E501

        String value representing the type of message routing  # noqa: E501

        :return: The relation_type of this DebugRuleChainEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._relation_type

    @relation_type.setter
    def relation_type(self, relation_type):
        """Sets the relation_type of this DebugRuleChainEventFilter.

        String value representing the type of message routing  # noqa: E501

        :param relation_type: The relation_type of this DebugRuleChainEventFilter.  # noqa: E501
        :type: str
        """

        self._relation_type = relation_type

    @property
    def entity_id(self):
        """Gets the entity_id of this DebugRuleChainEventFilter.  # noqa: E501

        String value representing the entity id in the event body (originator of the message)  # noqa: E501

        :return: The entity_id of this DebugRuleChainEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this DebugRuleChainEventFilter.

        String value representing the entity id in the event body (originator of the message)  # noqa: E501

        :param entity_id: The entity_id of this DebugRuleChainEventFilter.  # noqa: E501
        :type: str
        """

        self._entity_id = entity_id

    @property
    def msg_type(self):
        """Gets the msg_type of this DebugRuleChainEventFilter.  # noqa: E501

        String value representing the message type  # noqa: E501

        :return: The msg_type of this DebugRuleChainEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._msg_type

    @msg_type.setter
    def msg_type(self, msg_type):
        """Sets the msg_type of this DebugRuleChainEventFilter.

        String value representing the message type  # noqa: E501

        :param msg_type: The msg_type of this DebugRuleChainEventFilter.  # noqa: E501
        :type: str
        """

        self._msg_type = msg_type

    @property
    def error_str(self):
        """Gets the error_str of this DebugRuleChainEventFilter.  # noqa: E501

        The case insensitive 'contains' filter based on error message  # noqa: E501

        :return: The error_str of this DebugRuleChainEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._error_str

    @error_str.setter
    def error_str(self, error_str):
        """Sets the error_str of this DebugRuleChainEventFilter.

        The case insensitive 'contains' filter based on error message  # noqa: E501

        :param error_str: The error_str of this DebugRuleChainEventFilter.  # noqa: E501
        :type: str
        """

        self._error_str = error_str

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
        if issubclass(DebugRuleChainEventFilter, dict):
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
        if not isinstance(other, DebugRuleChainEventFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other