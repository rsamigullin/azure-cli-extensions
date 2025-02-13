# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "databricks workspace vnet-peering create",
)
class Create(AAZCommand):
    """Create a vnet peering for a workspace.

    :example: Create a vnet peering for a workspace
        az databricks workspace vnet-peering create --resource-group MyResourceGroup --workspace-name MyWorkspace -n MyPeering --remote-vnet /subscriptions/000000-0000-0000/resourceGroups/MyRG/providers/Microsoft.Network/virtualNetworks/MyVNet
    """

    _aaz_info = {
        "version": "2022-04-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.databricks/workspaces/{}/virtualnetworkpeerings/{}", "2022-04-01-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="The name of the vnet peering.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.workspace_name = AAZStrArg(
            options=["--workspace-name"],
            help="The name of the workspace.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                max_length=64,
                min_length=3,
            ),
        )
        _args_schema.allow_forwarded_traffic = AAZBoolArg(
            options=["--allow-forwarded-traffic"],
            help="Whether the forwarded traffic from the VMs in the local virtual network will be allowed/disallowed in remote virtual network.",
        )
        _args_schema.allow_gateway_transit = AAZBoolArg(
            options=["--allow-gateway-transit"],
            help="If gateway links can be used in remote virtual networking to link to this virtual network.",
        )
        _args_schema.allow_virtual_network_access = AAZBoolArg(
            options=["--allow-virtual-network-access"],
            help="Whether the VMs in the local virtual network space would be able to access the VMs in remote virtual network space.",
        )
        _args_schema.remote_vnet = AAZResourceIdArg(
            options=["--remote-vnet"],
            help="The remote virtual network name or Resource ID.",
            fmt=AAZResourceIdArgFormat(
                template="/subscriptions/{subscription}/resourceGroups/{resource_group}/providers/Microsoft.Network/virtualNetworks/{}"
            )
        )
        _args_schema.use_remote_gateways = AAZBoolArg(
            options=["--use-remote-gateways"],
            help="If remote gateways can be used on this virtual network. If the flag is set to true, and allowGatewayTransit on remote peering is also true, virtual network will use gateways of remote virtual network for transit. Only one peering can have this flag set to true. This flag cannot be set if virtual network already has a gateway.",
        )

        # define Arg Group "Properties"
        return cls._args_schema

    _args_address_space_create = None

    @classmethod
    def _build_args_address_space_create(cls, _schema):
        if cls._args_address_space_create is not None:
            _schema.address_prefixes = cls._args_address_space_create.address_prefixes
            return

        cls._args_address_space_create = AAZObjectArg()

        address_space_create = cls._args_address_space_create
        address_space_create.address_prefixes = AAZListArg(
            options=["address-prefixes"],
            help="A list of address blocks reserved for this virtual network in CIDR notation.",
        )

        address_prefixes = cls._args_address_space_create.address_prefixes
        address_prefixes.Element = AAZStrArg()

        _schema.address_prefixes = cls._args_address_space_create.address_prefixes

    def _execute_operations(self):
        self.pre_operations()
        yield self.VNetPeeringCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class VNetPeeringCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Databricks/workspaces/{workspaceName}/virtualNetworkPeerings/{peeringName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "peeringName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "workspaceName", self.ctx.args.workspace_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-04-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("allowForwardedTraffic", AAZBoolType, ".allow_forwarded_traffic")
                properties.set_prop("allowGatewayTransit", AAZBoolType, ".allow_gateway_transit")
                properties.set_prop("allowVirtualNetworkAccess", AAZBoolType, ".allow_virtual_network_access")
                properties.set_prop("remoteVirtualNetwork", AAZObjectType, ".", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("useRemoteGateways", AAZBoolType, ".use_remote_gateways")

            remote_virtual_network = _builder.get(".properties.remoteVirtualNetwork")
            if remote_virtual_network is not None:
                remote_virtual_network.set_prop("id", AAZStrType, ".remote_vnet")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.allow_forwarded_traffic = AAZBoolType(
                serialized_name="allowForwardedTraffic",
            )
            properties.allow_gateway_transit = AAZBoolType(
                serialized_name="allowGatewayTransit",
            )
            properties.allow_virtual_network_access = AAZBoolType(
                serialized_name="allowVirtualNetworkAccess",
            )
            properties.databricks_address_space = AAZObjectType(
                serialized_name="databricksAddressSpace",
            )
            _build_schema_address_space_read(properties.databricks_address_space)
            properties.databricks_virtual_network = AAZObjectType(
                serialized_name="databricksVirtualNetwork",
            )
            properties.peering_state = AAZStrType(
                serialized_name="peeringState",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.remote_address_space = AAZObjectType(
                serialized_name="remoteAddressSpace",
            )
            _build_schema_address_space_read(properties.remote_address_space)
            properties.remote_virtual_network = AAZObjectType(
                serialized_name="remoteVirtualNetwork",
                flags={"required": True},
            )
            properties.use_remote_gateways = AAZBoolType(
                serialized_name="useRemoteGateways",
            )

            databricks_virtual_network = cls._schema_on_200_201.properties.databricks_virtual_network
            databricks_virtual_network.id = AAZStrType()

            remote_virtual_network = cls._schema_on_200_201.properties.remote_virtual_network
            remote_virtual_network.id = AAZStrType()

            return cls._schema_on_200_201


def _build_schema_address_space_create(_builder):
    if _builder is None:
        return
    _builder.set_prop("addressPrefixes", AAZListType, ".address_prefixes")

    address_prefixes = _builder.get(".addressPrefixes")
    if address_prefixes is not None:
        address_prefixes.set_elements(AAZStrType, ".")


_schema_address_space_read = None


def _build_schema_address_space_read(_schema):
    global _schema_address_space_read
    if _schema_address_space_read is not None:
        _schema.address_prefixes = _schema_address_space_read.address_prefixes
        return

    _schema_address_space_read = AAZObjectType()

    address_space_read = _schema_address_space_read
    address_space_read.address_prefixes = AAZListType(
        serialized_name="addressPrefixes",
    )

    address_prefixes = _schema_address_space_read.address_prefixes
    address_prefixes.Element = AAZStrType()

    _schema.address_prefixes = _schema_address_space_read.address_prefixes


__all__ = ["Create"]
