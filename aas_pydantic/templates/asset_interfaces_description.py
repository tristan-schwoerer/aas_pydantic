"""AssetInterfacesDescription — generated from IDTA template."""

from typing import ClassVar, List, Optional
from pydantic import Field
from aas_pydantic import Submodel, SubmodelElementCollection, Capability, Qualifier

class nosec_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#NoSecurityScheme"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
    ]

    scheme: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#SecurityScheme", "qualifiers": [{"type": "Cardinality", "value": "One"}]}})

class auto_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#AutoSecurityScheme"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
    ]

    scheme: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#SecurityScheme", "qualifiers": [{"type": "Cardinality", "value": "One"}]}})
    proxy: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#proxy", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})

class basic_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#BasicSecurityScheme"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
    ]

    scheme: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#SecurityScheme", "qualifiers": [{"type": "Cardinality", "value": "One"}]}})
    name: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#name", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    in: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#in", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    proxy: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#proxy", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})

class combo_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#ComboSecurityScheme"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
    ]

    scheme: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#SecurityScheme", "qualifiers": [{"type": "Cardinality", "value": "One"}]}})
    one_of: List[str] = Field([], json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#oneOf", "qualifiers": [{"type": "Cardinality", "value": "One"}]}})
    all_of: List[str] = Field([], json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#allOf", "qualifiers": [{"type": "Cardinality", "value": "One"}]}})
    proxy: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#proxy", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})

class apikey_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#APIKeySecurityScheme"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
    ]

    scheme: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#SecurityScheme", "qualifiers": [{"type": "Cardinality", "value": "One"}]}})
    name: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#name", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    in: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#in", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    proxy: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#proxy", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})

class psk_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#PSKSecurityScheme"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
    ]

    scheme: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#SecurityScheme", "qualifiers": [{"type": "Cardinality", "value": "One"}]}})
    identity: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#identity", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    proxy: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#proxy", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})

class digest_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#DigestSecurityScheme"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
    ]

    scheme: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#SecurityScheme", "qualifiers": [{"type": "Cardinality", "value": "One"}]}})
    name: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#name", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    in: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#in", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    qop: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#qop", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    proxy: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#proxy", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})

class bearer_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#BearerSecurityScheme"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
    ]

    scheme: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#SecurityScheme", "qualifiers": [{"type": "Cardinality", "value": "One"}]}})
    name: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#name", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    in: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#in", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    authorization: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#authorization", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    alg: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#alg", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    format: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#format", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    proxy: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#proxy", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})

class oauth2_sc(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/security#OAuth2SecurityScheme"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
    ]

    scheme: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#SecurityScheme", "qualifiers": [{"type": "Cardinality", "value": "One"}]}})
    token: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#token", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    refresh: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#refresh", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    authorization: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#authorization", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    scopes: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#scopes", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    flow: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#flow", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    proxy: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/security#proxy", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})

class securityDefinitions(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/td#definesSecurityScheme"
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
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="One"),
    ]

    base: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/td#base", "qualifiers": [{"type": "Cardinality", "value": "One"}]}})
    content_type: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/hypermedia#forContentType", "qualifiers": [{"type": "Cardinality", "value": "One"}]}})
    security: List[str] = Field([], json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/td#hasSecurityConfiguration", "qualifiers": [{"type": "Cardinality", "value": "One"}]}})
    security_definitions: Optional[securityDefinitions] = None

class items(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/json-schema#items"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
        Qualifier(type_="Constraint", value="Only applicable for array-based values"),
    ]

    type: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/1999/02/22-rdf-syntax-ns#type", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    value_semantics: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    unit: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://schema.org/unitCode", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    default: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/json-schema#default", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    const: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/json-schema#const", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    observable: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/td#isObservable", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    title: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/td#title", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    min_max: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}, {"type": "Constraint", "value": "Only applicable for number-/interger-based values"}, {"type": "Select", "value": "minimum | maximum | minimum AND maximum as supplementalSem.Id"}]}})
    length_range: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}, {"type": "Constraint", "value": "Only applicable for string-based values"}, {"type": "Select", "value": "minLength | maxLength | minLength AND maxLength as supplementalSem.Id"}]}})

