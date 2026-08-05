"""AssetInterfacesDescription — generated from IDTA template."""

from __future__ import annotations

from typing import Any, ClassVar, List, Dict, TypeAlias
from aas_pydantic import (
    ContainerValue, File, Property, Range, ReferenceElement, Submodel, SubmodelElement, SubmodelElementCollection, SubmodelElementList,
)
from pydantic import Field

class security(SubmodelElementList):
    semantic_id: str = "https://www.w3.org/2019/wot/td#hasSecurityConfiguration"
    description: str = "Selects one or more of the security scheme(s) that can be applied at runtime from the collection of security schemes defines in securityDefinitions. "
    item_type: ClassVar = ReferenceElement
    value: List[ReferenceElement] = [
                ReferenceElement(
            semantic_id="https://www.w3.org/2019/wot/td#hasSecurityConfiguration",
            description="ReferenceElement within the SML points to a sercurity scheme definition in the SMC securityDefinitions.",
        ),
    ]

class nosec_scValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. the scheme for nosec_sc is nosec",
        value_type="xs:string",
    )

class nosec_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#NoSecurityScheme"
    description: str = "This SubmodelElements holds the information about security mechanism based on nosec security."
    value: nosec_scValues = nosec_scValues()

class auto_scValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. The scheme for auto_sc is auto.",
        value_type="xs:string",
    )
    proxy: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#proxy",
        description="Provides address information of the proxy server the security configuration provides access to.",
        value_type="xs:string",
    )

class auto_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#AutoSecurityScheme"
    description: str = "This SubmodelElements holds the information about security mechanism based on auto security."
    value: auto_scValues = auto_scValues()

class basic_scValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. The scheme for basic_sc is basic.",
        value_type="xs:string",
    )
    name: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#name",
        description="Name for query, header, cookie, or uri parameters",
        value_type="xs:string",
    )
    in_: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#in",
        description="Specifies the location of security authentication information. Proposed values are header, query, body, cookie or auto",
        value_type="xs:string",
    )
    proxy: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#proxy",
        description="Provides address information of the proxy server the security configuration provides access to.",
        value_type="xs:string",
    )

class basic_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#BasicSecurityScheme"
    description: str = "This SubmodelElements holds the information about security mechanism based on basic security."
    value: basic_scValues = basic_scValues()

class oneOf(SubmodelElementList):
    semantic_id: str = "https://www.w3.org/2019/wot/security#oneOf"
    description: str = "Specifies alternative security schemes where at least one listed scheme can be used."
    value: List[Any] = []

class allOf(SubmodelElementList):
    semantic_id: str = "https://www.w3.org/2019/wot/security#allOf"
    description: str = "Specifies a combined security configuration where all listed schemes are applied together."
    value: List[Any] = []

class combo_scValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. The scheme for combo_sc is combo.",
        value_type="xs:string",
    )
    one_of: oneOf = oneOf()
    all_of: allOf = allOf()
    proxy: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#proxy",
        description="Provides address information of the proxy server the security configuration provides access to.",
        value_type="xs:string",
    )

class combo_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#ComboSecurityScheme"
    description: str = "This SubmodelElements holds the information about security mechanism based on combo security."
    value: combo_scValues = combo_scValues()

class apikey_scValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. The scheme for apikey_sc is apikey.",
        value_type="xs:string",
    )
    name: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#name",
        description="Name for query, header, cookie, or uri parameters.",
        value_type="xs:string",
    )
    in_: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#in",
        description="Specifies the location of security authentication information. Proposed values are header, query, body, cookie or auto.",
        value_type="xs:string",
    )
    proxy: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#proxy",
        description="Provides address information of the proxy server the security configuration provides access to.",
        value_type="xs:string",
    )

class apikey_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#APIKeySecurityScheme"
    description: str = "This SubmodelElements holds the information about security mechanism based on apikey security."
    value: apikey_scValues = apikey_scValues()

class psk_scValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. The scheme for psk_sc is psk.",
        value_type="xs:string",
    )
    identity: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#identity",
        description="Identifier providing information which can be used for selection or confirmation.",
        value_type="xs:string",
    )
    proxy: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#proxy",
        description="Provides address information of the proxy server the security configuration provides access to.",
        value_type="xs:string",
    )

class psk_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#PSKSecurityScheme"
    description: str = "This SubmodelElements holds the information about security mechanism based on psk security."
    value: psk_scValues = psk_scValues()

class digest_scValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. The scheme for digest_sc is digest.",
        value_type="xs:string",
    )
    name: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#name",
        description="Name for query, header, cookie, or uri parameters.",
        value_type="xs:string",
    )
    in_: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#in",
        description="Specifies the location of security authentication information. Proposed values are header, query, body, cookie or auto",
        value_type="xs:string",
    )
    qop: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#qop",
        description="Defines Quality of protection. Values is one of auth or auth-int",
        value_type="xs:string",
    )
    proxy: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#proxy",
        description="Provides address information of the proxy server the security configuration provides access to.",
        value_type="xs:string",
    )

