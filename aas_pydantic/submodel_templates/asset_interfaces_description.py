"""AssetInterfacesDescription — generated from IDTA template."""

from __future__ import annotations

from typing import ClassVar, Dict, List, Optional
from aas_pydantic import (
    File, Property, Qualifier, Range, ReferenceElement, Submodel, SubmodelElement, SubmodelElementCollection, SubmodelElementList,
)

class security(SubmodelElementList):
    semantic_id: str = "https://www.w3.org/2019/wot/td#hasSecurityConfiguration"
    description: str = "Selects one or more of the security scheme(s) that can be applied at runtime from the collection of security schemes defines in securityDefinitions. "

    value: List[ReferenceElement] = []

class nosec_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#NoSecurityScheme"
    description: str = "This SubmodelElements holds the information about security mechanism based on nosec security."

    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. the scheme for nosec_sc is nosec",
    )

class auto_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#AutoSecurityScheme"
    description: str = "This SubmodelElements holds the information about security mechanism based on auto security."

    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. The scheme for auto_sc is auto.",
    )
    proxy: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#proxy",
        description="Provides address information of the proxy server the security configuration provides access to.",
    )

class basic_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#BasicSecurityScheme"
    description: str = "This SubmodelElements holds the information about security mechanism based on basic security."

    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. The scheme for basic_sc is basic.",
    )
    name: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#name",
        description="Name for query, header, cookie, or uri parameters",
    )
    in_: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#in",
        description="Specifies the location of security authentication information. Proposed values are header, query, body, cookie or auto",
    )
    proxy: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#proxy",
        description="Provides address information of the proxy server the security configuration provides access to.",
    )

class oneOf(SubmodelElementList):
    semantic_id: str = "https://www.w3.org/2019/wot/security#oneOf"
    description: str = "Specifies alternative security schemes where at least one listed scheme can be used."

    value: List[SubmodelElement] = []

class allOf(SubmodelElementList):
    semantic_id: str = "https://www.w3.org/2019/wot/security#allOf"
    description: str = "Specifies a combined security configuration where all listed schemes are applied together."

    value: List[SubmodelElement] = []

class combo_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#ComboSecurityScheme"
    description: str = "This SubmodelElements holds the information about security mechanism based on combo security."

    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. The scheme for combo_sc is combo.",
    )
    one_of: oneOf = oneOf(id_short="oneOf")
    all_of: allOf = allOf(id_short="allOf")
    proxy: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#proxy",
        description="Provides address information of the proxy server the security configuration provides access to.",
    )

class apikey_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#APIKeySecurityScheme"
    description: str = "This SubmodelElements holds the information about security mechanism based on apikey security."

    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. The scheme for apikey_sc is apikey.",
    )
    name: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#name",
        description="Name for query, header, cookie, or uri parameters.",
    )
    in_: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#in",
        description="Specifies the location of security authentication information. Proposed values are header, query, body, cookie or auto.",
    )
    proxy: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#proxy",
        description="Provides address information of the proxy server the security configuration provides access to.",
    )

class psk_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#PSKSecurityScheme"
    description: str = "This SubmodelElements holds the information about security mechanism based on psk security."

    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. The scheme for psk_sc is psk.",
    )
    identity: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#identity",
        description="Identifier providing information which can be used for selection or confirmation.",
    )
    proxy: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#proxy",
        description="Provides address information of the proxy server the security configuration provides access to.",
    )

class digest_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#DigestSecurityScheme"
    description: str = "This SubmodelElements holds the information about security mechanism based on digest security."

    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. The scheme for digest_sc is digest.",
    )
    name: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#name",
        description="Name for query, header, cookie, or uri parameters.",
    )
    in_: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#in",
        description="Specifies the location of security authentication information. Proposed values are header, query, body, cookie or auto",
    )
    qop: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#qop",
        description="Defines Quality of protection. Values is one of auth or auth-int",
    )
    proxy: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#proxy",
        description="Provides address information of the proxy server the security configuration provides access to.",
    )

