"""Nameplate — generated from IDTA template."""

from __future__ import annotations

from typing import Any, ClassVar, List, Dict, Optional
from aas_pydantic import (
    File, MultiLanguageProperty, Property, Submodel, SubmodelElement, SubmodelElementCollection, SubmodelElementList,
)

class URIOfTheProduct(Property):
    semantic_id: str = "0112/2///61987#ABN590#002"
    supplemental_semantic_ids: List[str] = ["0173-1#02-ABH173#003"]
    value_type: str = "xs:anyURI"

class ManufacturerName(MultiLanguageProperty):
    semantic_id: str = "0112/2///61987#ABA565#009"
    supplemental_semantic_ids: List[str] = ["0173-1#02-AAO677#004"]

class ManufacturerProductDesignation(MultiLanguageProperty):
    semantic_id: str = "0112/2///61987#ABA567#009"
    supplemental_semantic_ids: List[str] = ["0173-1#02-AAW338#003"]

class Street(MultiLanguageProperty):
    semantic_id: str = "0173-1#02-AAO128#002"

class Zipcode(MultiLanguageProperty):
    semantic_id: str = "0173-1#02-AAO129#002"

class CityTown(MultiLanguageProperty):
    semantic_id: str = "0173-1#02-AAO132#002"

class NationalCode(MultiLanguageProperty):
    semantic_id: str = "0173-1#02-AAO134#002"

class AddressOfAdditionalLink(Property):
    semantic_id: str = "0173-1#02-AAQ326#002"
    value_type: str = "xs:string"

class AddressInformation(SubmodelElementCollection):
    semantic_id: str = "https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/AddressInformation"
    description: str = "Note: this set of information is defined by SMT drop-in \"Address Information\""
    supplemental_semantic_ids: List[str] = ["https://admin-shell.io/smt-dropin/smt-dropin-use/1/0", "0112/2///61360_7#AAS002#001", "0173-1#02-AAQ837#008/0173-1#01-ADR448#008"]
    street: Street
    zipcode: Zipcode
    city_town: CityTown
    national_code: NationalCode
    address_of_additional_link: Optional[AddressOfAdditionalLink] = None

class ManufacturerProductRoot(MultiLanguageProperty):
    semantic_id: str = "0112/2///61360_7#AAS011#001"
    supplemental_semantic_ids: List[str] = ["0173-1#02-AAU732#003"]

class ManufacturerProductFamily(MultiLanguageProperty):
    semantic_id: str = "0112/2///61987#ABP464#002"
    supplemental_semantic_ids: List[str] = ["0173-1#02-AAU731#003"]

class ManufacturerProductType(Property):
    semantic_id: str = "0112/2///61987#ABA300#008"
    supplemental_semantic_ids: List[str] = ["0173-1#02-AAO057#004"]
    value_type: str = "xs:string"

class OrderCodeOfManufacturer(Property):
    semantic_id: str = "0112/2///61987#ABA950#008"
    supplemental_semantic_ids: List[str] = ["0173-1#02-AAO227#004"]
    value_type: str = "xs:string"

class ProductArticleNumberOfManufacturer(Property):
    semantic_id: str = "0112/2///61987#ABA581#007"
    supplemental_semantic_ids: List[str] = ["0173-1#02-AAO676#005"]
    value_type: str = "xs:string"

class SerialNumber(Property):
    semantic_id: str = "0112/2///61987#ABA951#009"
    supplemental_semantic_ids: List[str] = ["0173-1#02-AAM556#004"]
    value_type: str = "xs:string"

class YearOfConstruction(Property):
    semantic_id: str = "0112/2///61987#ABP000#002"
    supplemental_semantic_ids: List[str] = ["0173-1#02-AAP906#003"]
    value_type: str = "xs:string"

class DateOfManufacture(Property):
    semantic_id: str = "0112/2///61987#ABB757#007"
    supplemental_semantic_ids: List[str] = ["0173-1#02-AAR972#004"]
    value_type: str = "xs:date"

class HardwareVersion(Property):
    semantic_id: str = "0112/2///61987#ABA926#008"
    supplemental_semantic_ids: List[str] = ["0173-1#02-AAN270#004"]
    value_type: str = "xs:string"

class FirmwareVersion(Property):
    semantic_id: str = "0112/2///61987#ABA302#006"
    supplemental_semantic_ids: List[str] = ["0173-1#02-AAM985#004"]
    value_type: str = "xs:string"