class digest_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#DigestSecurityScheme"
    description: str = "This SubmodelElements holds the information about security mechanism based on digest security."
    value: digest_scValues = digest_scValues()

class bearer_scValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. The scheme for bearer_sc is bearer.",
        value_type="xs:string",
    )
    name: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#name",
        description="Name for query, header, cookie, or uri parameters.",
        value_type="xs:string",
    )
    in_: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#in",
        description="Specifies the location of security authentication information. Proposed values are header, query, body, cookie or auto.",
        value_type="xs:string",
    )
    authorization: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#authorization",
        description="Specifies URI of the authorization server.",
        value_type="xs:string",
    )
    alg: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#alg",
        description="Defines Encoding, encryption, or digest algorithm (e.g. ES256, ES512-256).",
        value_type="xs:string",
    )
    format: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#format",
        description="Specifies format of security authentication information. Options as value are jwt, cwt, jwe or jws",
        value_type="xs:string",
    )
    proxy: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#proxy",
        description="Provides address information of the proxy server the security configuration provides access to.",
        value_type="xs:string",
    )

class bearer_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#BearerSecurityScheme"
    description: str = "This SubmodelElements holds the information about security mechanism based on bearer security."
    value: bearer_scValues = bearer_scValues()

class scopes(SubmodelElementList):
    semantic_id: str = "https://www.w3.org/2019/wot/security#scopes"
    description: str = "Set of authorization scope identifiers (as Property) provided as an array. These are provided in tokens returned by an authorization server and associated with forms in order to identify what resources a client may access and how."
    value: List[Any] = []

# alias so field ``scopes_t`` can name a class of the same id_short
scopes_t: TypeAlias = scopes
class oauth2_scValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. The scheme for oauth2_sc is oauth2.",
        value_type="xs:string",
    )
    token: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#token",
        description="Specifies URI of the token server.",
        value_type="xs:anyURI",
    )
    refresh: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#refresh",
        description="Specifies URI of the refresh server.",
        value_type="xs:anyURI",
    )
    authorization: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#authorization",
        description="Specifies URI of the authorization server.",
        value_type="xs:anyURI",
    )
    scopes: scopes_t = scopes_t()
    flow: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#flow",
        description="Defines authorization flow such as code or client.",
        value_type="xs:string",
    )
    proxy: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#proxy",
        description="Provides address information of the proxy server the security configuration provides access to.",
        value_type="xs:anyURI",
    )

class oauth2_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#OAuth2SecurityScheme"
    description: str = "This SubmodelElements holds the information about security mechanism based on oauth2 security."
    value: oauth2_scValues = oauth2_scValues()

# alias so field ``nosec_sc_t`` can name a class of the same id_short
nosec_sc_t: TypeAlias = nosec_sc
# alias so field ``auto_sc_t`` can name a class of the same id_short
auto_sc_t: TypeAlias = auto_sc
# alias so field ``basic_sc_t`` can name a class of the same id_short
basic_sc_t: TypeAlias = basic_sc
# alias so field ``combo_sc_t`` can name a class of the same id_short
combo_sc_t: TypeAlias = combo_sc
# alias so field ``apikey_sc_t`` can name a class of the same id_short
apikey_sc_t: TypeAlias = apikey_sc
# alias so field ``psk_sc_t`` can name a class of the same id_short
psk_sc_t: TypeAlias = psk_sc
# alias so field ``digest_sc_t`` can name a class of the same id_short
digest_sc_t: TypeAlias = digest_sc
# alias so field ``bearer_sc_t`` can name a class of the same id_short
bearer_sc_t: TypeAlias = bearer_sc
# alias so field ``oauth2_sc_t`` can name a class of the same id_short
oauth2_sc_t: TypeAlias = oauth2_sc
class securityDefinitionsValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    nosec_sc: nosec_sc_t = nosec_sc_t()
    auto_sc: auto_sc_t = auto_sc_t()
    basic_sc: basic_sc_t = basic_sc_t()
    combo_sc: combo_sc_t = combo_sc_t()
    apikey_sc: apikey_sc_t = apikey_sc_t()
    psk_sc: psk_sc_t = psk_sc_t()
    digest_sc: digest_sc_t = digest_sc_t()
    bearer_sc: bearer_sc_t = bearer_sc_t()
    oauth2_sc: oauth2_sc_t = oauth2_sc_t()

class securityDefinitions(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/td#definesSecurityScheme"
    description: str = "Defines the security scheme according to W3C"
    value: securityDefinitionsValues = securityDefinitionsValues()

# alias so field ``security_t`` can name a class of the same id_short
security_t: TypeAlias = security
class EndpointMetadataValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    base: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#baseURI",
        description="Defines asset connection entry point. The base pattern for HTTP is defined in Qalifier.",
        value_type="xs:anyURI",
    )
    content_type: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/hypermedia#forContentType",
        description="Defines content type based on a media type (e.g., text/plain) and potential character decoding/encoding type (e.g., charset=utf-8) for the media type (see RFC2046) of the whole interface.",
        value_type="xs:string",
    )
    security: security_t = security_t()
    security_definitions: securityDefinitions = securityDefinitions()