class bearer_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#BearerSecurityScheme"
    description: str = "This SubmodelElements holds the information about security mechanism based on bearer security."

    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. The scheme for bearer_sc is bearer.",
    )
    name: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#name",
        description="Name for query, header, cookie, or uri parameters.",
    )
    in_: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#in",
        description="Specifies the location of security authentication information. Proposed values are header, query, body, cookie or auto.",
    )
    authorization: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#authorization",
        description="Specifies URI of the authorization server.",
    )
    alg: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#alg",
        description="Defines Encoding, encryption, or digest algorithm (e.g. ES256, ES512-256).",
    )
    format_: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#format",
        description="Specifies format of security authentication information. Options as value are jwt, cwt, jwe or jws",
    )
    proxy: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#proxy",
        description="Provides address information of the proxy server the security configuration provides access to.",
    )

class scopes(SubmodelElementList):
    semantic_id: str = "https://www.w3.org/2019/wot/security#scopes"
    description: str = "Set of authorization scope identifiers (as Property) provided as an array. These are provided in tokens returned by an authorization server and associated with forms in order to identify what resources a client may access and how."

    value: List[SubmodelElement] = []

class oauth2_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#OAuth2SecurityScheme"
    description: str = "This SubmodelElements holds the information about security mechanism based on oauth2 security."

    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. The scheme for oauth2_sc is oauth2.",
    )
    token: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#token",
        description="Specifies URI of the token server.",
    )
    refresh: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#refresh",
        description="Specifies URI of the refresh server.",
    )
    authorization: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#authorization",
        description="Specifies URI of the authorization server.",
    )
    # _ref suffix: field renamed from "scopes" (Pydantic name-collision workaround)
    scopes_ref: scopes = scopes(id_short="scopes")
    flow: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#flow",
        description="Defines authorization flow such as code or client.",
    )
    proxy: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#proxy",
        description="Provides address information of the proxy server the security configuration provides access to.",
    )

class securityDefinitions(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/td#definesSecurityScheme"
    description: str = "Defines the security scheme according to W3C."

    # _ref suffix: field renamed from "nosec_sc" (Pydantic name-collision workaround)
    nosec_sc_ref: Optional[nosec_sc] = None
    # _ref suffix: field renamed from "auto_sc" (Pydantic name-collision workaround)
    auto_sc_ref: Optional[auto_sc] = None
    # _ref suffix: field renamed from "basic_sc" (Pydantic name-collision workaround)
    basic_sc_ref: Optional[basic_sc] = None
    # _ref suffix: field renamed from "combo_sc" (Pydantic name-collision workaround)
    combo_sc_ref: Optional[combo_sc] = None
    # _ref suffix: field renamed from "apikey_sc" (Pydantic name-collision workaround)
    apikey_sc_ref: Optional[apikey_sc] = None
    # _ref suffix: field renamed from "psk_sc" (Pydantic name-collision workaround)
    psk_sc_ref: Optional[psk_sc] = None
    # _ref suffix: field renamed from "digest_sc" (Pydantic name-collision workaround)
    digest_sc_ref: Optional[digest_sc] = None
    # _ref suffix: field renamed from "bearer_sc" (Pydantic name-collision workaround)
    bearer_sc_ref: Optional[bearer_sc] = None
    # _ref suffix: field renamed from "oauth2_sc" (Pydantic name-collision workaround)
    oauth2_sc_ref: Optional[oauth2_sc] = None

class EndpointMetadata(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/EndpointMetadata"
    description: str = "Provides the metadata of the asset\u2019s endpoint (base, content type that is used for interaction, etc)"

    base: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#baseURI",
        description="Defines asset connection entry point. The base pattern for HTTP is defined in Qalifier.",
    )
    content_type: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/hypermedia#forContentType",
        description="Defines content type based on a media type (e.g., text/plain) and potential character decoding/encoding type (e.g., charset=utf-8) for the media type (see RFC2046) of the whole interface.",
    )
    # _ref suffix: field renamed from "security" (Pydantic name-collision workaround)
    security_ref: security = security(id_short="security")
    security_definitions: securityDefinitions

class enum(SubmodelElementList):
    semantic_id: str = "https://www.w3.org/2019/wot/json-schema#enum"
    description: str = "Provides a list of restricted set of values that the asset can provide as datapoint value."

    value: List[Property] = []

