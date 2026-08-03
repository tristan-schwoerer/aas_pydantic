"""Nameplate — generated from IDTA template."""

from __future__ import annotations

from typing import ClassVar, Dict, List, Optional
from aas_pydantic import (
    File, MultiLanguageProperty, Property, Qualifier, Submodel, SubmodelElement, SubmodelElementCollection, SubmodelElementList,
)

class AddressInformation(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/AddressInformation"
    description: str = "Note: this set of information is defined by SMT drop-in \"Address Information\""

    pass

class Markings(SubmodelElementList):
    semantic_id: str = "0112/2///61360_7#AAS006#001"
    description: str = "Note: CE marking is declared as mandatory according to EU Blue Guide"

    value: List[None] = []

class GuidelineSpecificProperties(SubmodelElementList):
    semantic_id: str = "0173-1#02-ABI219#003/0173-1#01-AHD205#004"

    value: List[None] = []

class AssetSpecificProperties(SubmodelElementCollection):
    semantic_id: str = "0173-1#02-ABI218#003/0173-1#01-AGZ672#004"

    arbitrary_property: Property = Property(
        semantic_id="https://admin-shell.io/SMT/General/ArbitraryProp",
        description="Note: Every property can be used.",
    )
    arbitrary_m_l_p: MultiLanguageProperty = MultiLanguageProperty(
        semantic_id="https://admin-shell.io/SMT/General/ArbitraryMLP",
        description="Note: Every multilanguage property can be used.",
    )
    arbitrary_file: File = File(
        semantic_id="https://admin-shell.io/SMT/General/ArbitraryFile",
        description="Note: Every file can be used.",
    )
    guideline_specific_properties: GuidelineSpecificProperties = GuidelineSpecificProperties(id_short="GuidelineSpecificProperties")

class Nameplate(Submodel):
    semantic_id: str = "https://admin-shell.io/idta/nameplate/3/0/Nameplate"
    description: str = "Contains the nameplate information attached to the product"
    VERSION: ClassVar[str] = "3"
    REVISION: ClassVar[str] = "0"

    u_r_i_of_the_product: Property = Property(
        semantic_id="0112/2///61987#ABN590#002",
    )
    manufacturer_name: MultiLanguageProperty = MultiLanguageProperty(
        semantic_id="0112/2///61987#ABA565#009",
    )
    manufacturer_product_designation: MultiLanguageProperty = MultiLanguageProperty(
        semantic_id="0112/2///61987#ABA567#009",
    )
    address_information: Optional[AddressInformation] = None
    manufacturer_product_root: MultiLanguageProperty = MultiLanguageProperty(
        semantic_id="0112/2///61360_7#AAS011#001",
    )
    manufacturer_product_family: MultiLanguageProperty = MultiLanguageProperty(
        semantic_id="0112/2///61987#ABP464#002",
    )
    manufacturer_product_type: Property = Property(
        semantic_id="0112/2///61987#ABA300#008",
    )
    order_code_of_manufacturer: Property = Property(
        semantic_id="0112/2///61987#ABA950#008",
    )
    product_article_number_of_manufacturer: Property = Property(
        semantic_id="0112/2///61987#ABA581#007",
    )
    serial_number: Property = Property(
        semantic_id="0112/2///61987#ABA951#009",
    )
    year_of_construction: Property = Property(
        semantic_id="0112/2///61987#ABP000#002",
    )
    date_of_manufacture: Property = Property(
        semantic_id="0112/2///61987#ABB757#007",
    )
    hardware_version: Property = Property(
        semantic_id="0112/2///61987#ABA926#008",
    )
    firmware_version: Property = Property(
        semantic_id="0112/2///61987#ABA302#006",
    )
    software_version: Property = Property(
        semantic_id="0112/2///61987#ABA601#008",
    )
    country_of_origin: Property = Property(
        semantic_id="0112/2///61987#ABP462#001",
        description="Note: Country codes defined accord. to DIN EN ISO 3166-1 alpha-2 codes",
    )
    unique_facility_identifier: Property = Property(
        semantic_id="https://admin-shell.io/idta/nameplate/3/0/UniqueFacilityIdentifier",
    )
    company_logo: File = File(
        semantic_id="0112/2///61987#ABP463#001",
    )
    markings: Markings = Markings(id_short="Markings")
    asset_specific_properties: Optional[AssetSpecificProperties] = None


# ── Resolve forward references (Pydantic circular refs) ──
AddressInformation.model_rebuild()
Markings.model_rebuild()
GuidelineSpecificProperties.model_rebuild()
AssetSpecificProperties.model_rebuild()
Nameplate.model_rebuild()