class EndpointMetadata(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/EndpointMetadata"
    description: str = "Provides the metadata of the asset\u2019s endpoint (base, content type that is used for interaction, etc)"
    value: EndpointMetadataValues = EndpointMetadataValues()

class enum(SubmodelElementList):
    semantic_id: str = "https://www.w3.org/2019/wot/json-schema#enum"
    description: str = "Provides a list of restricted set of values that the asset can provide as datapoint value."
    value: List[Any] = []

# alias so field ``enum_t`` can name a class of the same id_short
enum_t: TypeAlias = enum
class itemsValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    type: Property = Property(
        semantic_id="https://www.w3.org/1999/02/22-rdf-syntax-ns#type",
        description="Indicates the abstract data type (one of object, array, string, number, integer, boolean, or null) of the described datapoint.",
        value_type="xs:string",
    )
    title: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#title",
        description="Provides a human-readable title of this interaction (e.g., display a text for UI representation)",
        value_type="xs:string",
    )
    observable: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#isObservable",
        description="An indicator that tells that the interaction datapoint can be observed with a, e.g., subscription mechanism by an underlying protocol.",
        value_type="xs:boolean",
    )
    const: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/json-schema#const",
        description="Provides a constant value for defined datapoint. The data type should be identical to the one provided by the Property type.",
        value_type="xs:int",
    )
    enum: enum_t = enum_t()
    default: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/json-schema#default",
        description="Provides a default value that must of the type as the datapoint valueType. The data type should be identical to the one as provided by the Property type.",
        value_type="xs:string",
    )
    unit: Property = Property(
        semantic_id="https://schema.org/unitCode",
        description="Provides information about the datapoint\u2019s unit.",
        value_type="xs:string",
    )
    min_max: Range = Range(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange",
        description="Specifies a minimum and/or maximum numeric value for the datapoint. This term is only used when type element is number or integer. When it is number, the range data type has to be float and when it is integer, the range data type has to be integer ",
        value_type="xs:string",
    )
    length_range: Range = Range(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange",
        description="Specifies the minimum and maximum length of a string.",
        value_type="xs:string",
    )
    value_semantics: ReferenceElement = ReferenceElement(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics",
        description="Provides additional semantic information of the value that is read/subscribed at runtime. ",
    )

class items(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/json-schema#items"
    description: str = "Used to define the data schema characteristics (as specified within Section 2.9) of an array payload."
    value: itemsValues = itemsValues()

class htv_headerValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    htv_field_name: Property = Property(
        semantic_id="https://www.w3.org/2011/http#fieldName",
        description="Defines message header name ",
        value_type="xs:string",
    )
    htv_field_value: Property = Property(
        semantic_id="https://www.w3.org/2011/http#fieldValue",
        description="Defines message header value",
        value_type="xs:string",
    )

class htv_header(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2011/http#headers"
    description: str = "Defines message header content "
    value: htv_headerValues = htv_headerValues()

class htv_headers(SubmodelElementList):
    semantic_id: str = "https://www.w3.org/2011/http#headers"
    description: str = "Defines additional information to be sent within the HTTP header message."
    item_type: ClassVar = htv_header
    value: List[htv_header] = [
        htv_header(id_short="htv_header"),
    ]

# alias so field ``htv_headers_t`` can name a class of the same id_short
htv_headers_t: TypeAlias = htv_headers
class formsValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    href: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/hypermedia#hasTarget",
        description="Indicates target IRI relative path or full IRI of asset\u2019s datapoint. The relative endpoint definition in href is always relative to base defined in EndpointMetadata. ",
        value_type="xs:string",
    )
    content_type: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/hypermedia#forContentType",
        description="Indicates the datapoint media type specified by IANA.Note: this local definition overwrites the globally defined contentType specified in EndpointMetadata (if it exists).",
        value_type="xs:string",
    )
    subprotocol: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/hypermedia#forSubProtocol",
        description="Indicates the exact mechanism by which an interaction will be accomplished for a given protocol when there are multiple options.",
        value_type="xs:string",
    )
    security: security_t = security_t()
    htv_method_name: Property = Property(
        semantic_id="https://www.w3.org/2011/http#methodName",
        description="Defines the action to be performed datapoint IRI",
        value_type="xs:string",
    )
    htv_headers: htv_headers_t = htv_headers_t()

