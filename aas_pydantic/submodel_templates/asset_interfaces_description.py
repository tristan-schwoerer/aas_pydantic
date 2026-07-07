"""AssetInterfacesDescription — generated from IDTA template."""

from __future__ import annotations

from typing import ClassVar, List, Optional
from pydantic import Field
from aas_pydantic import (
    Submodel, SubmodelElementCollection, Capability, Qualifier,
    Blob, File, MultiLanguageProperty, Property, Range, ReferenceElement, RelationshipElement,
)

class nosec_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#NoSecurityScheme"
    description: str = "This SubmodelElements holds the information about security mechanism based on nosec security."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
    ]

    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. the scheme for nosec_sc is nosec",
        qualifiers=[
            Qualifier(type_="Cardinality", value="One"),
        ],
    )

class auto_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#AutoSecurityScheme"
    description: str = "This SubmodelElements holds the information about security mechanism based on auto security."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
    ]

    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. The scheme for auto_sc is auto.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="One"),
        ],
    )
    proxy: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#proxy",
        description="Provides address information of the proxy server the security configuration provides access to.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )

class basic_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#BasicSecurityScheme"
    description: str = "This SubmodelElements holds the information about security mechanism based on basic security."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
    ]

    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. The scheme for basic_sc is basic.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="One"),
        ],
    )
    name: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#name",
        description="Name for query, header, cookie, or uri parameters",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    in_: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#in",
        description="Specifies the location of security authentication information. Proposed values are header, query, body, cookie or auto",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    proxy: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#proxy",
        description="Provides address information of the proxy server the security configuration provides access to.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )

class combo_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#ComboSecurityScheme"
    description: str = "This SubmodelElements holds the information about security mechanism based on combo security."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
    ]

    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. The scheme for combo_sc is combo.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="One"),
        ],
    )
    one_of: List[str] = Field([], json_schema_extra={"aas": {
            "semantic_id": "https://www.w3.org/2019/wot/security#oneOf",
            "description": "Specifies alternative security schemes where at least one listed scheme can be used.",
            "qualifiers": [
                Qualifier(type_="Cardinality", value="One")
            ]
        }})
    all_of: List[str] = Field([], json_schema_extra={"aas": {
            "semantic_id": "https://www.w3.org/2019/wot/security#allOf",
            "description": "Specifies a combined security configuration where all listed schemes are applied together.",
            "qualifiers": [
                Qualifier(type_="Cardinality", value="One")
            ]
        }})
    proxy: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#proxy",
        description="Provides address information of the proxy server the security configuration provides access to.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )

class apikey_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#APIKeySecurityScheme"
    description: str = "This SubmodelElements holds the information about security mechanism based on apikey security."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
    ]

    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. The scheme for apikey_sc is apikey.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="One"),
        ],
    )
    name: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#name",
        description="Name for query, header, cookie, or uri parameters.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    in_: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#in",
        description="Specifies the location of security authentication information. Proposed values are header, query, body, cookie or auto.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    proxy: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#proxy",
        description="Provides address information of the proxy server the security configuration provides access to.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )

class psk_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#PSKSecurityScheme"
    description: str = "This SubmodelElements holds the information about security mechanism based on psk security."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
    ]

    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. The scheme for psk_sc is psk.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="One"),
        ],
    )
    identity: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#identity",
        description="Identifier providing information which can be used for selection or confirmation.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    proxy: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#proxy",
        description="Provides address information of the proxy server the security configuration provides access to.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )

class digest_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#DigestSecurityScheme"
    description: str = "This SubmodelElements holds the information about security mechanism based on digest security."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
    ]

    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. The scheme for digest_sc is digest.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="One"),
        ],
    )
    name: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#name",
        description="Name for query, header, cookie, or uri parameters.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    in_: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#in",
        description="Specifies the location of security authentication information. Proposed values are header, query, body, cookie or auto",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    qop: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#qop",
        description="Defines Quality of protection. Values is one of auth or auth-int",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    proxy: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#proxy",
        description="Provides address information of the proxy server the security configuration provides access to.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )

