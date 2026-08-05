"""Nameplate — generated from IDTA template."""

from __future__ import annotations

from typing import Any, ClassVar, List, Dict
from aas_pydantic import (
    ContainerValue, File, MultiLanguageProperty, Property, Submodel, SubmodelElement, SubmodelElementCollection, SubmodelElementList,
)

class AddressInformationValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    pass

class AddressInformation(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/AddressInformation"
    description: str = "Note: this set of information is defined by SMT drop-in \"Address Information\""
    supplemental_semantic_ids: List[str] = ["https://admin-shell.io/smt-dropin/smt-dropin-use/1/0", "0112/2///61360_7#AAS002#001", "0173-1#02-AAQ837#008/0173-1#01-ADR448#008"]
    value: AddressInformationValues = AddressInformationValues()

class MarkingAdditionalText(Property):
    semantic_id: str = "0112/2///61987#ABB146#007"
    supplemental_semantic_ids: List[str] = ["0173-1#02-ABI192#003"]

class MarkingsItemValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    marking_name: Property = Property(
        semantic_id="0112/2///61987#ABA231#009",
        value_type="xs:string",
    )
    designation_of_certificate_or_approval: Property = Property(
        semantic_id="0112/2///61987#ABH783#003",
        description="Note: Approval identifier, reference to the certificate number, to be entered without spaces ",
        value_type="xs:string",
    )
    issue_date: Property = Property(
        semantic_id="0112/2///61987#ABO097#001",
        description="Note: format by lexical representation: CCYY-MM-DD Note: to be specified to the day ",
        value_type="xs:date",
    )
    expiry_date: Property = Property(
        semantic_id="0112/2///61987#ABH830#002",
        description="Note: format by lexical representation: CCYY-MM-DD Note: to be specified to the day ",
        value_type="xs:date",
    )
    marking_file: File = File(
        semantic_id="0112/2///61987#ABO100#002",
    )
    marking_additional_text: Dict[str, MarkingAdditionalText] = {}

class MarkingsItem(SubmodelElementCollection):
    semantic_id: str = "0112/2///61360_7#AAS009#001"
    description: str = "Note: CE marking is declared as mandatory according to the Blue Guide of the EU-Commission"
    supplemental_semantic_ids: List[str] = ["0173-1#02-ABI564#003/0173-1#01-AHF850#003"]
    value: MarkingsItemValues = MarkingsItemValues()

class Markings(SubmodelElementList):
    semantic_id: str = "0112/2///61360_7#AAS006#001"
    description: str = "Note: CE marking is declared as mandatory according to EU Blue Guide"
    supplemental_semantic_ids: List[str] = ["0173-1#02-ABI563#003/0173-1#01-AHF849#003"]
    item_type: ClassVar = MarkingsItem
    value: List[MarkingsItem] = [
        MarkingsItem(id_short="MarkingsItem"),
    ]

class ArbitraryProperty(Property):
    semantic_id: str = "https://admin-shell.io/SMT/General/ArbitraryProp"
    description: str = "Note: Every property can be used."

class ArbitraryMLP(MultiLanguageProperty):
    semantic_id: str = "https://admin-shell.io/SMT/General/ArbitraryMLP"
    description: str = "Note: Every multilanguage property can be used."

class ArbitraryFile(File):
    semantic_id: str = "https://admin-shell.io/SMT/General/ArbitraryFile"
    description: str = "Note: Every file can be used."

class GuidelineSpecificPropertiesItemValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    guideline_for_conformity_declaration: Property = Property(
        semantic_id="0173-1#02-AAO856#002",
        value_type="xs:string",
    )
    arbitrary_property: Dict[str, ArbitraryProperty] = {}
    arbitrary_file: Dict[str, ArbitraryFile] = {}
    arbitrary_m_l_p: Dict[str, ArbitraryMLP] = {}

class GuidelineSpecificPropertiesItem(SubmodelElementCollection):
    semantic_id: str = "0173-1#01-AHD205#004"
    value: GuidelineSpecificPropertiesItemValues = GuidelineSpecificPropertiesItemValues()

class GuidelineSpecificProperties(SubmodelElementList):
    semantic_id: str = "0173-1#02-ABI219#003/0173-1#01-AHD205#004"
    item_type: ClassVar = GuidelineSpecificPropertiesItem
    value: List[GuidelineSpecificPropertiesItem] = [
        GuidelineSpecificPropertiesItem(id_short="GuidelineSpecificPropertiesItem"),
    ]

class AssetSpecificPropertiesValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    arbitrary_property: Dict[str, ArbitraryProperty] = {}
    arbitrary_m_l_p: Dict[str, ArbitraryMLP] = {}
    arbitrary_file: Dict[str, ArbitraryFile] = {}
    guideline_specific_properties: GuidelineSpecificProperties = GuidelineSpecificProperties()

class AssetSpecificProperties(SubmodelElementCollection):
    semantic_id: str = "0173-1#02-ABI218#003/0173-1#01-AGZ672#004"
    value: AssetSpecificPropertiesValues = AssetSpecificPropertiesValues()

class NameplateValues(ContainerValue):
    model_config = {'extra': 'forbid'}
    u_r_i_of_the_product: Property = Property(
        semantic_id="0112/2///61987#ABN590#002",
        value_type="xs:anyURI",
    )
    manufacturer_name: MultiLanguageProperty = MultiLanguageProperty(
        semantic_id="0112/2///61987#ABA565#009",
    )
    manufacturer_product_designation: MultiLanguageProperty = MultiLanguageProperty(
        semantic_id="0112/2///61987#ABA567#009",
    )
    address_information: AddressInformation = AddressInformation()
    manufacturer_product_root: MultiLanguageProperty = MultiLanguageProperty(
        semantic_id="0112/2///61360_7#AAS011#001",
    )
    manufacturer_product_family: MultiLanguageProperty = MultiLanguageProperty(
        semantic_id="0112/2///61987#ABP464#002",
    )
    manufacturer_product_type: Property = Property(
        semantic_id="0112/2///61987#ABA300#008",
        value_type="xs:string",
    )
    order_code_of_manufacturer: Property = Property(
        semantic_id="0112/2///61987#ABA950#008",
        value_type="xs:string",
    )
    product_article_number_of_manufacturer: Property = Property(
        semantic_id="0112/2///61987#ABA581#007",
        value_type="xs:string",
    )
    serial_number: Property = Property(
        semantic_id="0112/2///61987#ABA951#009",
        value_type="xs:string",
    )
    year_of_construction: Property = Property(
        semantic_id="0112/2///61987#ABP000#002",
        value_type="xs:string",
    )
    date_of_manufacture: Property = Property(
        semantic_id="0112/2///61987#ABB757#007",
        value_type="xs:date",
    )
    hardware_version: Property = Property(
        semantic_id="0112/2///61987#ABA926#008",
        value_type="xs:string",
    )
    firmware_version: Property = Property(
        semantic_id="0112/2///61987#ABA302#006",
        value_type="xs:string",
    )
    software_version: Property = Property(
        semantic_id="0112/2///61987#ABA601#008",
        value_type="xs:string",
    )
    country_of_origin: Property = Property(
        semantic_id="0112/2///61987#ABP462#001",
        description="Note: Country codes defined accord. to DIN EN ISO 3166-1 alpha-2 codes",
        value_type="xs:string",
    )
    unique_facility_identifier: Property = Property(
        semantic_id="https://admin-shell.io/idta/nameplate/3/0/UniqueFacilityIdentifier",
        value_type="xs:string",
    )
    company_logo: File = File(
        semantic_id="0112/2///61987#ABP463#001",
    )
    markings: Markings = Markings()
    asset_specific_properties: AssetSpecificProperties = AssetSpecificProperties()

class Nameplate(Submodel):
    semantic_id: str = "https://admin-shell.io/idta/nameplate/3/0/Nameplate"
    description: str = "Contains the nameplate information attached to the product"
    VERSION: ClassVar[str] = "3"
    REVISION: ClassVar[str] = "0"
    submodel_element: NameplateValues = NameplateValues()

# ── Resolve forward references (Pydantic circular refs) ──
AddressInformationValues.model_rebuild()
AddressInformation.model_rebuild()
MarkingAdditionalText.model_rebuild()
MarkingsItemValues.model_rebuild()
MarkingsItem.model_rebuild()
Markings.model_rebuild()
ArbitraryProperty.model_rebuild()
ArbitraryMLP.model_rebuild()
ArbitraryFile.model_rebuild()
GuidelineSpecificPropertiesItemValues.model_rebuild()
GuidelineSpecificPropertiesItem.model_rebuild()
GuidelineSpecificProperties.model_rebuild()
AssetSpecificPropertiesValues.model_rebuild()
AssetSpecificProperties.model_rebuild()
NameplateValues.model_rebuild()
Nameplate.model_rebuild()