class SoftwareVersion(Property):
    semantic_id: str = "0112/2///61987#ABA601#008"
    supplemental_semantic_ids: List[str] = ["0173-1#02-AAM737#004"]
    value_type: str = "xs:string"

class CountryOfOrigin(Property):
    semantic_id: str = "0112/2///61987#ABP462#001"
    description: str = "Note: Country codes defined accord. to DIN EN ISO 3166-1 alpha-2 codes"
    supplemental_semantic_ids: List[str] = ["0173-1#02-AAO259#007"]
    value_type: str = "xs:string"

class UniqueFacilityIdentifier(Property):
    semantic_id: str = "https://admin-shell.io/idta/nameplate/3/0/UniqueFacilityIdentifier"
    value_type: str = "xs:string"

class CompanyLogo(File):
    semantic_id: str = "0112/2///61987#ABP463#001"
    supplemental_semantic_ids: List[str] = ["0173-1#02-ABI776#002"]
    content_type: str = "image/png"

class MarkingName(Property):
    semantic_id: str = "0112/2///61987#ABA231#009"
    supplemental_semantic_ids: List[str] = ["0173-1#02-ABI190#003"]
    value_type: str = "xs:string"

class DesignationOfCertificateOrApproval(Property):
    semantic_id: str = "0112/2///61987#ABH783#003"
    description: str = "Note: Approval identifier, reference to the certificate number, to be entered without spaces "
    supplemental_semantic_ids: List[str] = ["0173-1#02-ABI975#002"]
    value_type: str = "xs:string"

class IssueDate(Property):
    semantic_id: str = "0112/2///61987#ABO097#001"
    description: str = "Note: format by lexical representation: CCYY-MM-DD Note: to be specified to the day "
    supplemental_semantic_ids: List[str] = ["0173-1#02-ABL774#001"]
    value_type: str = "xs:date"

class ExpiryDate(Property):
    semantic_id: str = "0112/2///61987#ABH830#002"
    description: str = "Note: format by lexical representation: CCYY-MM-DD Note: to be specified to the day "
    supplemental_semantic_ids: List[str] = ["0173-1#02-ABL775#001"]
    value_type: str = "xs:date"

class MarkingFile(File):
    semantic_id: str = "0112/2///61987#ABO100#002"
    supplemental_semantic_ids: List[str] = ["0173-1#02-ABI191#003"]
    content_type: str = "image/png"

class MarkingAdditionalText(Property):
    semantic_id: str = "0112/2///61987#ABB146#007"
    supplemental_semantic_ids: List[str] = ["0173-1#02-ABI192#003"]
    value_type: str = "xs:string"

class MarkingsItem(SubmodelElementCollection):
    semantic_id: str = "0112/2///61360_7#AAS009#001"
    description: str = "Note: CE marking is declared as mandatory according to the Blue Guide of the EU-Commission"
    supplemental_semantic_ids: List[str] = ["0173-1#02-ABI564#003/0173-1#01-AHF850#003"]
    marking_name: MarkingName
    designation_of_certificate_or_approval: Optional[DesignationOfCertificateOrApproval] = None
    issue_date: Optional[IssueDate] = None
    expiry_date: Optional[ExpiryDate] = None
    marking_file: MarkingFile
    marking_additional_text: Dict[str, MarkingAdditionalText] = {}

class Markings(SubmodelElementList):
    semantic_id: str = "0112/2///61360_7#AAS006#001"
    description: str = "Note: CE marking is declared as mandatory according to EU Blue Guide"
    supplemental_semantic_ids: List[str] = ["0173-1#02-ABI563#003/0173-1#01-AHF849#003"]
    item_type: ClassVar = MarkingsItem
    value: List[MarkingsItem] = []

class ArbitraryProperty(Property):
    semantic_id: str = "https://admin-shell.io/SMT/General/ArbitraryProp"
    description: str = "Note: Every property can be used."
    value_type: str = "xs:string"

class ArbitraryMLP(MultiLanguageProperty):
    semantic_id: str = "https://admin-shell.io/SMT/General/ArbitraryMLP"
    description: str = "Note: Every multilanguage property can be used."

class ArbitraryFile(File):
    semantic_id: str = "https://admin-shell.io/SMT/General/ArbitraryFile"
    description: str = "Note: Every file can be used."
    content_type: str = "application/pdf"

class GuidelineForConformityDeclaration(Property):
    semantic_id: str = "0173-1#02-AAO856#002"
    value_type: str = "xs:string"