class bearer_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#BearerSecurityScheme"
    description: str = "This SubmodelElements holds the information about security mechanism based on bearer security."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
    ]

    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. The scheme for bearer_sc is bearer.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="One"),
        ],
    )
    name: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#name",
        description="Name for query, header, cookie, or uri parameters.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    in_: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#in",
        description="Specifies the location of security authentication information. Proposed values are header, query, body, cookie or auto.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    authorization: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#authorization",
        description="Specifies URI of the authorization server.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    alg: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#alg",
        description="Defines Encoding, encryption, or digest algorithm (e.g. ES256, ES512-256).",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    format_: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#format",
        description="Specifies format of security authentication information. Options as value are jwt, cwt, jwe or jws",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    proxy: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#proxy",
        description="Provides address information of the proxy server the security configuration provides access to.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )

class oauth2_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#OAuth2SecurityScheme"
    description: str = "This SubmodelElements holds the information about security mechanism based on oauth2 security."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
    ]

    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. The scheme for oauth2_sc is oauth2.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="One"),
        ],
    )
    token: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#token",
        description="Specifies URI of the token server.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    refresh: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#refresh",
        description="Specifies URI of the refresh server.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    authorization: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#authorization",
        description="Specifies URI of the authorization server.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    scopes: List[str] = Field([], json_schema_extra={"aas": {
            "semantic_id": "https://www.w3.org/2019/wot/security#scopes",
            "description": "Set of authorization scope identifiers (as Property) provided as an array. These are provided in tokens returned by an authorization server and associated with forms in order to identify what resources a client may access and how.",
            "qualifiers": [
                Qualifier(type_="Cardinality", value="ZeroToOne")
            ]
        }})
    flow: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#flow",
        description="Defines authorization flow such as code or client.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    proxy: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#proxy",
        description="Provides address information of the proxy server the security configuration provides access to.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )

class securityDefinitions(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/td#definesSecurityScheme"
    description: str = "Defines the security scheme according to W3C."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="One"),
    ]

    nosec_sc: Optional[nosec_sc] = None
    auto_sc: Optional[auto_sc] = None
    basic_sc: Optional[basic_sc] = None
    combo_sc: Optional[combo_sc] = None
    apikey_sc: Optional[apikey_sc] = None
    psk_sc: Optional[psk_sc] = None
    digest_sc: Optional[digest_sc] = None
    bearer_sc: Optional[bearer_sc] = None
    oauth2_sc: Optional[oauth2_sc] = None

class EndpointMetadata(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/EndpointMetadata"
    description: str = "Provides the metadata of the asset\u2019s endpoint (base, content type that is used for interaction, etc)"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="One"),
    ]

    base: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#baseURI",
        description="Defines asset connection entry point. The base pattern for HTTP is defined in Qalifier.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="One"),
        ],
    )
    content_type: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/hypermedia#forContentType",
        description="Defines content type based on a media type (e.g., text/plain) and potential character decoding/encoding type (e.g., charset=utf-8) for the media type (see RFC2046) of the whole interface.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="One"),
        ],
    )
    security: List[ReferenceElement] = Field([], json_schema_extra={"aas": {
            "semantic_id": "https://www.w3.org/2019/wot/td#hasSecurityConfiguration",
            "description": "Selects one or more of the security scheme(s) that can be applied at runtime from the collection of security schemes defines in securityDefinitions. ",
            "qualifiers": [
                Qualifier(type_="Cardinality", value="One")
            ]
        }})
    security_definitions: Optional[securityDefinitions] = None