class items(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/json-schema#items"
    description: str = "Used to define the data schema characteristics (as specified within Section 2.9) of an array payload."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Constraint", value="Only applicable for array-based values"),
    ]

    type_: Property = Property(
        semantic_id="https://www.w3.org/1999/02/22-rdf-syntax-ns#type",
        description="Indicates the abstract data type (one of object, array, string, number, integer, boolean, or null) of the described datapoint.",
    )
    title: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#title",
        description="Provides a human-readable title of this interaction (e.g., display a text for UI representation)",
    )
    observable: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#isObservable",
        description="An indicator that tells that the interaction datapoint can be observed with a, e.g., subscription mechanism by an underlying protocol.",
    )
    const: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/json-schema#const",
        description="Provides a constant value for defined datapoint. The data type should be identical to the one provided by the Property type.",
    )
    # _ref suffix: field renamed from "enum" (Pydantic name-collision workaround)
    enum_ref: enum = enum(id_short="enum")
    default: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/json-schema#default",
        description="Provides a default value that must of the type as the datapoint valueType. The data type should be identical to the one as provided by the Property type.",
    )
    unit: Property = Property(
        semantic_id="https://schema.org/unitCode",
        description="Provides information about the datapoint\u2019s unit.",
    )
    min_max: Range = Range(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange",
        description="Specifies a minimum and/or maximum numeric value for the datapoint. This term is only used when type element is number or integer. When it is number, the range data type has to be float and when it is integer, the range data type has to be integer ",
        qualifiers=[
            Qualifier(type_="Constraint", value="Only applicable for number-/integer-based values"),
            Qualifier(type_="Select", value="minimum | maximum | minimum AND maximum as supplementalSem.Id"),
        ],
    )
    length_range: Range = Range(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange",
        description="Specifies the minimum and maximum length of a string.",
        qualifiers=[
            Qualifier(type_="Constraint", value="Only applicable for string-based values"),
            Qualifier(type_="Select", value="minLength | maxLength | minLength AND maxLength as supplementalSem.Id"),
        ],
    )
    value_semantics: ReferenceElement = ReferenceElement(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics",
        description="Provides additional semantic information of the value that is read/subscribed at runtime. ",
    )

class iolv_enumeratedValues(SubmodelElementList):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/hasEnumeratedValues"
    description: str = "Contains a list of enumerated values that define the logical semantic to encoded payload provided a byte or byte stream. "

    value: List[None] = []

class iolv_payloadMapping(SubmodelElementList):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/hasPayloadMapping"
    description: str = "For object type datapoints. Used to provides logical mapping information of a complex payload from a IO lInk device."

    value: List[None] = []

class forms(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/td#hasForm"
    description: str = "Contains information about datapoint resource location. Note, forms is only available at the top level {property_name}"

    href: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/hypermedia#hasTarget",
        description="Indicates target IRI relative path or full IRI of asset\u2019s datapoint. The relative endpoint definition in href is always relative to base defined in EndpointMetadata. ",
    )
    content_type: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/hypermedia#forContentType",
        description="Indicates the datapoint media type specified by IANA.Note: this local definition overwrites the globally defined contentType specified in EndpointMetadata (if it exists).",
    )
    subprotocol: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/hypermedia#forSubProtocol",
        description="Indicates the exact mechanism by which an interaction will be accomplished for a given protocol when there are multiple options.",
    )
    # _ref suffix: field renamed from "security" (Pydantic name-collision workaround)
    security_ref: security = security(id_short="security")
    iolv_method: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/hasMethod",
        description="Defines the type of operation to execute on a datapoint",
    )
    iolv_access_rigths: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/hasAccessRights",
        description="Defines the type of operation that can be executed of a datapoint.",
    )
    iolv_type: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/hasPayloadDataType",
        description="Specifies the data type contained in the request or response payload. ",
    )
    iolv_byte_offset: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/byteOffset",
        description="For object type datapoints. Used to identify the starting point within a byte stream payload that represents a datapoint.",
    )
    iolv_byte_length: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/byteLength",
        description="For object type datapoints. Used to identify the byte length within a byte stream payload that represents a datapoint.",
    )
    iolv_bit_offset: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/bitOffset",
        description="For object type datapoints. Used to identify the starting point within a bit stream payload that represents a datapoint.",
    )
    iolv_bit_length: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/1/IO-Link/bitLength",
        description="For object type datapoints. Used to identify the bit length of a datapoint from the bit stream payload.",
    )
    iolv_enumerated_values: iolv_enumeratedValues = iolv_enumeratedValues(id_short="iolv_enumeratedValues")
    iolv_payload_mapping: iolv_payloadMapping = iolv_payloadMapping(id_short="iolv_payloadMapping")