class GuidelineSpecificPropertiesItem(SubmodelElementCollection):
    semantic_id: str = "0173-1#01-AHD205#004"
    guideline_for_conformity_declaration: GuidelineForConformityDeclaration
    arbitrary_property: Dict[str, ArbitraryProperty] = {}
    arbitrary_file: Dict[str, ArbitraryFile] = {}
    arbitrary_m_l_p: Dict[str, ArbitraryMLP] = {}

class GuidelineSpecificProperties(SubmodelElementList):
    semantic_id: str = "0173-1#02-ABI219#003/0173-1#01-AHD205#004"
    item_type: ClassVar = GuidelineSpecificPropertiesItem
    value: List[GuidelineSpecificPropertiesItem] = []

class AssetSpecificProperties(SubmodelElementCollection):
    semantic_id: str = "0173-1#02-ABI218#003/0173-1#01-AGZ672#004"
    arbitrary_property: Dict[str, ArbitraryProperty] = {}
    arbitrary_m_l_p: Dict[str, ArbitraryMLP] = {}
    arbitrary_file: Dict[str, ArbitraryFile] = {}
    guideline_specific_properties: Optional[GuidelineSpecificProperties] = None

class Nameplate(Submodel):
    semantic_id: str = "https://admin-shell.io/idta/nameplate/3/0/Nameplate"
    description: str = "Contains the nameplate information attached to the product"
    VERSION: ClassVar[str] = "3"
    REVISION: ClassVar[str] = "0"
    u_r_i_of_the_product: URIOfTheProduct
    manufacturer_name: ManufacturerName
    manufacturer_product_designation: ManufacturerProductDesignation
    address_information: AddressInformation
    manufacturer_product_root: Optional[ManufacturerProductRoot] = None
    manufacturer_product_family: Optional[ManufacturerProductFamily] = None
    manufacturer_product_type: Optional[ManufacturerProductType] = None
    order_code_of_manufacturer: OrderCodeOfManufacturer
    product_article_number_of_manufacturer: Optional[ProductArticleNumberOfManufacturer] = None
    serial_number: Optional[SerialNumber] = None
    year_of_construction: Optional[YearOfConstruction] = None
    date_of_manufacture: Optional[DateOfManufacture] = None
    hardware_version: Optional[HardwareVersion] = None
    firmware_version: Optional[FirmwareVersion] = None
    software_version: Optional[SoftwareVersion] = None
    country_of_origin: Optional[CountryOfOrigin] = None
    unique_facility_identifier: Optional[UniqueFacilityIdentifier] = None
    company_logo: Optional[CompanyLogo] = None
    markings: Optional[Markings] = None
    asset_specific_properties: Optional[AssetSpecificProperties] = None

# ── Resolve forward references (Pydantic circular refs) ──
URIOfTheProduct.model_rebuild()
ManufacturerName.model_rebuild()
ManufacturerProductDesignation.model_rebuild()
Street.model_rebuild()
Zipcode.model_rebuild()
CityTown.model_rebuild()
NationalCode.model_rebuild()
AddressOfAdditionalLink.model_rebuild()
AddressInformation.model_rebuild()
ManufacturerProductRoot.model_rebuild()
ManufacturerProductFamily.model_rebuild()
ManufacturerProductType.model_rebuild()
OrderCodeOfManufacturer.model_rebuild()
ProductArticleNumberOfManufacturer.model_rebuild()
SerialNumber.model_rebuild()
YearOfConstruction.model_rebuild()
DateOfManufacture.model_rebuild()
HardwareVersion.model_rebuild()
FirmwareVersion.model_rebuild()
SoftwareVersion.model_rebuild()
CountryOfOrigin.model_rebuild()
UniqueFacilityIdentifier.model_rebuild()
CompanyLogo.model_rebuild()
MarkingName.model_rebuild()
DesignationOfCertificateOrApproval.model_rebuild()
IssueDate.model_rebuild()
ExpiryDate.model_rebuild()
MarkingFile.model_rebuild()
MarkingAdditionalText.model_rebuild()
MarkingsItem.model_rebuild()
Markings.model_rebuild()
ArbitraryProperty.model_rebuild()
ArbitraryMLP.model_rebuild()
ArbitraryFile.model_rebuild()
GuidelineForConformityDeclaration.model_rebuild()
GuidelineSpecificPropertiesItem.model_rebuild()
GuidelineSpecificProperties.model_rebuild()
AssetSpecificProperties.model_rebuild()
Nameplate.model_rebuild()