class forms(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/td#hasForm"
    description: str = "Contains information about datapoint resource location. Note, forms is only available at the top level {property_name}"
    value: formsValues = formsValues()

# alias so field ``items_t`` can name a class of the same id_short
items_t: TypeAlias = items
# alias so field ``forms_t`` can name a class of the same id_short
forms_t: TypeAlias = forms
class property_nameValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    key: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/0/key",
        description="Optional element when the idShort of {property_name} cannot be used to reflect the desired property name due to the idShort restrictions (e.g., payload message uses \u201ctemperature-value\u201d as key term).",
        value_type="xs:string",
    )
    type: Property = Property(
        semantic_id="https://www.w3.org/1999/02/22-rdf-syntax-ns#type",
        description="Indicates the abstract data type (one of object, array, string, number, integer, boolean, or null) of the described datapoint.",
        value_type="xs:string",
    )
    title: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#title",
        description="Provides a human-readable title of this interaction (e.g., display a text for UI representation)",
        value_type="xs:string",
    )
    observable: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#isObservable",
        description="An indicator that tells that the interaction datapoint can be observed with a, e.g., subscription mechanism by an underlying protocol.",
        value_type="xs:boolean",
    )
    const: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/json-schema#const",
        description="Provides a constant value for defined datapoint. The data type should be identical to the one provided by the Property type.",
        value_type="xs:int",
    )
    enum: enum_t = enum_t()
    default: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/json-schema#default",
        description="Provides a default value that must of the type as the datapoint valueType. The data type should be identical to the one as provided by the Property type.",
        value_type="xs:string",
    )
    unit: Property = Property(
        semantic_id="https://schema.org/unitCode",
        description="Provides information about the datapoint\u2019s unit.",
        value_type="xs:string",
    )
    min_max: Range = Range(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange",
        description="Specifies a minimum and/or maximum numeric value for the datapoint. This term is only used when type element is number or integer. When it is number, the range data type has to be float and when it is integer, the range data type has to be integer ",
        value_type="xs:string",
    )
    length_range: Range = Range(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange",
        description="Specifies the minimum and maximum length of a string.",
        value_type="xs:string",
    )
    items: items_t = items_t()
    items_range: Range = Range(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/0/itemsRange",
        description="Defines the minimum and maximum number of items that have to be in an array payload.",
        value_type="xs:string",
    )
    value_semantics: ReferenceElement = ReferenceElement(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics",
        description="Provides additional semantic information of the value that is read/subscribed at runtime. ",
    )
    forms: forms_t = forms_t()