class property_name(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/PropertyDefinition"
    description: str = "Defines an interaction property that covers usually a datapoint definition that can be read or subscribed to."

    key: Property = Property(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/0/key",
        description="Optional element when the idShort of {property_name} cannot be used to reflect the desired property name due to the idShort restrictions (e.g., payload message uses \u201ctemperature-value\u201d as key term).",
    )
    type_: Property = Property(
        semantic_id="https://www.w3.org/1999/02/22-rdf-syntax-ns#type",
        description="Indicates the abstract data type (one of object, array, string, number, integer, boolean, or null) of the described datapoint.",
    )
    title: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#title",
        description="Provides a human-readable title of this interaction (e.g., display a text for UI representation)",
    )
    observable: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#isObservable",
        description="An indicator that tells that the interaction datapoint can be observed with a, e.g., subscription mechanism by an underlying protocol.",
    )
    const: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/json-schema#const",
        description="Provides a constant value for defined datapoint. The data type should be identical to the one provided by the Property type.",
    )
    # _ref suffix: field renamed from "enum" (Pydantic name-collision workaround)
    enum_ref: enum = enum(id_short="enum")
    default: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/json-schema#default",
        description="Provides a default value that must of the type as the datapoint valueType. The data type should be identical to the one as provided by the Property type.",
    )
    unit: Property = Property(
        semantic_id="https://schema.org/unitCode",
        description="Provides information about the datapoint\u2019s unit.",
    )
    min_max: Range = Range(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange",
        description="Specifies a minimum and/or maximum numeric value for the datapoint. This term is only used when type element is number or integer. When it is number, the range data type has to be float and when it is integer, the range data type has to be integer ",
        qualifiers=[
            Qualifier(type_="Constraint", value="Only applicable for number-/integer-based values"),
            Qualifier(type_="Select", value="minimum | maximum | minimum AND maximum as supplementalSem.Id"),
        ],
    )
    length_range: Range = Range(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange",
        description="Specifies the minimum and maximum length of a string.",
        qualifiers=[
            Qualifier(type_="Constraint", value="Only applicable for string-based values"),
            Qualifier(type_="Select", value="minLength | maxLength | minLength AND maxLength as supplementalSem.Id"),
        ],
    )
    # _ref suffix: field renamed from "items" (Pydantic name-collision workaround)
    items_ref: Optional[items] = None
    items_range: Range = Range(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/0/itemsRange",
        description="Defines the minimum and maximum number of items that have to be in an array payload.",
        qualifiers=[
            Qualifier(type_="Constraint", value="Only applicable for string-based values"),
            Qualifier(type_="Select", value="minItems | maxItems | minItems AND maxItems as supplementalSem.Id"),
        ],
    )
    # _ref suffix: field renamed from "properties" (Pydantic name-collision workaround)
    properties_ref: Optional[properties] = None
    value_semantics: ReferenceElement = ReferenceElement(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics",
        description="Provides additional semantic information of the value that is read/subscribed at runtime. ",
    )
    # _ref suffix: field renamed from "forms" (Pydantic name-collision workaround)
    forms_ref: Optional[forms] = None

class properties(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/td#PropertyAffordance"
    description: str = "Collection of asset\u2019s datapoint definitions"

    # _ref suffix: field renamed from "property_name" (Pydantic name-collision workaround)
    property_name_ref: Optional[Dict[str, property_name]] = None

class htv_headers(SubmodelElementList):
    semantic_id: str = "https://www.w3.org/2011/http#headers"
    description: str = "Defines additional information to be sent within the HTTP header message."
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Constraint", value="Only applicable for HTTP binding"),
    ]

    value: List[None] = []