class items(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/json-schema#items"
    description: str = "Used to define the data schema characteristics (as specified within Section 2.9) of an array payload."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
        Qualifier(type_="Constraint", value="Only applicable for array-based values"),
    ]

    type_: Property = Property(
        semantic_id="https://www.w3.org/1999/02/22-rdf-syntax-ns#type",
        description="Indicates the abstract data type (one of object, array, string, number, integer, boolean, or null) of the described datapoint.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    title: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#title",
        description="Provides a human-readable title of this interaction (e.g., display a text for UI representation)",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    observable: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#isObservable",
        description="An indicator that tells that the interaction datapoint can be observed with a, e.g., subscription mechanism by an underlying protocol.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    const: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/json-schema#const",
        description="Provides a constant value for defined datapoint. The data type should be identical to the one provided by the Property type.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    enum: List[str] = Field([], json_schema_extra={"aas": {
            "semantic_id": "https://www.w3.org/2019/wot/json-schema#enum",
            "description": "Provides a list of restricted set of values that the asset can provide as datapoint value.",
            "qualifiers": [
                Qualifier(type_="Cardinality", value="ZeroToOne")
            ]
        }})
    default: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/json-schema#default",
        description="Provides a default value that must of the type as the datapoint valueType. The data type should be identical to the one as provided by the Property type.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    unit: Property = Property(
        semantic_id="https://schema.org/unitCode",
        description="Provides information about the datapoint\u2019s unit.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    min_max: Range = Range(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange",
        description="Specifies a minimum and/or maximum numeric value for the datapoint. This term is only used when type element is number or integer. When it is number, the range data type has to be float and when it is integer, the range data type has to be integer ",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
            Qualifier(type_="Constraint", value="Only applicable for number-/integer-based values"),
            Qualifier(type_="Select", value="minimum | maximum | minimum AND maximum as supplementalSem.Id"),
        ],
    )
    length_range: Range = Range(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange",
        description="Specifies the minimum and maximum length of a string.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
            Qualifier(type_="Constraint", value="Only applicable for string-based values"),
            Qualifier(type_="Select", value="minLength | maxLength | minLength AND maxLength as supplementalSem.Id"),
        ],
    )
    value_semantics: ReferenceElement = ReferenceElement(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics",
        description="Provides additional semantic information of the value that is read/subscribed at runtime. ",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )

class iolv_enumeratedValue(SubmodelElementCollection):
    semantic_id: str = "http://www.w3.org/2022/wot/iolink#EnumeratedValue"
    description: str = "Defines the logical semantic to encoded payload provided a byte or byte stream."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZerotoMany"),
    ]

    iolv_encoded_payload: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/encodedPayload",
        description="Specifies the presentation of the payload Logical encoding.  ",
        qualifiers=[
            Qualifier(type_="Cardinality", value="One"),
        ],
    )
    iolv_decoded_payload: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/decodedPayload",
        description="Specifies the human readable meaning of the payload Logical encoding.  ",
        qualifiers=[
            Qualifier(type_="Cardinality", value="One"),
        ],
    )

class iolv_payloadMappingElement(SubmodelElementCollection):
    semantic_id: str = "http://www.w3.org/2022/wot/iolink#PayloadMapping"
    description: str = "Defines the payload mapping associated to a datapoint."

    iolv_reference_to_property: ReferenceElement = ReferenceElement(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/referenceToProperty",
        description="Defined the reference to a nested datapoint of an object type datapoint. ",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    iolv_type: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/hasPayloadDataType",
        description="Specifies the data type contained in the request or response payload. ",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    iolv_byte_offset: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/byteOffset",
        description="For object type datapoints. Used to identify the starting point within a byte stream payload that represents a datapoint.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    iolv_byte_length: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/byteLength",
        description="For object type datapoints. Used to identify the byte length within a byte stream payload that represents a datapoint.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    iolv_bit_offset: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/bitOffset",
        description="For object type datapoints. Used to identify the starting point within a bit stream payload that represents a datapoint.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    iolv_bit_length: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/bitLength",
        description="For object type datapoints. Used to identify the bit length of a datapoint from the bit stream payload.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    iolv_enumerated_values: List[iolv_enumeratedValue] = []

class forms(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/td#hasForm"
    description: str = "Contains information about datapoint resource location. Note, forms is only available at the top level {property_name}"

    href: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/hypermedia#hasTarget",
        description="Indicates target IRI relative path or full IRI of asset\u2019s datapoint. The relative endpoint definition in href is always relative to base defined in EndpointMetadata. ",
        qualifiers=[
            Qualifier(type_="Cardinality", value="One"),
        ],
    )
    content_type: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/hypermedia#forContentType",
        description="Indicates the datapoint media type specified by IANA.Note: this local definition overwrites the globally defined contentType specified in EndpointMetadata (if it exists).",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    subprotocol: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/hypermedia#forSubProtocol",
        description="Indicates the exact mechanism by which an interaction will be accomplished for a given protocol when there are multiple options.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    security: List[ReferenceElement] = Field([], json_schema_extra={"aas": {
            "semantic_id": "https://www.w3.org/2019/wot/td#hasSecurityConfiguration",
            "description": "Selects one or more of the security scheme(s) that can be applied at runtime from the collection of security schemes defines in securityDefinitions. ",
            "qualifiers": [
                Qualifier(type_="Cardinality", value="One")
            ]
        }})
    iolv_method: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/hasMethod",
        description="Defines the type of operation to execute on a datapoint",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    iolv_access_rigths: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/hasAccessRights",
        description="Defines the type of operation that can be executed of a datapoint.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    iolv_type: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/hasPayloadDataType",
        description="Specifies the data type contained in the request or response payload. ",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    iolv_byte_offset: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/byteOffset",
        description="For object type datapoints. Used to identify the starting point within a byte stream payload that represents a datapoint.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    iolv_byte_length: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/byteLength",
        description="For object type datapoints. Used to identify the byte length within a byte stream payload that represents a datapoint.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    iolv_bit_offset: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/bitOffset",
        description="For object type datapoints. Used to identify the starting point within a bit stream payload that represents a datapoint.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    iolv_bit_length: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/bitLength",
        description="For object type datapoints. Used to identify the bit length of a datapoint from the bit stream payload.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    iolv_enumerated_values: List[iolv_enumeratedValue] = []
    iolv_payload_mapping: List[iolv_payloadMappingElement] = []