class property_name(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/PropertyDefinition"
    description: str = "Defines an interaction property that covers usually a datapoint definition that can be read or subscribed to.  "
    supplemental_semantic_ids: List[str] = ["https://www.w3.org/2019/wot/td#name"]
    value: property_nameValues = property_nameValues()

# alias so field ``property_name_t`` can name a class of the same id_short
property_name_t: TypeAlias = property_name
class propertiesValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    property_name: Dict[str, property_name_t] = {}

class properties(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/td#PropertyAffordance"
    description: str = "Collection of asset\u2019s datapoint definitions"
    value: propertiesValues = propertiesValues()

class actionsValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    pass

class actions(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/td#ActionAffordance"
    description: str = "Collection of functions that can be done on asset as action SMC"
    value: actionsValues = actionsValues()

class eventsValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    pass

class events(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/td#EventAffordance"
    description: str = "Collection of events triggerable by datapoint state as event SMC"
    value: eventsValues = eventsValues()

# alias so field ``properties_t`` can name a class of the same id_short
properties_t: TypeAlias = properties
# alias so field ``actions_t`` can name a class of the same id_short
actions_t: TypeAlias = actions
# alias so field ``events_t`` can name a class of the same id_short
events_t: TypeAlias = events
class InteractionMetadataValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    properties: properties_t = properties_t()
    actions: actions_t = actions_t()
    events: events_t = events_t()

class InteractionMetadata(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/InteractionMetadata"
    description: str = "Provides the metadata of the actually interfaces such as which datapoints and functions are provided by the properties, actions, and events interaction abstraction. "
    supplemental_semantic_ids: List[str] = ["https://www.w3.org/2019/wot/td#InteractionAffordance"]
    value: InteractionMetadataValues = InteractionMetadataValues()

class ExternalDescriptorValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    file_name: File = File(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/0/externalDescriptorName",
        description="File reference (local in AASX or outside) to an external descriptor description (e.g., Thing Description, GSDML, MTP, etc,).  ",
    )

class ExternalDescriptor(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/ExternalDescriptor"
    description: str = "Provides a place for existing description files (e.g., Thing Description, GSDML, etc,)."
    value: ExternalDescriptorValues = ExternalDescriptorValues()

class InterfaceTemplateForHTTPValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    title: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#title",
        description="Provides a human-readable title to give a human-readable context of the interface.",
        value_type="xs:string",
    )
    created: Property = Property(
        semantic_id="http://purl.org/dc/terms/created",
        description="Provides information when the AID Submodel was created.",
        value_type="xs:dateTime",
    )
    modified: Property = Property(
        semantic_id="http://purl.org/dc/terms/modified",
        description="Provides information when the AID Submodel was modified.",
        value_type="xs:dateTime",
    )
    support: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#supportContact",
        description="Provides an address on how to contact the maintainer of AID Submodel as URI scheme.",
        value_type="xs:anyURI",
    )
    endpoint_metadata: EndpointMetadata = EndpointMetadata()
    interaction_metadata: InteractionMetadata = InteractionMetadata()
    external_descriptor: ExternalDescriptor = ExternalDescriptor()

class InterfaceTemplateForHTTP(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/Interface"
    description: str = "Indicates entry point for HTTP interface."
    supplemental_semantic_ids: List[str] = ["http://www.w3.org/2011/http", "https://www.w3.org/2019/wot/td"]
    value: InterfaceTemplateForHTTPValues = InterfaceTemplateForHTTPValues()

class InterfaceTemplateForMODBUSValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    title: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#title",
        description="Provides a human-readable title to give a human-readable context of the interface.",
        value_type="xs:string",
    )
    created: Property = Property(
        semantic_id="http://purl.org/dc/terms/created",
        description="Provides information when the AID Submodel was created.",
        value_type="xs:dateTime",
    )
    modified: Property = Property(
        semantic_id="http://purl.org/dc/terms/modified",
        description="Provides information when the AID Submodel was modified.",
        value_type="xs:dateTime",
    )
    support: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#supportContact",
        description="Provides an address on how to contact the maintainer of AID Submodel as URI scheme.",
        value_type="xs:anyURI",
    )
    endpoint_metadata: EndpointMetadata = EndpointMetadata()
    interaction_metadata: InteractionMetadata = InteractionMetadata()
    external_descriptor: ExternalDescriptor = ExternalDescriptor()

class InterfaceTemplateForMODBUS(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/Interface"
    description: str = "Indicates entry point for MODBUS interface."
    supplemental_semantic_ids: List[str] = ["http://www.w3.org/2011/modbus", "https://www.w3.org/2019/wot/td"]
    value: InterfaceTemplateForMODBUSValues = InterfaceTemplateForMODBUSValues()

class InterfaceTemplateForMQTTValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    title: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#title",
        description="Provides a human-readable title to give a human-readable context of the interface.",
        value_type="xs:string",
    )
    created: Property = Property(
        semantic_id="http://purl.org/dc/terms/created",
        description="Provides information when the AID Submodel was created.",
        value_type="xs:dateTime",
    )
    modified: Property = Property(
        semantic_id="http://purl.org/dc/terms/modified",
        description="Provides information when the AID Submodel was modified.",
        value_type="xs:dateTime",
    )
    support: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#supportContact",
        description="Provides an address on how to contact the maintainer of AID Submodel as URI scheme.",
        value_type="xs:anyURI",
    )
    endpoint_metadata: EndpointMetadata = EndpointMetadata()
    interaction_metadata: InteractionMetadata = InteractionMetadata()
    external_descriptor: ExternalDescriptor = ExternalDescriptor()

class InterfaceTemplateForMQTT(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/Interface"
    description: str = "Indicates entry point for MQTT interface."
    supplemental_semantic_ids: List[str] = ["http://www.w3.org/2011/mqtt", "https://www.w3.org/2019/wot/td"]
    value: InterfaceTemplateForMQTTValues = InterfaceTemplateForMQTTValues()

class opcua_channel_scValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. The scheme for opcua_channel_sc is ua_channelsec.",
        value_type="xs:string",
    )
    proxy: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#proxy",
        description="Provides address information of the proxy server the security configuration provides access to.",
        value_type="xs:string",
    )
    uav_security_mode: Property = Property(
        semantic_id="http://opcfoundation.org/UA/WoT-Binding/securityMode ",
        description="Provides information about the security modes supported by the OPC UA server endpoint(e.g None, Sign,SignAndEncrypt)",
        value_type="xs:string",
    )
    uav_security_policy: Property = Property(
        semantic_id="http://opcfoundation.org/UA/WoT-Binding/securityPolicy",
        description="Provides information about which policy options are available from the supported endpoints of the OPC UA server(e.g None, Basic256Sha256)",
        value_type="xs:string",
    )

class opcua_channel_sc(SubmodelElementCollection):
    semantic_id: str = "http://opcfoundation.org/UA/WoT-Binding/OPCUASecurityChannelScheme"
    description: str = "This SubmodelElements holds the information about security mechanism based on opcua_channel security."
    value: opcua_channel_scValues = opcua_channel_scValues()

class opcua_authentication_scValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. The scheme for opcua_authentication_sc is ua_authentication.",
        value_type="xs:string",
    )
    proxy: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#proxy",
        description="Provides address information of the proxy server the security configuration provides access to.",
        value_type="xs:string",
    )
    uav_user_identity_token: Property = Property(
        semantic_id="http://opcfoundation.org/UA/WoT-Binding/userIdentityToken",
        description="Provides information about which policy options are available from the supported endpoints of the OPC UA server (e.g Anonymous)",
        value_type="xs:string",
    )
    uav_issue_token: ReferenceElement = ReferenceElement(
        semantic_id="http://opcfoundation.org/UA/WoT-Binding/issueToken",
        description="Provides reference to security scheme within SecurityDefinition SMC that holds information about the token to use (e.g OAuth2).",
    )

class opcua_authentication_sc(SubmodelElementCollection):
    semantic_id: str = "http://opcfoundation.org/UA/WoT-Binding/OPCUASecurityAuthenticationScheme "
    description: str = "This SubmodelElements holds the information about security mechanism based on opcua_authentication security."
    value: opcua_authentication_scValues = opcua_authentication_scValues()

class InterfaceTemplateForOPCUAValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    title: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#title",
        description="Provides a human-readable title to give a human-readable context of the interface.",
        value_type="xs:string",
    )
    created: Property = Property(
        semantic_id="http://purl.org/dc/terms/created",
        description="Provides information when the AID Submodel was created.",
        value_type="xs:dateTime",
    )
    modified: Property = Property(
        semantic_id="http://purl.org/dc/terms/modified",
        description="Provides information when the AID Submodel was modified.",
        value_type="xs:dateTime",
    )
    support: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#supportContact",
        description="Provides an address on how to contact the maintainer of AID Submodel as URI scheme.",
        value_type="xs:anyURI",
    )
    endpoint_metadata: EndpointMetadata = EndpointMetadata()
    interaction_metadata: InteractionMetadata = InteractionMetadata()
    external_descriptor: ExternalDescriptor = ExternalDescriptor()

class InterfaceTemplateForOPCUA(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/Interface"
    description: str = "Indicates entry point for OPC UA interface."
    supplemental_semantic_ids: List[str] = ["http://opcfoundation.org/UA/WoT-Binding/", "https://www.w3.org/2019/wot/td"]
    value: InterfaceTemplateForOPCUAValues = InterfaceTemplateForOPCUAValues()

class uriVariablesValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    property_name: Dict[str, uriVariables] = {}

class uriVariables(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/td#hasUriTemplateSchema"
    description: str = "Defines URI template variables according to RFC6570 as a collection based on an interaction affordance data schema"
    value: uriVariablesValues = Field(default_factory=uriVariablesValues)

class bacv_hasNamedMember(SubmodelElementList):
    semantic_id: str = "http://www.w3.org/2022/bacnet#hasNamedMember"
    description: str = "Defines the Named Member of a Sequence or Choice data type."
    value: List[Any] = []

class bacv_hasValueMap(SubmodelElementList):
    semantic_id: str = "http://www.w3.org/2022/bacnet#hasValueMap"
    description: str = "Defines the value map of an enumeration."
    value: List[Any] = []

class bacv_hasMemberValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    bacv_is_i_s_o8601: Property = Property(
        semantic_id="http://www.w3.org/2022/bacnet#isIso8601",
        description="Current counter value",
        value_type="xs:boolean",
    )
    bacv_has_binary_representation: Property = Property(
        semantic_id="http://www.w3.org/2022/bacnet#hasBinaryRepresentation",
        description="Current counter value",
        value_type="xs:boolean",
    )
    bacv_has_named_member: bacv_hasNamedMember = bacv_hasNamedMember()
    bacv_has_value_map: bacv_hasValueMap = bacv_hasValueMap()

class bacv_hasMember(SubmodelElementCollection):
    semantic_id: str = "http://www.w3.org/2022/bacnet#hasMember"
    description: str = "Defines the member of a Sequence and List data type."
    value: bacv_hasMemberValues = bacv_hasMemberValues()

class bacv_hasDataTypeValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    bacv_is_i_s_o8601: Property = Property(
        semantic_id="http://www.w3.org/2022/bacnet#isIso8601",
        description="Defines if the data uses ISO8601 format",
        value_type="xs:boolean",
    )
    bacv_has_binary_representation: Property = Property(
        semantic_id="http://www.w3.org/2022/bacnet#hasBinaryRepresentation",
        description="Defines the payload\u2019s binary representation type. This term is used when the payload is an OctetString",
        value_type="xs:boolean",
    )
    bacv_has_member: bacv_hasMember = bacv_hasMember()
    bacv_has_named_member: bacv_hasNamedMember = bacv_hasNamedMember()
    bacv_has_value_map: bacv_hasValueMap = bacv_hasValueMap()

class bacv_hasDataType(SubmodelElementCollection):
    semantic_id: str = "http://www.w3.org/2022/bacnet#hasDataType"
    description: str = "Defines the type information of a BACnet payload. This SMC is used to abstract BACnet data model to human and machine readable model by still keeping its wire compatibility on the protocol."
    supplemental_semantic_ids: List[str] = ["http://www.w3.org/2022/bacnet#SequenceOf", "http://www.w3.org/2022/bacnet#Sequence", "http://www.w3.org/2022/bacnet#List", "http://www.w3.org/2022/bacnet#Choice", "http://www.w3.org/2022/bacnet#Date", "http://www.w3.org/2022/bacnet#Time", "http://www.w3.org/2022/bacnet#WeekNDay", "http://www.w3.org/2022/bacnet#Unsigned", "http://www.w3.org/2022/bacnet#Signed", "http://www.w3.org/2022/bacnet#Real", "http://www.w3.org/2022/bacnet#Double", "http://www.w3.org/2022/bacnet#Boolean", "http://www.w3.org/2022/bacnet#Enumerated", "http://www.w3.org/2022/bacnet#String", "http://www.w3.org/2022/bacnet#OctetString", "http://www.w3.org/2022/bacnet#BitString", "http://www.w3.org/2022/bacnet#Any", "http://www.w3.org/2022/bacnet#Null", "http://www.w3.org/2022/bacnet#ObjectIdentifier"]
    value: bacv_hasDataTypeValues = bacv_hasDataTypeValues()

class InterfaceTemplateForBacnetValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    title: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#title",
        description="Provides a human-readable title to give a human-readable context of the interface.",
        value_type="xs:string",
    )
    created: Property = Property(
        semantic_id="http://purl.org/dc/terms/created",
        description="Provides information when the AID Submodel was created.",
        value_type="xs:dateTime",
    )
    modified: Property = Property(
        semantic_id="http://purl.org/dc/terms/modified",
        description="Provides information when the AID Submodel was modified.",
        value_type="xs:dateTime",
    )
    support: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#supportContact",
        description="Provides an address on how to contact the maintainer of AID Submodel as URI scheme.",
        value_type="xs:anyURI",
    )
    endpoint_metadata: EndpointMetadata = EndpointMetadata()
    interaction_metadata: InteractionMetadata = InteractionMetadata()
    external_descriptor: ExternalDescriptor = ExternalDescriptor()