class actions(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/td#ActionAffordance"
    description: str = "Collection of functions that can be done on asset as action SMC"

    pass

class events(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/td#EventAffordance"
    description: str = "Collection of events triggerable by datapoint state as event SMC"

    pass

class InteractionMetadata(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/InteractionMetadata"
    description: str = "Provides the metadata of the actually interfaces such as which datapoints and functions are provided by the properties, actions, and events interaction abstraction. "

    # _ref suffix: field renamed from "properties" (Pydantic name-collision workaround)
    properties_ref: Optional[properties] = None
    # _ref suffix: field renamed from "actions" (Pydantic name-collision workaround)
    actions_ref: Optional[actions] = None
    # _ref suffix: field renamed from "events" (Pydantic name-collision workaround)
    events_ref: Optional[events] = None

class ExternalDescriptor(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/ExternalDescriptor"
    description: str = "Provides a place for existing description files (e.g., Thing Description, GSDML, etc,)."

    file_name: File = File(
        semantic_id="https://admin-shell.io/idta/AssetInterfacesDescription/1/0/externalDescriptorName",
        description="File reference (local in AASX or outside) to an external descriptor description (e.g., Thing Description, GSDML, MTP, etc,).  ",
    )

class InterfaceTemplateForHTTP(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/Interface"
    description: str = "Indicates entry point for HTTP interface."

    title: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#title",
        description="Provides a human-readable title to give a human-readable context of the interface.",
    )
    created: Property = Property(
        semantic_id="http://purl.org/dc/terms/created",
        description="Provides information when the AID Submodel was created.",
    )
    modified: Property = Property(
        semantic_id="http://purl.org/dc/terms/modified",
        description="Provides information when the AID Submodel was modified.",
    )
    support: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#supportContact",
        description="Provides an address on how to contact the maintainer of AID Submodel as URI scheme.",
    )
    endpoint_metadata: EndpointMetadata
    interaction_metadata: InteractionMetadata
    external_descriptor: Optional[ExternalDescriptor] = None

class InterfaceTemplateForMODBUS(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/Interface"
    description: str = "Indicates entry point for MODBUS interface."

    title: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#title",
        description="Provides a human-readable title to give a human-readable context of the interface.",
    )
    created: Property = Property(
        semantic_id="http://purl.org/dc/terms/created",
        description="Provides information when the AID Submodel was created.",
    )
    modified: Property = Property(
        semantic_id="http://purl.org/dc/terms/modified",
        description="Provides information when the AID Submodel was modified.",
    )
    support: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#supportContact",
        description="Provides an address on how to contact the maintainer of AID Submodel as URI scheme.",
    )
    endpoint_metadata: EndpointMetadata
    interaction_metadata: InteractionMetadata
    external_descriptor: Optional[ExternalDescriptor] = None

class InterfaceTemplateForMQTT(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/Interface"
    description: str = "Indicates entry point for MQTT interface."

    title: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#title",
        description="Provides a human-readable title to give a human-readable context of the interface.",
    )
    created: Property = Property(
        semantic_id="http://purl.org/dc/terms/created",
        description="Provides information when the AID Submodel was created.",
    )
    modified: Property = Property(
        semantic_id="http://purl.org/dc/terms/modified",
        description="Provides information when the AID Submodel was modified.",
    )
    support: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#supportContact",
        description="Provides an address on how to contact the maintainer of AID Submodel as URI scheme.",
    )
    endpoint_metadata: EndpointMetadata
    interaction_metadata: InteractionMetadata
    external_descriptor: Optional[ExternalDescriptor] = None

class opcua_channel_sc(SubmodelElementCollection):
    semantic_id: str = "http://opcfoundation.org/UA/WoT-Binding/OPCUASecurityChannelScheme"
    description: str = "This SubmodelElements holds the information about security mechanism based on opcua_channel security."

    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. The scheme for opcua_channel_sc is ua_channelsec.",
    )
    proxy: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#proxy",
        description="Provides address information of the proxy server the security configuration provides access to.",
    )
    uav_security_mode: Property = Property(
        semantic_id="http://opcfoundation.org/UA/WoT-Binding/securityMode ",
        description="Provides information about the security modes supported by the OPC UA server endpoint(e.g None, Sign,SignAndEncrypt)",
    )
    uav_security_policy: Property = Property(
        semantic_id="http://opcfoundation.org/UA/WoT-Binding/securityPolicy",
        description="Provides information about which policy options are available from the supported endpoints of the OPC UA server(e.g None, Basic256Sha256)",
    )