class property_name(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/PropertyDefinition"
    description: str = "Defines an interaction property that covers usually a datapoint definition that can be read or subscribed to."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToMany"),
    ]

    key: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/0/key",
        description="Optional element when the idShort of {property_name} cannot be used to reflect the desired property name due to the idShort restrictions (e.g., payload message uses \u201ctemperature-value\u201d as key term).",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    type_: Property = Property(
        semantic_id="https://www.w3.org/1999/02/22-rdf-syntax-ns#type",
        description="Indicates the abstract data type (one of object, array, string, number, integer, boolean, or null) of the described datapoint.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    title: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#title",
        description="Provides a human-readable title of this interaction (e.g., display a text for UI representation)",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    observable: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#isObservable",
        description="An indicator that tells that the interaction datapoint can be observed with a, e.g., subscription mechanism by an underlying protocol.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    const: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/json-schema#const",
        description="Provides a constant value for defined datapoint. The data type should be identical to the one provided by the Property type.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    enum: List[str] = Field([], json_schema_extra={"aas": {
            "semantic_id": "https://www.w3.org/2019/wot/json-schema#enum",
            "description": "Provides a list of restricted set of values that the asset can provide as datapoint value.",
            "qualifiers": [
                Qualifier(type_="Cardinality", value="ZeroToOne")
            ]
        }})
    default: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/json-schema#default",
        description="Provides a default value that must of the type as the datapoint valueType. The data type should be identical to the one as provided by the Property type.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    unit: Property = Property(
        semantic_id="https://schema.org/unitCode",
        description="Provides information about the datapoint\u2019s unit.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    min_max: Range = Range(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange",
        description="Specifies a minimum and/or maximum numeric value for the datapoint. This term is only used when type element is number or integer. When it is number, the range data type has to be float and when it is integer, the range data type has to be integer ",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
            Qualifier(type_="Constraint", value="Only applicable for number-/integer-based values"),
            Qualifier(type_="Select", value="minimum | maximum | minimum AND maximum as supplementalSem.Id"),
        ],
    )
    length_range: Range = Range(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange",
        description="Specifies the minimum and maximum length of a string.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
            Qualifier(type_="Constraint", value="Only applicable for string-based values"),
            Qualifier(type_="Select", value="minLength | maxLength | minLength AND maxLength as supplementalSem.Id"),
        ],
    )
    items: Optional[items] = None
    items_range: Range = Range(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/0/itemsRange",
        description="Defines the minimum and maximum number of items that have to be in an array payload.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
            Qualifier(type_="Constraint", value="Only applicable for string-based values"),
            Qualifier(type_="Select", value="minItems | maxItems | minItems AND maxItems as supplementalSem.Id"),
        ],
    )
    properties: Optional[properties] = None
    value_semantics: ReferenceElement = ReferenceElement(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics",
        description="Provides additional semantic information of the value that is read/subscribed at runtime. ",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    forms: Optional[forms] = None

class properties(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/td#PropertyAffordance"
    description: str = "Collection of asset\u2019s datapoint definitions"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
    ]

    property_name: Optional[property_name] = None

class htv_header(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2011/http#headers"
    description: str = "Defines message header content "
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="OneToMany"),
    ]

    htv_field_name: Property = Property(
        semantic_id="https://www.w3.org/2011/http#fieldName",
        description="Defines message header name ",
        qualifiers=[
            Qualifier(type_="Cardinality", value="One"),
        ],
    )
    htv_field_value: Property = Property(
        semantic_id="https://www.w3.org/2011/http#fieldValue",
        description="Defines message header value",
        qualifiers=[
            Qualifier(type_="Cardinality", value="One"),
        ],
    )

