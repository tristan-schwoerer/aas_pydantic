"""Nameplate — generated from IDTA template."""

from typing import ClassVar, List, Optional
from pydantic import Field
from aas_pydantic import Submodel, SubmodelElementCollection, Capability, Qualifier

class AddressInformation(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/AddressInformation"
    description: str = "Note: this set of information is defined by SMT drop-in \"Address Information\""
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/Cardinality", value="One", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
    ]

    pass

class MarkingsItem(SubmodelElementCollection):
    semantic_id: str = "0112/2///61360_7#AAS009#001"
    description: str = "Note: CE marking is declared as mandatory according to the Blue Guide of the EU-Commission"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/Cardinality", value="OneToMany", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
    ]

    marking_name: str = Field("", json_schema_extra={"aas": {"semantic_id": "0112/2///61987#ABA231#009", "qualifiers": [{"type": "SMT/Cardinality", "value": "One", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    designation_of_certificate_or_approval: str = Field("", json_schema_extra={"aas": {"semantic_id": "0112/2///61987#ABH783#003", "description": "Note: Approval identifier, reference to the certificate number, to be entered without spaces ", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToOne", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    issue_date: str = Field("", json_schema_extra={"aas": {"semantic_id": "0112/2///61987#ABO097#001", "description": "Note: format by lexical representation: CCYY-MM-DD Note: to be specified to the day ", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToOne", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    expiry_date: str = Field("", json_schema_extra={"aas": {"semantic_id": "0112/2///61987#ABH830#002", "description": "Note: format by lexical representation: CCYY-MM-DD Note: to be specified to the day ", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToOne", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    marking_file: str = Field("", json_schema_extra={"aas": {"semantic_id": "0112/2///61987#ABO100#002", "qualifiers": [{"type": "SMT/Cardinality", "value": "One", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    marking_additional_text: str = Field("", json_schema_extra={"aas": {"semantic_id": "0112/2///61987#ABB146#007", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToMany", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})

class GuidelineSpecificPropertiesItem(SubmodelElementCollection):
    semantic_id: str = "0173-1#01-AHD205#004"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/Cardinality", value="OneToMany", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
    ]

    guideline_for_conformity_declaration: str = Field("", json_schema_extra={"aas": {"semantic_id": "0173-1#02-AAO856#002", "qualifiers": [{"type": "SMT/Cardinality", "value": "One", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    arbitrary_property: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/SMT/General/ArbitraryProp", "description": "Note: Every property can be used.", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToMany", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    arbitrary_file: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/SMT/General/ArbitraryFile", "description": "Note: Every file can be used.", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToMany", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    arbitrary_m_l_p: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/SMT/General/ArbitraryMLP", "description": "Note: Every multilanguage property can be used.", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToMany", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})

class AssetSpecificProperties(SubmodelElementCollection):
    semantic_id: str = "0173-1#02-ABI218#003/0173-1#01-AGZ672#004"
    qualifiers: List[Qualifier] = [
        Qualifier(type_="SMT/Cardinality", value="ZeroToOne", semantic_id="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"),
    ]

    arbitrary_property: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/SMT/General/ArbitraryProp", "description": "Note: Every property can be used.", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToMany", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    arbitrary_m_l_p: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/SMT/General/ArbitraryMLP", "description": "Note: Every multilanguage property can be used.", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToMany", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    arbitrary_file: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/SMT/General/ArbitraryFile", "description": "Note: Every file can be used.", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToMany", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    guideline_specific_properties: List[GuidelineSpecificPropertiesItem] = []

class Nameplate(Submodel):
    semantic_id: str = "https://admin-shell.io/idta/nameplate/3/0/Nameplate"
    description: str = "Contains the nameplate information attached to the product"
    VERSION: ClassVar[str] = "3"
    REVISION: ClassVar[str] = "0"

    u_r_i_of_the_product: str = Field("", json_schema_extra={"aas": {"semantic_id": "0112/2///61987#ABN590#002", "qualifiers": [{"type": "SMT/Cardinality", "value": "One", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    manufacturer_name: str = Field("", json_schema_extra={"aas": {"semantic_id": "0112/2///61987#ABA565#009", "qualifiers": [{"type": "SMT/Cardinality", "value": "One", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    manufacturer_product_designation: str = Field("", json_schema_extra={"aas": {"semantic_id": "0112/2///61987#ABA567#009", "qualifiers": [{"type": "SMT/Cardinality", "value": "One", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    address_information: Optional[AddressInformation] = None
    manufacturer_product_root: str = Field("", json_schema_extra={"aas": {"semantic_id": "0112/2///61360_7#AAS011#001", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToOne", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    manufacturer_product_family: str = Field("", json_schema_extra={"aas": {"semantic_id": "0112/2///61987#ABP464#002", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToOne", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    manufacturer_product_type: str = Field("", json_schema_extra={"aas": {"semantic_id": "0112/2///61987#ABA300#008", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToOne", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    order_code_of_manufacturer: str = Field("", json_schema_extra={"aas": {"semantic_id": "0112/2///61987#ABA950#008", "qualifiers": [{"type": "SMT/Cardinality", "value": "One", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    product_article_number_of_manufacturer: str = Field("", json_schema_extra={"aas": {"semantic_id": "0112/2///61987#ABA581#007", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToOne", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    serial_number: str = Field("", json_schema_extra={"aas": {"semantic_id": "0112/2///61987#ABA951#009", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToOne", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    year_of_construction: str = Field("", json_schema_extra={"aas": {"semantic_id": "0112/2///61987#ABP000#002", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToOne", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    date_of_manufacture: str = Field("", json_schema_extra={"aas": {"semantic_id": "0112/2///61987#ABB757#007", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToOne", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    hardware_version: str = Field("", json_schema_extra={"aas": {"semantic_id": "0112/2///61987#ABA926#008", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToOne", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    firmware_version: str = Field("", json_schema_extra={"aas": {"semantic_id": "0112/2///61987#ABA302#006", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToOne", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    software_version: str = Field("", json_schema_extra={"aas": {"semantic_id": "0112/2///61987#ABA601#008", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToOne", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    country_of_origin: str = Field("", json_schema_extra={"aas": {"semantic_id": "0112/2///61987#ABP462#001", "description": "Note: Country codes defined accord. to DIN EN ISO 3166-1 alpha-2 codes", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToOne", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    unique_facility_identifier: str = Field("", json_schema_extra={"aas": {"semantic_id": "https://admin-shell.io/idta/nameplate/3/0/UniqueFacilityIdentifier", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToOne", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    company_logo: str = Field("", json_schema_extra={"aas": {"semantic_id": "0112/2///61987#ABP463#001", "qualifiers": [{"type": "SMT/Cardinality", "value": "ZeroToOne", "semantic_id": "https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"}]}})
    markings: List[MarkingsItem] = []
    asset_specific_properties: Optional[AssetSpecificProperties] = None