class opcua_authentication_sc(SubmodelElementCollection):
    semantic_id: str = "http://opcfoundation.org/UA/WoT-Binding/OPCUASecurityAuthenticationScheme "
    description: str = "This SubmodelElements holds the information about security mechanism based on opcua_authentication security."

    scheme: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#SecurityScheme",
        description="Defines the security mechanism that used during access. The scheme for opcua_authentication_sc is ua_authentication.",
    )
    proxy: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/security#proxy",
        description="Provides address information of the proxy server the security configuration provides access to.",
    )
    uav_user_identity_token: Property = Property(
        semantic_id="http://opcfoundation.org/UA/WoT-Binding/userIdentityToken",
        description="Provides information about which policy options are available from the supported endpoints of the OPC UA server (e.g Anonymous)",
    )
    uav_issue_token: ReferenceElement = ReferenceElement(
        semantic_id="http://opcfoundation.org/UA/WoT-Binding/issueToken",
        description="Provides reference to security scheme within SecurityDefinition SMC that holds information about the token to use (e.g OAuth2).",
    )

class InterfaceTemplateForOPCUA(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/Interface"
    description: str = "Indicates entry point for OPC UA interface."

    title: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#title",
        description="Provides a human-readable title to give a human-readable context of the interface.",
    )
    created: Property = Property(
        semantic_id="http://purl.org/dc/terms/created",
        description="Provides information when the AID Submodel was created.",
    )
    modified: Property = Property(
        semantic_id="http://purl.org/dc/terms/modified",
        description="Provides information when the AID Submodel was modified.",
    )
    support: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#supportContact",
        description="Provides an address on how to contact the maintainer of AID Submodel as URI scheme.",
    )
    endpoint_metadata: EndpointMetadata
    interaction_metadata: InteractionMetadata
    external_descriptor: Optional[ExternalDescriptor] = None

class uriVariables(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/td#hasUriTemplateSchema"
    description: str = "Defines URI template variables according to RFC6570 as a collection based on an interaction affordance data schema"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Constraint", value="Only applicable for object-based values"),
    ]

    # _ref suffix: field renamed from "property_name" (Pydantic name-collision workaround)
    property_name_ref: Optional[Dict[str, property_name]] = None

class bacv_hasMember(SubmodelElementCollection):
    semantic_id: str = "http://www.w3.org/2022/bacnet#hasMember"
    description: str = "Defines the member of a Sequence and List data type."

    bacv_is_i_s_o8601: Property = Property(
        semantic_id="http://www.w3.org/2022/bacnet#isIso8601",
        description="Current counter value",
    )
    bacv_has_binary_representation: Property = Property(
        semantic_id="http://www.w3.org/2022/bacnet#hasBinaryRepresentation",
        description="Current counter value",
    )
    bacv_has_member_: Optional[bacv_hasMember] = None
    bacv_has_named_member: List[properties] = []
    bacv_has_value_map: List[properties] = []

class bacv_hasDataType(SubmodelElementCollection):
    semantic_id: str = "http://www.w3.org/2022/bacnet#hasDataType"
    description: str = "Defines the type information of a BACnet payload. This SMC is used to abstract BACnet data model to human and machine readable model by still keeping its wire compatibility on the protocol."

    bacv_is_i_s_o8601: Property = Property(
        semantic_id="http://www.w3.org/2022/bacnet#isIso8601",
        description="Defines if the data uses ISO8601 format",
    )
    bacv_has_binary_representation: Property = Property(
        semantic_id="http://www.w3.org/2022/bacnet#hasBinaryRepresentation",
        description="Defines the payload\u2019s binary representation type. This term is used when the payload is an OctetString",
    )
    bacv_has_member: Optional[bacv_hasMember] = None
    bacv_has_named_member: List[properties] = []
    bacv_has_value_map: List[properties] = []