class actions(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/td#ActionAffordance"
    description: str = "Collection of functions that can be done on asset as action SMC"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
    ]

    pass

class events(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/td#EventAffordance"
    description: str = "Collection of events triggerable by datapoint state as event SMC"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
    ]

    pass

class InteractionMetadata(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/InteractionMetadata"
    description: str = "Provides the metadata of the actually interfaces such as which datapoints and functions are provided by the properties, actions, and events interaction abstraction. "
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="One"),
    ]

    properties: Optional[properties] = None
    actions: Optional[actions] = None
    events: Optional[events] = None

class ExternalDescriptor(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/ExternalDescriptor"
    description: str = "Provides a place for existing description files (e.g., Thing Description, GSDML, etc,)."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
    ]

    file_name: File = File(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/0/externalDescriptorName",
        description="File reference (local in AASX or outside) to an external descriptor description (e.g., Thing Description, GSDML, MTP, etc,).  ",
    )

class InterfaceTemplateForHTTP(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/Interface"
    description: str = "Indicates entry point for HTTP interface."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToMany"),
    ]

    title: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#title",
        description="Provides a human-readable title to give a human-readable context of the interface.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="One"),
        ],
    )
    created: Property = Property(
        semantic_id="http://purl.org/dc/terms/created",
        description="Provides information when the AID Submodel was created.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    modified: Property = Property(
        semantic_id="http://purl.org/dc/terms/modified",
        description="Provides information when the AID Submodel was modified.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    support: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#supportContact",
        description="Provides an address on how to contact the maintainer of AID Submodel as URI scheme.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    endpoint_metadata: Optional[EndpointMetadata] = None
    interaction_metadata: Optional[InteractionMetadata] = None
    external_descriptor: Optional[ExternalDescriptor] = None

class InterfaceTemplateForMODBUS(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/Interface"
    description: str = "Indicates entry point for MODBUS interface."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToMany"),
    ]

    title: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#title",
        description="Provides a human-readable title to give a human-readable context of the interface.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="One"),
        ],
    )
    created: Property = Property(
        semantic_id="http://purl.org/dc/terms/created",
        description="Provides information when the AID Submodel was created.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    modified: Property = Property(
        semantic_id="http://purl.org/dc/terms/modified",
        description="Provides information when the AID Submodel was modified.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    support: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#supportContact",
        description="Provides an address on how to contact the maintainer of AID Submodel as URI scheme.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    endpoint_metadata: Optional[EndpointMetadata] = None
    interaction_metadata: Optional[InteractionMetadata] = None
    external_descriptor: Optional[ExternalDescriptor] = None

class InterfaceTemplateForMQTT(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/Interface"
    description: str = "Indicates entry point for MQTT interface."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToMany"),
    ]

    title: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#title",
        description="Provides a human-readable title to give a human-readable context of the interface.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="One"),
        ],
    )
    created: Property = Property(
        semantic_id="http://purl.org/dc/terms/created",
        description="Provides information when the AID Submodel was created.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    modified: Property = Property(
        semantic_id="http://purl.org/dc/terms/modified",
        description="Provides information when the AID Submodel was modified.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    support: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#supportContact",
        description="Provides an address on how to contact the maintainer of AID Submodel as URI scheme.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    endpoint_metadata: Optional[EndpointMetadata] = None
    interaction_metadata: Optional[InteractionMetadata] = None
    external_descriptor: Optional[ExternalDescriptor] = None

class opcua_channel_sc(SubmodelElementCollection):
    semantic_id: str = "http://opcfoundation.org/UA/WoT-Binding/OPCUASecurityChannelScheme"
    description: str = "This SubmodelElements holds the information about security mechanism based on opcua_channel security."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
    ]

    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. The scheme for opcua_channel_sc is ua_channelsec.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="One"),
        ],
    )
    proxy: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#proxy",
        description="Provides address information of the proxy server the security configuration provides access to.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    uav_security_mode: Property = Property(
        semantic_id="http://opcfoundation.org/UA/WoT-Binding/securityMode ",
        description="Provides information about the security modes supported by the OPC UA server endpoint(e.g None, Sign,SignAndEncrypt)",
        qualifiers=[
            Qualifier(type_="Cardinality", value="One"),
        ],
    )
    uav_security_policy: Property = Property(
        semantic_id="http://opcfoundation.org/UA/WoT-Binding/securityPolicy",
        description="Provides information about which policy options are available from the supported endpoints of the OPC UA server(e.g None, Basic256Sha256)",
        qualifiers=[
            Qualifier(type_="Cardinality", value="One"),
        ],
    )