class InterfaceTemplateForBacnet(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/Interface"
    description: str = "Indicates entry point for BACnet interface."
    supplemental_semantic_ids: List[str] = ["http://www.w3.org/2022/bacnet", "https://www.w3.org/2019/wot/td"]
    value: InterfaceTemplateForBacnetValues = InterfaceTemplateForBacnetValues()

class iolv_enumeratedValueValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    iolv_encoded_payload: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/encodedPayload",
        description="Specifies the presentation of the payload Logical encoding.  ",
        value_type="xs:string",
    )
    iolv_decoded_payload: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/decodedPayload",
        description="Specifies the human readable meaning of the payload Logical encoding.  ",
        value_type="xs:integer",
    )

class iolv_enumeratedValue(SubmodelElementCollection):
    semantic_id: str = "http://www.w3.org/2022/wot/iolink#EnumeratedValue"
    description: str = "Defines the logical semantic to encoded payload provided a byte or byte stream."
    value: iolv_enumeratedValueValues = iolv_enumeratedValueValues()

class iolv_enumeratedValues(SubmodelElementList):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/hasEnumeratedValues"
    description: str = "Contains a list of enumerated values that define the logical semantic to encoded payload provided a byte or byte stream. "
    item_type: ClassVar = iolv_enumeratedValue
    value: List[iolv_enumeratedValue] = [
        iolv_enumeratedValue(id_short="iolv_enumeratedValue"),
    ]

class iolv_payloadMappingElementValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    iolv_reference_to_property: ReferenceElement = ReferenceElement(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/referenceToProperty",
        description="Defined the reference to a nested datapoint of an object type datapoint. ",
    )
    iolv_type: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/hasPayloadDataType",
        description="Specifies the data type contained in the request or response payload. ",
        value_type="xs:string",
    )
    iolv_byte_offset: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/byteOffset",
        description="For object type datapoints. Used to identify the starting point within a byte stream payload that represents a datapoint.",
        value_type="xs:string",
    )
    iolv_byte_length: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/byteLength",
        description="For object type datapoints. Used to identify the byte length within a byte stream payload that represents a datapoint.",
        value_type="xs:string",
    )
    iolv_bit_offset: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/bitOffset",
        description="For object type datapoints. Used to identify the starting point within a bit stream payload that represents a datapoint.",
        value_type="xs:integer",
    )
    iolv_bit_length: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/bitLength",
        description="For object type datapoints. Used to identify the bit length of a datapoint from the bit stream payload.",
        value_type="xs:string",
    )
    iolv_enumerated_values: iolv_enumeratedValues = iolv_enumeratedValues()

class iolv_payloadMappingElement(SubmodelElementCollection):
    semantic_id: str = "http://www.w3.org/2022/wot/iolink#PayloadMapping"
    description: str = "Defines the payload mapping associated to a datapoint."
    value: iolv_payloadMappingElementValues = iolv_payloadMappingElementValues()

class iolv_payloadMapping(SubmodelElementList):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/hasPayloadMapping"
    description: str = "For object type datapoints. Used to provides logical mapping information of a complex payload from a IO lInk device."
    item_type: ClassVar = iolv_payloadMappingElement
    value: List[iolv_payloadMappingElement] = [
        iolv_payloadMappingElement(id_short="iolv_payloadMappingElement"),
    ]

class InterfaceTemplateForIOLINK_OVER_PROFINET_RESTValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    title: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#title",
        description="Provides a human-readable title to give a human-readable context of the interface.",
        value_type="xs:string",
    )
    created: Property = Property(
        semantic_id="http://purl.org/dc/terms/created",
        description="Provides information when the AID Submodel was created.",
        value_type="xs:dateTime",
    )
    modified: Property = Property(
        semantic_id="http://purl.org/dc/terms/modified",
        description="Provides information when the AID Submodel was modified.",
        value_type="xs:dateTime",
    )
    support: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#supportContact",
        description="Provides an address on how to contact the maintainer of AID Submodel as URI scheme.",
        value_type="xs:anyURI",
    )
    endpoint_metadata: EndpointMetadata = EndpointMetadata()
    interaction_metadata: InteractionMetadata = InteractionMetadata()
    external_descriptor: ExternalDescriptor = ExternalDescriptor()

