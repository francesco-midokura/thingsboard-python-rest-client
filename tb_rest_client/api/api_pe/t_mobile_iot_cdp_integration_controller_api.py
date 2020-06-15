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

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from tb_rest_client.api_client import ApiClient


class TMobileIotCdpIntegrationControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.    
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def process_request_using_delete2(self, routing_key, msg, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.process_request_using_delete2(routing_key, msg, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str msg: msg (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.process_request_using_delete2_with_http_info(routing_key, msg, request_headers, **kwargs)  # noqa: E501
        else:
            (data) = self.process_request_using_delete2_with_http_info(routing_key, msg, request_headers, **kwargs)  # noqa: E501
            return data

    def process_request_using_delete2_with_http_info(self, routing_key, msg, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.process_request_using_delete2_with_http_info(routing_key, msg, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str msg: msg (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['routing_key', 'msg', 'request_headers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'routing_key' is set
        if ('routing_key' not in params or
                params['routing_key'] is None):
            raise ValueError("Missing the required parameter `routing_key` when calling `process_request_using_delete2`")  # noqa: E501
        # verify the required parameter 'msg' is set
        if ('msg' not in params or
                params['msg'] is None):
            raise ValueError("Missing the required parameter `msg` when calling `process_request_using_delete2`")  # noqa: E501
        # verify the required parameter 'request_headers' is set
        if ('request_headers' not in params or
                params['request_headers'] is None):
            raise ValueError("Missing the required parameter `request_headers` when calling `process_request_using_delete2`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'routing_key' in params:
            path_params['routingKey'] = params['routing_key']  # noqa: E501

        query_params = []

        header_params = {}
        if 'request_headers' in params:
            header_params['requestHeaders'] = params['request_headers']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'msg' in params:
            body_params = params['msg']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/integrations/tmobile_iot_cdp/{routingKey}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def process_request_using_get2(self, routing_key, msg, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.process_request_using_get2(routing_key, msg, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str msg: msg (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.process_request_using_get2_with_http_info(routing_key, msg, request_headers, **kwargs)  # noqa: E501
        else:
            (data) = self.process_request_using_get2_with_http_info(routing_key, msg, request_headers, **kwargs)  # noqa: E501
            return data

    def process_request_using_get2_with_http_info(self, routing_key, msg, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.process_request_using_get2_with_http_info(routing_key, msg, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str msg: msg (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['routing_key', 'msg', 'request_headers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'routing_key' is set
        if ('routing_key' not in params or
                params['routing_key'] is None):
            raise ValueError("Missing the required parameter `routing_key` when calling `process_request_using_get2`")  # noqa: E501
        # verify the required parameter 'msg' is set
        if ('msg' not in params or
                params['msg'] is None):
            raise ValueError("Missing the required parameter `msg` when calling `process_request_using_get2`")  # noqa: E501
        # verify the required parameter 'request_headers' is set
        if ('request_headers' not in params or
                params['request_headers'] is None):
            raise ValueError("Missing the required parameter `request_headers` when calling `process_request_using_get2`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'routing_key' in params:
            path_params['routingKey'] = params['routing_key']  # noqa: E501

        query_params = []

        header_params = {}
        if 'request_headers' in params:
            header_params['requestHeaders'] = params['request_headers']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'msg' in params:
            body_params = params['msg']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/integrations/tmobile_iot_cdp/{routingKey}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def process_request_using_head2(self, routing_key, msg, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.process_request_using_head2(routing_key, msg, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str msg: msg (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.process_request_using_head2_with_http_info(routing_key, msg, request_headers, **kwargs)  # noqa: E501
        else:
            (data) = self.process_request_using_head2_with_http_info(routing_key, msg, request_headers, **kwargs)  # noqa: E501
            return data

    def process_request_using_head2_with_http_info(self, routing_key, msg, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.process_request_using_head2_with_http_info(routing_key, msg, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str msg: msg (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['routing_key', 'msg', 'request_headers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'routing_key' is set
        if ('routing_key' not in params or
                params['routing_key'] is None):
            raise ValueError("Missing the required parameter `routing_key` when calling `process_request_using_head2`")  # noqa: E501
        # verify the required parameter 'msg' is set
        if ('msg' not in params or
                params['msg'] is None):
            raise ValueError("Missing the required parameter `msg` when calling `process_request_using_head2`")  # noqa: E501
        # verify the required parameter 'request_headers' is set
        if ('request_headers' not in params or
                params['request_headers'] is None):
            raise ValueError("Missing the required parameter `request_headers` when calling `process_request_using_head2`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'routing_key' in params:
            path_params['routingKey'] = params['routing_key']  # noqa: E501

        query_params = []

        header_params = {}
        if 'request_headers' in params:
            header_params['requestHeaders'] = params['request_headers']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'msg' in params:
            body_params = params['msg']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/integrations/tmobile_iot_cdp/{routingKey}', 'HEAD',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def process_request_using_options2(self, routing_key, msg, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.process_request_using_options2(routing_key, msg, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str msg: msg (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.process_request_using_options2_with_http_info(routing_key, msg, request_headers, **kwargs)  # noqa: E501
        else:
            (data) = self.process_request_using_options2_with_http_info(routing_key, msg, request_headers, **kwargs)  # noqa: E501
            return data

    def process_request_using_options2_with_http_info(self, routing_key, msg, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.process_request_using_options2_with_http_info(routing_key, msg, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str msg: msg (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['routing_key', 'msg', 'request_headers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'routing_key' is set
        if ('routing_key' not in params or
                params['routing_key'] is None):
            raise ValueError("Missing the required parameter `routing_key` when calling `process_request_using_options2`")  # noqa: E501
        # verify the required parameter 'msg' is set
        if ('msg' not in params or
                params['msg'] is None):
            raise ValueError("Missing the required parameter `msg` when calling `process_request_using_options2`")  # noqa: E501
        # verify the required parameter 'request_headers' is set
        if ('request_headers' not in params or
                params['request_headers'] is None):
            raise ValueError("Missing the required parameter `request_headers` when calling `process_request_using_options2`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'routing_key' in params:
            path_params['routingKey'] = params['routing_key']  # noqa: E501

        query_params = []

        header_params = {}
        if 'request_headers' in params:
            header_params['requestHeaders'] = params['request_headers']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'msg' in params:
            body_params = params['msg']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/integrations/tmobile_iot_cdp/{routingKey}', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def process_request_using_patch2(self, routing_key, msg, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.process_request_using_patch2(routing_key, msg, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str msg: msg (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.process_request_using_patch2_with_http_info(routing_key, msg, request_headers, **kwargs)  # noqa: E501
        else:
            (data) = self.process_request_using_patch2_with_http_info(routing_key, msg, request_headers, **kwargs)  # noqa: E501
            return data

    def process_request_using_patch2_with_http_info(self, routing_key, msg, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.process_request_using_patch2_with_http_info(routing_key, msg, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str msg: msg (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['routing_key', 'msg', 'request_headers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'routing_key' is set
        if ('routing_key' not in params or
                params['routing_key'] is None):
            raise ValueError("Missing the required parameter `routing_key` when calling `process_request_using_patch2`")  # noqa: E501
        # verify the required parameter 'msg' is set
        if ('msg' not in params or
                params['msg'] is None):
            raise ValueError("Missing the required parameter `msg` when calling `process_request_using_patch2`")  # noqa: E501
        # verify the required parameter 'request_headers' is set
        if ('request_headers' not in params or
                params['request_headers'] is None):
            raise ValueError("Missing the required parameter `request_headers` when calling `process_request_using_patch2`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'routing_key' in params:
            path_params['routingKey'] = params['routing_key']  # noqa: E501

        query_params = []

        header_params = {}
        if 'request_headers' in params:
            header_params['requestHeaders'] = params['request_headers']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'msg' in params:
            body_params = params['msg']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/integrations/tmobile_iot_cdp/{routingKey}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def process_request_using_post6(self, routing_key, msg, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.process_request_using_post6(routing_key, msg, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str msg: msg (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.process_request_using_post6_with_http_info(routing_key, msg, request_headers, **kwargs)  # noqa: E501
        else:
            (data) = self.process_request_using_post6_with_http_info(routing_key, msg, request_headers, **kwargs)  # noqa: E501
            return data

    def process_request_using_post6_with_http_info(self, routing_key, msg, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.process_request_using_post6_with_http_info(routing_key, msg, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str msg: msg (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['routing_key', 'msg', 'request_headers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'routing_key' is set
        if ('routing_key' not in params or
                params['routing_key'] is None):
            raise ValueError("Missing the required parameter `routing_key` when calling `process_request_using_post6`")  # noqa: E501
        # verify the required parameter 'msg' is set
        if ('msg' not in params or
                params['msg'] is None):
            raise ValueError("Missing the required parameter `msg` when calling `process_request_using_post6`")  # noqa: E501
        # verify the required parameter 'request_headers' is set
        if ('request_headers' not in params or
                params['request_headers'] is None):
            raise ValueError("Missing the required parameter `request_headers` when calling `process_request_using_post6`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'routing_key' in params:
            path_params['routingKey'] = params['routing_key']  # noqa: E501

        query_params = []

        header_params = {}
        if 'request_headers' in params:
            header_params['requestHeaders'] = params['request_headers']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'msg' in params:
            body_params = params['msg']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/integrations/tmobile_iot_cdp/{routingKey}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def process_request_using_put2(self, routing_key, msg, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.process_request_using_put2(routing_key, msg, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str msg: msg (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.process_request_using_put2_with_http_info(routing_key, msg, request_headers, **kwargs)  # noqa: E501
        else:
            (data) = self.process_request_using_put2_with_http_info(routing_key, msg, request_headers, **kwargs)  # noqa: E501
            return data

    def process_request_using_put2_with_http_info(self, routing_key, msg, request_headers, **kwargs):  # noqa: E501
        """processRequest  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.process_request_using_put2_with_http_info(routing_key, msg, request_headers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str routing_key: routingKey (required)
        :param str msg: msg (required)
        :param object request_headers: requestHeaders (required)
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['routing_key', 'msg', 'request_headers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'routing_key' is set
        if ('routing_key' not in params or
                params['routing_key'] is None):
            raise ValueError("Missing the required parameter `routing_key` when calling `process_request_using_put2`")  # noqa: E501
        # verify the required parameter 'msg' is set
        if ('msg' not in params or
                params['msg'] is None):
            raise ValueError("Missing the required parameter `msg` when calling `process_request_using_put2`")  # noqa: E501
        # verify the required parameter 'request_headers' is set
        if ('request_headers' not in params or
                params['request_headers'] is None):
            raise ValueError("Missing the required parameter `request_headers` when calling `process_request_using_put2`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'routing_key' in params:
            path_params['routingKey'] = params['routing_key']  # noqa: E501

        query_params = []

        header_params = {}
        if 'request_headers' in params:
            header_params['requestHeaders'] = params['request_headers']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'msg' in params:
            body_params = params['msg']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/integrations/tmobile_iot_cdp/{routingKey}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