class opcua_authentication_sc(SubmodelElementCollection):
    semantic_id: str = "http://opcfoundation.org/UA/WoT-Binding/OPCUASecurityAuthenticationScheme "
    description: str = "This SubmodelElements holds the information about security mechanism based on opcua_authentication security."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
    ]

    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. The scheme for opcua_authentication_sc is ua_authentication.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="One"),
        ],
    )
    proxy: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#proxy",
        description="Provides address information of the proxy server the security configuration provides access to.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    uav_user_identity_token: Property = Property(
        semantic_id="http://opcfoundation.org/UA/WoT-Binding/userIdentityToken",
        description="Provides information about which policy options are available from the supported endpoints of the OPC UA server (e.g Anonymous)",
        qualifiers=[
            Qualifier(type_="Cardinality", value="One"),
        ],
    )
    uav_issue_token: ReferenceElement = ReferenceElement(
        semantic_id="http://opcfoundation.org/UA/WoT-Binding/issueToken",
        description="Provides reference to security scheme within SecurityDefinition SMC that holds information about the token to use (e.g OAuth2).",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )

class InterfaceTemplateForOPCUA(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/Interface"
    description: str = "Indicates entry point for OPC UA interface."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToMany"),
    ]

    title: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#title",
        description="Provides a human-readable title to give a human-readable context of the interface.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="One"),
        ],
    )
    created: Property = Property(
        semantic_id="http://purl.org/dc/terms/created",
        description="Provides information when the AID Submodel was created.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    modified: Property = Property(
        semantic_id="http://purl.org/dc/terms/modified",
        description="Provides information when the AID Submodel was modified.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    support: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#supportContact",
        description="Provides an address on how to contact the maintainer of AID Submodel as URI scheme.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    endpoint_metadata: Optional[EndpointMetadata] = None
    interaction_metadata: Optional[InteractionMetadata] = None
    external_descriptor: Optional[ExternalDescriptor] = None

class uriVariables(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/td#hasUriTemplateSchema"
    description: str = "Defines URI template variables according to RFC6570 as a collection based on an interaction affordance data schema"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
        Qualifier(type_="Constraint", value="Only applicable for object-based values"),
    ]

    property_name: Optional[property_name] = None

class bacv_hasMember(SubmodelElementCollection):
    semantic_id: str = "http://www.w3.org/2022/bacnet#hasMember"
    description: str = "Defines the member of a Sequence and List data type."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
    ]

    bacv_is_i_s_o8601: Property = Property(
        semantic_id="http://www.w3.org/2022/bacnet#isIso8601",
        description="Current counter value",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    bacv_has_binary_representation: Property = Property(
        semantic_id="http://www.w3.org/2022/bacnet#hasBinaryRepresentation",
        description="Current counter value",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    bacv_has_member_: Optional[bacv_hasMember] = None
    bacv_has_named_member: List[properties] = []
    bacv_has_value_map: List[properties] = []

class bacv_hasDataType(SubmodelElementCollection):
    semantic_id: str = "http://www.w3.org/2022/bacnet#hasDataType"
    description: str = "Defines the type information of a BACnet payload. This SMC is used to abstract BACnet data model to human and machine readable model by still keeping its wire compatibility on the protocol."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
    ]

    bacv_is_i_s_o8601: Property = Property(
        semantic_id="http://www.w3.org/2022/bacnet#isIso8601",
        description="Defines if the data uses ISO8601 format",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    bacv_has_binary_representation: Property = Property(
        semantic_id="http://www.w3.org/2022/bacnet#hasBinaryRepresentation",
        description="Defines the payload\u2019s binary representation type. This term is used when the payload is an OctetString",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    bacv_has_member: Optional[bacv_hasMember] = None
    bacv_has_named_member: List[properties] = []
    bacv_has_value_map: List[properties] = []

class InterfaceTemplateForBacnet(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/Interface"
    description: str = "Indicates entry point for BACnet interface."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToMany"),
    ]

    title: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#title",
        description="Provides a human-readable title to give a human-readable context of the interface.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="One"),
        ],
    )
    created: Property = Property(
        semantic_id="http://purl.org/dc/terms/created",
        description="Provides information when the AID Submodel was created.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    modified: Property = Property(
        semantic_id="http://purl.org/dc/terms/modified",
        description="Provides information when the AID Submodel was modified.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    support: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#supportContact",
        description="Provides an address on how to contact the maintainer of AID Submodel as URI scheme.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    endpoint_metadata: Optional[EndpointMetadata] = None
    interaction_metadata: Optional[InteractionMetadata] = None
    external_descriptor: Optional[ExternalDescriptor] = None

class InterfaceTemplateForIOLINK_OVER_PROFINET_REST(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/Interface"
    description: str = "Indicates entry point for IO Link over HTTP and PROFINET interface."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToMany"),
    ]

    title: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#title",
        description="Provides a human-readable title to give a human-readable context of the interface.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="One"),
        ],
    )
    created: Property = Property(
        semantic_id="http://purl.org/dc/terms/created",
        description="Provides information when the AID Submodel was created.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    modified: Property = Property(
        semantic_id="http://purl.org/dc/terms/modified",
        description="Provides information when the AID Submodel was modified.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    support: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#supportContact",
        description="Provides an address on how to contact the maintainer of AID Submodel as URI scheme.",
        qualifiers=[
            Qualifier(type_="Cardinality", value="ZeroToOne"),
        ],
    )
    endpoint_metadata: Optional[EndpointMetadata] = None
    interaction_metadata: Optional[InteractionMetadata] = None
    external_descriptor: Optional[ExternalDescriptor] = None

class AssetInterfacesDescription(Submodel):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/1/Submodel"
    description: str = "Definition of the Submodel Asset Interfaces Description identified by its semanticId. The Submodel idShort can be picked freely."
    VERSION: ClassVar[str] = "1"
    REVISION: ClassVar[str] = "1"

    interface_template_for_h_t_t_p: Optional[InterfaceTemplateForHTTP] = None
    interface_template_for_m_o_d_b_u_s: Optional[InterfaceTemplateForMODBUS] = None
    interface_template_for_m_q_t_t: Optional[InterfaceTemplateForMQTT] = None
    interface_template_for_o_p_c_u_a: Optional[InterfaceTemplateForOPCUA] = None
    interface_template_for_bacnet: Optional[InterfaceTemplateForBacnet] = None
    interface_template_for_i_o_l_i_n_k__o_v_e_r__p_r_o_f_i_n_e_t__r_e_s_t: Optional[InterfaceTemplateForIOLINK_OVER_PROFINET_REST] = None