class InterfaceTemplateForBacnet(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/Interface"
    description: str = "Indicates entry point for BACnet interface."

    title: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#title",
        description="Provides a human-readable title to give a human-readable context of the interface.",
    )
    created: Property = Property(
        semantic_id="http://purl.org/dc/terms/created",
        description="Provides information when the AID Submodel was created.",
    )
    modified: Property = Property(
        semantic_id="http://purl.org/dc/terms/modified",
        description="Provides information when the AID Submodel was modified.",
    )
    support: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#supportContact",
        description="Provides an address on how to contact the maintainer of AID Submodel as URI scheme.",
    )
    endpoint_metadata: EndpointMetadata
    interaction_metadata: InteractionMetadata
    external_descriptor: Optional[ExternalDescriptor] = None

class InterfaceTemplateForIOLINK_OVER_PROFINET_REST(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/Interface"
    description: str = "Indicates entry point for IO Link over HTTP and PROFINET interface."

    title: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#title",
        description="Provides a human-readable title to give a human-readable context of the interface.",
    )
    created: Property = Property(
        semantic_id="http://purl.org/dc/terms/created",
        description="Provides information when the AID Submodel was created.",
    )
    modified: Property = Property(
        semantic_id="http://purl.org/dc/terms/modified",
        description="Provides information when the AID Submodel was modified.",
    )
    support: Property = Property(
        semantic_id="https://www.w3.org/2019/wot/td#supportContact",
        description="Provides an address on how to contact the maintainer of AID Submodel as URI scheme.",
    )
    endpoint_metadata: EndpointMetadata
    interaction_metadata: InteractionMetadata
    external_descriptor: Optional[ExternalDescriptor] = None

class AssetInterfacesDescription(Submodel):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/1/Submodel"
    description: str = "Definition of the Submodel Asset Interfaces Description identified by its semanticId. The Submodel idShort can be picked freely."
    VERSION: ClassVar[str] = "1"
    REVISION: ClassVar[str] = "1"

    interface_template_for_h_t_t_p: Optional[Dict[str, InterfaceTemplateForHTTP]] = None
    interface_template_for_m_o_d_b_u_s: Optional[Dict[str, InterfaceTemplateForMODBUS]] = None
    interface_template_for_m_q_t_t: Optional[Dict[str, InterfaceTemplateForMQTT]] = None
    interface_template_for_o_p_c_u_a: Optional[Dict[str, InterfaceTemplateForOPCUA]] = None
    interface_template_for_bacnet: Optional[Dict[str, InterfaceTemplateForBacnet]] = None
    interface_template_for_i_o_l_i_n_k__o_v_e_r__p_r_o_f_i_n_e_t__r_e_s_t: Optional[Dict[str, InterfaceTemplateForIOLINK_OVER_PROFINET_REST]] = None


# ── Resolve forward references (Pydantic circular refs) ──
security.model_rebuild()
nosec_sc.model_rebuild()
auto_sc.model_rebuild()
basic_sc.model_rebuild()
oneOf.model_rebuild()
allOf.model_rebuild()
combo_sc.model_rebuild()
apikey_sc.model_rebuild()
psk_sc.model_rebuild()
digest_sc.model_rebuild()
bearer_sc.model_rebuild()
scopes.model_rebuild()
oauth2_sc.model_rebuild()
securityDefinitions.model_rebuild()
EndpointMetadata.model_rebuild()
enum.model_rebuild()
items.model_rebuild()
properties.model_rebuild()
property_name.model_rebuild()
htv_headers.model_rebuild()
forms.model_rebuild()
actions.model_rebuild()
events.model_rebuild()
InteractionMetadata.model_rebuild()
ExternalDescriptor.model_rebuild()
InterfaceTemplateForHTTP.model_rebuild()
InterfaceTemplateForMODBUS.model_rebuild()
InterfaceTemplateForMQTT.model_rebuild()
opcua_channel_sc.model_rebuild()
opcua_authentication_sc.model_rebuild()
InterfaceTemplateForOPCUA.model_rebuild()
uriVariables.model_rebuild()
bacv_hasMember.model_rebuild()
bacv_hasDataType.model_rebuild()
InterfaceTemplateForBacnet.model_rebuild()
iolv_enumeratedValues.model_rebuild()
iolv_payloadMapping.model_rebuild()
InterfaceTemplateForIOLINK_OVER_PROFINET_REST.model_rebuild()
AssetInterfacesDescription.model_rebuild()