class InterfaceTemplateForIOLINK_OVER_PROFINET_REST(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/Interface"
    description: str = "Indicates entry point for IO Link over HTTP and PROFINET interface."
    supplemental_semantic_ids: List[str] = ["https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link", "https://www.w3.org/2019/wot/td"]
    value: InterfaceTemplateForIOLINK_OVER_PROFINET_RESTValues = InterfaceTemplateForIOLINK_OVER_PROFINET_RESTValues()

class AssetInterfacesDescriptionValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    interface_template_for_h_t_t_p: Dict[str, InterfaceTemplateForHTTP] = {}
    interface_template_for_m_o_d_b_u_s: Dict[str, InterfaceTemplateForMODBUS] = {}
    interface_template_for_m_q_t_t: Dict[str, InterfaceTemplateForMQTT] = {}
    interface_template_for_o_p_c_u_a: Dict[str, InterfaceTemplateForOPCUA] = {}
    interface_template_for_bacnet: Dict[str, InterfaceTemplateForBacnet] = {}
    interface_template_for_i_o_l_i_n_k__o_v_e_r__p_r_o_f_i_n_e_t__r_e_s_t: Dict[str, InterfaceTemplateForIOLINK_OVER_PROFINET_REST] = {}

class AssetInterfacesDescription(Submodel):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/1/Submodel"
    description: str = "Definition of the Submodel Asset Interfaces Description identified by its semanticId. The Submodel idShort can be picked freely."
    VERSION: ClassVar[str] = "1"
    REVISION: ClassVar[str] = "1"
    submodel_element: AssetInterfacesDescriptionValues = AssetInterfacesDescriptionValues()

# ── Resolve forward references (Pydantic circular refs) ──
security.model_rebuild()
nosec_scValues.model_rebuild()
nosec_sc.model_rebuild()
auto_scValues.model_rebuild()
auto_sc.model_rebuild()
basic_scValues.model_rebuild()
basic_sc.model_rebuild()
oneOf.model_rebuild()
allOf.model_rebuild()
combo_scValues.model_rebuild()
combo_sc.model_rebuild()
apikey_scValues.model_rebuild()
apikey_sc.model_rebuild()
psk_scValues.model_rebuild()
psk_sc.model_rebuild()
digest_scValues.model_rebuild()
digest_sc.model_rebuild()
bearer_scValues.model_rebuild()
bearer_sc.model_rebuild()
scopes.model_rebuild()
oauth2_scValues.model_rebuild()
oauth2_sc.model_rebuild()
securityDefinitionsValues.model_rebuild()
securityDefinitions.model_rebuild()
EndpointMetadataValues.model_rebuild()
EndpointMetadata.model_rebuild()
enum.model_rebuild()
itemsValues.model_rebuild()
items.model_rebuild()
htv_headerValues.model_rebuild()
htv_header.model_rebuild()
htv_headers.model_rebuild()
formsValues.model_rebuild()
forms.model_rebuild()
property_nameValues.model_rebuild()
property_name.model_rebuild()
propertiesValues.model_rebuild()
properties.model_rebuild()
actionsValues.model_rebuild()
actions.model_rebuild()
eventsValues.model_rebuild()
events.model_rebuild()
InteractionMetadataValues.model_rebuild()
InteractionMetadata.model_rebuild()
ExternalDescriptorValues.model_rebuild()
ExternalDescriptor.model_rebuild()
InterfaceTemplateForHTTPValues.model_rebuild()
InterfaceTemplateForHTTP.model_rebuild()
InterfaceTemplateForMODBUSValues.model_rebuild()
InterfaceTemplateForMODBUS.model_rebuild()
InterfaceTemplateForMQTTValues.model_rebuild()
InterfaceTemplateForMQTT.model_rebuild()
opcua_channel_scValues.model_rebuild()
opcua_channel_sc.model_rebuild()
opcua_authentication_scValues.model_rebuild()
opcua_authentication_sc.model_rebuild()
InterfaceTemplateForOPCUAValues.model_rebuild()
InterfaceTemplateForOPCUA.model_rebuild()
uriVariablesValues.model_rebuild()
uriVariables.model_rebuild()
bacv_hasNamedMember.model_rebuild()
bacv_hasValueMap.model_rebuild()
bacv_hasMemberValues.model_rebuild()
bacv_hasMember.model_rebuild()
bacv_hasDataTypeValues.model_rebuild()
bacv_hasDataType.model_rebuild()
InterfaceTemplateForBacnetValues.model_rebuild()
InterfaceTemplateForBacnet.model_rebuild()
iolv_enumeratedValueValues.model_rebuild()
iolv_enumeratedValue.model_rebuild()
iolv_enumeratedValues.model_rebuild()
iolv_payloadMappingElementValues.model_rebuild()
iolv_payloadMappingElement.model_rebuild()
iolv_payloadMapping.model_rebuild()
InterfaceTemplateForIOLINK_OVER_PROFINET_RESTValues.model_rebuild()
InterfaceTemplateForIOLINK_OVER_PROFINET_REST.model_rebuild()
AssetInterfacesDescriptionValues.model_rebuild()
AssetInterfacesDescription.model_rebuild()