class forms(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/td#hasForm"

    href: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/hypermedia#hasTarget", "qualifiers": [{"type": "Cardinality", "value": "One"}]}})
    content_type: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/hypermedia#forContentType", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    security: List[str] = Field([], json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/td#hasSecurityConfiguration", "qualifiers": [{"type": "Cardinality", "value": "One"}]}})
    mqv_retain: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/mqtt#hasRetainFlag", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}, {"type": "Constraint", "value": "Only applicable for MQTT binding"}]}})
    mqv_control_packet: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/mqtt#ControlPacket", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}, {"type": "Constraint", "value": "Only applicable for MQTT binding"}]}})
    mqv_qos: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/mqtt#hasQoSFlag", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}, {"type": "Constraint", "value": "Only applicable for MQTT binding"}]}})

class property_name(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfaceDescription/1/0/PropertyDefinition"
    description: str = "Current counter value"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToMany"),
    ]

    key: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/key", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    type: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/1999/02/22-rdf-syntax-ns#type", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    title: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/td#title", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    observable: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/td#isObservable", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    const: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/json-schema#const", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    default: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/json-schema#default", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    unit: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://schema.org/unitCode", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    min_max: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/minMaxRange", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}, {"type": "Constraint", "value": "Only applicable for number-/interger-based values"}, {"type": "Select", "value": "minimum | maximum | minimum AND maximum as supplementalSem.Id"}]}})
    length_range: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/lengthRange", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}, {"type": "Constraint", "value": "Only applicable for string-based values"}, {"type": "Select", "value": "minLength | maxLength | minLength AND maxLength as supplementalSem.Id"}]}})
    items: Optional[items] = None
    items_range: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/itemsRange", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}, {"type": "Constraint", "value": "Only applicable for string-based values"}, {"type": "Select", "value": "minItems | maxItems | minItems AND maxItems as supplementalSem.Id"}]}})
    properties: Optional[properties] = None
    value_semantics: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/valueSemantics", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    forms: Optional[forms] = None

class properties(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/td#PropertyAffordance"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
    ]

    property_name: Optional[property_name] = None

class htv_headersItem(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2011/http#headers"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="OneToMany"),
    ]

    htv_field_name: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2011/http#fieldName", "qualifiers": [{"type": "Cardinality", "value": "One"}]}})
    htv_field_value: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2011/http#fieldValue", "qualifiers": [{"type": "Cardinality", "value": "One"}]}})

class actions(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/td#ActionAffordance"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
    ]

    pass

class events(SubmodelElementCollection):
    semantic_id: str = "https://www.w3.org/2019/wot/td#EventAffordance"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
    ]

    pass

class InteractionMetadata(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/InteractionMetadata"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="One"),
    ]

    properties: Optional[properties] = None
    actions: Optional[actions] = None
    events: Optional[events] = None

class ExternalDescriptor(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/ExternalDescriptor"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToOne"),
    ]

    file_name: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/externalDescriptorName"}})

class InterfaceTemplateForHTTP(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/Interface"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToMany"),
    ]

    title: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/td#title", "qualifiers": [{"type": "Cardinality", "value": "One"}]}})
    created: str = Field("", json_schema_extra={"aas": {"semantic_id": "http://purl.org/dc/terms/created", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    modified: str = Field("", json_schema_extra={"aas": {"semantic_id": "http://purl.org/dc/terms/modified", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    support: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/td#supportContact", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    endpoint_metadata: Optional[EndpointMetadata] = None
    interaction_metadata: Optional[InteractionMetadata] = None
    external_descriptor: Optional[ExternalDescriptor] = None

class InterfaceTemplateForMODBUS(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/Interface"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToMany"),
    ]

    title: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/td#title", "qualifiers": [{"type": "Cardinality", "value": "One"}]}})
    created: str = Field("", json_schema_extra={"aas": {"semantic_id": "http://purl.org/dc/terms/created", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    modified: str = Field("", json_schema_extra={"aas": {"semantic_id": "http://purl.org/dc/terms/modified", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    support: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/td#support", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    endpoint_metadata: Optional[EndpointMetadata] = None
    interaction_metadata: Optional[InteractionMetadata] = None
    external_descriptor: Optional[ExternalDescriptor] = None

class InterfaceTemplateForMQTT(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/Interface"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="Cardinality", value="ZeroToMany"),
    ]

    title: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/td#title", "qualifiers": [{"type": "Cardinality", "value": "One"}]}})
    created: str = Field("", json_schema_extra={"aas": {"semantic_id": "http://purl.org/dc/terms/created", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    modified: str = Field("", json_schema_extra={"aas": {"semantic_id": "http://purl.org/dc/terms/modified", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    support: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://www.w3.org/2019/wot/td#support", "qualifiers": [{"type": "Cardinality", "value": "ZeroToOne"}]}})
    endpoint_metadata: Optional[EndpointMetadata] = None
    interaction_metadata: Optional[InteractionMetadata] = None
    external_descriptor: Optional[ExternalDescriptor] = None

class AssetInterfacesDescription(Submodel):
    semantic_id: str = "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/Submodel"
    description: str = "AID Template Sample"
    VERSION: ClassVar[str] = "1"
    REVISION: ClassVar[str] = "0"

    interface_template_for_h_t_t_p: Optional[InterfaceTemplateForHTTP] = None
    interface_template_for_m_o_d_b_u_s: Optional[InterfaceTemplateForMODBUS] = None
    interface_template_for_m_q_t_t: Optional[InterfaceTemplateForMQTT] = None
