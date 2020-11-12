import requests
from bs4 import BeautifulSoup
import pdfrw
import re

from pdf.exceptions.custom_exceptions import InvalidPropertyType

FORM_KEYS_ATTACHED = dict()
FORM_KEYS_DETACHED = dict()
CHECKBOX_PDF_TYPE = 'checkbox'
STRING_PDF_TYPE = 'string'
FORM_KEYS_ATTACHED.update({
    'property_details': STRING_PDF_TYPE,
    'parcel_identification_number': STRING_PDF_TYPE,
    'agent_details_name': STRING_PDF_TYPE,
    'agent_details_company_page_1': STRING_PDF_TYPE,
    'agent_details_company_page_3': STRING_PDF_TYPE,
    'hoa_dues': STRING_PDF_TYPE,
    'tax': STRING_PDF_TYPE,
    'tax_year': STRING_PDF_TYPE,
    'tax_exemptions_yes': CHECKBOX_PDF_TYPE,
    'tax_exemptions_no': CHECKBOX_PDF_TYPE,
    'refrigerator_yes': CHECKBOX_PDF_TYPE,
    'refrigerator_details': STRING_PDF_TYPE,
    'oven_or_range_yes': CHECKBOX_PDF_TYPE,
    'oven_or_range_details': STRING_PDF_TYPE,
    'microware_yes': CHECKBOX_PDF_TYPE,
    'microwave_details': STRING_PDF_TYPE,
    'dishwasher_yes': CHECKBOX_PDF_TYPE,
    'dishwasher_details': STRING_PDF_TYPE,
    'garbage_disposal_yes': CHECKBOX_PDF_TYPE,
    'garbage_disposal_details': STRING_PDF_TYPE,
    'trash_compactor_yes': CHECKBOX_PDF_TYPE,
    'trash_compactor_details': STRING_PDF_TYPE,
    'washer_yes': CHECKBOX_PDF_TYPE,
    'washer_details': STRING_PDF_TYPE,
    'dryer_yes': CHECKBOX_PDF_TYPE,
    'dryer_details': STRING_PDF_TYPE,
    'water_softener_yes': CHECKBOX_PDF_TYPE,
    'water_softner_details': STRING_PDF_TYPE,
    'sump_pump_yes': CHECKBOX_PDF_TYPE,
    'sump_pump_details': STRING_PDF_TYPE,
    'smoke_and_monoxide_detectors_yes': CHECKBOX_PDF_TYPE,
    'smoke_and_carbon_monoxide_detectors_details': STRING_PDF_TYPE,
    'intercom_system_yes': CHECKBOX_PDF_TYPE,
    'intercom_system_details': STRING_PDF_TYPE,
    'security_system_yes': CHECKBOX_PDF_TYPE,
    'security_system_details': STRING_PDF_TYPE,
    'security_system_rented_yes': CHECKBOX_PDF_TYPE,
    'security_system_owned_yes': CHECKBOX_PDF_TYPE,
    'satellite_dish_yes': CHECKBOX_PDF_TYPE,
    'satellite_dish_details': STRING_PDF_TYPE,
    'attached_tv_yes': CHECKBOX_PDF_TYPE,
    'attached_tv_details': STRING_PDF_TYPE,
    'tv_antenna_yes': CHECKBOX_PDF_TYPE,
    'tv_antenna_details': STRING_PDF_TYPE,
    'multimedia_equipment_yes': CHECKBOX_PDF_TYPE,
    'multimedia_equipment_details': STRING_PDF_TYPE,
    'central_air_conditioner_yes': CHECKBOX_PDF_TYPE,
    'central_air_conditioner_details': STRING_PDF_TYPE,
    'window_air_conditioner_yes': CHECKBOX_PDF_TYPE,
    'window_air_conditioner_details': STRING_PDF_TYPE,
    'electronic_air_filter_yes': CHECKBOX_PDF_TYPE,
    'electronic_air_filter_details': STRING_PDF_TYPE,
    'central_humidifier_yes': CHECKBOX_PDF_TYPE,
    'central_humidifier_details': STRING_PDF_TYPE,
    'lighting_fixtures_yes': CHECKBOX_PDF_TYPE,
    'lighting_fixtures_details': STRING_PDF_TYPE,
    'electronic_garage_door_yes': CHECKBOX_PDF_TYPE,
    'electronic_garage_door_with_remote_unit_details': STRING_PDF_TYPE,
    'tacked_down_carpeting_yes': CHECKBOX_PDF_TYPE,
    'fireplace_screen_and_equipment_yes': CHECKBOX_PDF_TYPE,
    'fireplace_screen_and_equipment_details': STRING_PDF_TYPE,
    'fireplace_gas_log_yes': CHECKBOX_PDF_TYPE,
    'fireplace_gas_log_details': STRING_PDF_TYPE,
    'firewood_yes': CHECKBOX_PDF_TYPE,
    'firewood_details': STRING_PDF_TYPE,
    'attached_gas_grill_yes': CHECKBOX_PDF_TYPE,
    'attached_gas_grill_details': STRING_PDF_TYPE,
    'existing_storms_and_screens_yes': CHECKBOX_PDF_TYPE,
    'existing_storms_and_screens_details': STRING_PDF_TYPE,
    'window_treatments_yes': CHECKBOX_PDF_TYPE,
    'window_treatments_details': STRING_PDF_TYPE,
    'other_equipment_yes': CHECKBOX_PDF_TYPE,
    'other_equipment_details': STRING_PDF_TYPE,
    'built_in_or_attached_shelves_or_cabinets_yes': CHECKBOX_PDF_TYPE,
    'built_int_or_attached_shelves_or_cabinets_details': STRING_PDF_TYPE,
    'ceiling_fan_yes': CHECKBOX_PDF_TYPE,
    'ceiling_fan_details': STRING_PDF_TYPE,
    'radiator_covers_yes': CHECKBOX_PDF_TYPE,
    'radiator_covers_details': STRING_PDF_TYPE,
    'all_planted_vegetation_yes': CHECKBOX_PDF_TYPE,
    'outdoor_play_set_or_swings_yes': CHECKBOX_PDF_TYPE,
    'outdoor_shed_yes': CHECKBOX_PDF_TYPE,
    'purchase_price': STRING_PDF_TYPE,
    'credit_buyer_at_closing_yes': CHECKBOX_PDF_TYPE,
    'credit_buyer_at_closing_if_yes_amount': STRING_PDF_TYPE,
    'credit_buyer_at_closing_no': CHECKBOX_PDF_TYPE,
    'credit_buyer_at_closing_if_no_percentage': STRING_PDF_TYPE,
    'home_warranty_amount': STRING_PDF_TYPE,
    'brokerage_for_earnest_money': STRING_PDF_TYPE,
    'initial_earnest_money_amount': STRING_PDF_TYPE,
    'how_buyer_deposits_earnest_money': STRING_PDF_TYPE,
    'initial_earnest_money_due_date': STRING_PDF_TYPE,
    'balance_of_earnest_money_amount': STRING_PDF_TYPE,
    'balance_of_earnest_money_due_date': STRING_PDF_TYPE,
    'contract_subject_to_mortgage_yes': CHECKBOX_PDF_TYPE,
    'contract_subject_to_mortgage_no': CHECKBOX_PDF_TYPE,
    'mortgage_contingency_date': STRING_PDF_TYPE,
    'buyer_loan_to_value': STRING_PDF_TYPE,
    'buyer_interest_rate': STRING_PDF_TYPE,
    'buyer_loan_term': STRING_PDF_TYPE,
    'closing_date': STRING_PDF_TYPE,
    'disclosures_a_yes': CHECKBOX_PDF_TYPE,
    'disclosures_a_no': CHECKBOX_PDF_TYPE,
    'disclosures_b_yes': CHECKBOX_PDF_TYPE,
    'disclosures_b_no': CHECKBOX_PDF_TYPE,
    'disclosures_c_yes': CHECKBOX_PDF_TYPE,
    'disclosures_c_no': CHECKBOX_PDF_TYPE,
    'disclosures_d_yes': CHECKBOX_PDF_TYPE,
    'disclosures_d_no': CHECKBOX_PDF_TYPE,
    'dual_agent_broker_yes': CHECKBOX_PDF_TYPE,
    'dual_agent_broker_no': CHECKBOX_PDF_TYPE,
    'dual_agent_broker_name': STRING_PDF_TYPE,
    'length_of_attorney_review': STRING_PDF_TYPE,
    'length_of_inspection_period': STRING_PDF_TYPE,
    'offer_date': STRING_PDF_TYPE,
    'designated_agent': STRING_PDF_TYPE,
    'agent_mls': STRING_PDF_TYPE,
    'agent_license': STRING_PDF_TYPE,
    'brokerage': STRING_PDF_TYPE,
    'brokerage_mls': STRING_PDF_TYPE,
    'brokerage_license': STRING_PDF_TYPE,
    'broker_address': STRING_PDF_TYPE,
    'agent_phone': STRING_PDF_TYPE,
    'agent_fax': STRING_PDF_TYPE,
    'broker_email': STRING_PDF_TYPE,
    'attorney_name': STRING_PDF_TYPE,
    'attorney_address': STRING_PDF_TYPE,
    'attorney_phone': STRING_PDF_TYPE,
    'attorney_fax': STRING_PDF_TYPE,
    'attorney_email': STRING_PDF_TYPE,
    'lender_name': STRING_PDF_TYPE,
    'lender_company': STRING_PDF_TYPE,
    'lender_address': STRING_PDF_TYPE,
    'lender_phone': STRING_PDF_TYPE,
    'lender_fax': STRING_PDF_TYPE,
    'lender_email': STRING_PDF_TYPE,
    'buyer_name': STRING_PDF_TYPE,
    'seller_name': STRING_PDF_TYPE,
    'special_assessment_yes': CHECKBOX_PDF_TYPE,
    'special_assessment_no': CHECKBOX_PDF_TYPE,
    'deliver_association': STRING_PDF_TYPE,
    'homeowner': CHECKBOX_PDF_TYPE,
    'senior': CHECKBOX_PDF_TYPE,
    'senior_freeze': CHECKBOX_PDF_TYPE,
    'historical': CHECKBOX_PDF_TYPE,
    'prorated': STRING_PDF_TYPE,
    'parking_space_numbers': STRING_PDF_TYPE,
    'deeded': CHECKBOX_PDF_TYPE,
    'assigned': CHECKBOX_PDF_TYPE,
    'indoor': CHECKBOX_PDF_TYPE,
    'outdoor': CHECKBOX_PDF_TYPE,
    'limited_common_element': CHECKBOX_PDF_TYPE,
    'parking_pin': STRING_PDF_TYPE,
})
FORM_KEYS_DETACHED.update({
    'property_details': STRING_PDF_TYPE,
    'parcel_identification_number': STRING_PDF_TYPE,
    'tax_exemptions_yes': CHECKBOX_PDF_TYPE,
    'tax_exemptions_no': CHECKBOX_PDF_TYPE,
    'refrigerator_yes': CHECKBOX_PDF_TYPE,
    'refrigerator_details': STRING_PDF_TYPE,
    'oven_or_range_yes': CHECKBOX_PDF_TYPE,
    'oven_or_range_details': STRING_PDF_TYPE,
    'microware_yes': CHECKBOX_PDF_TYPE,
    'microwave_details': STRING_PDF_TYPE,
    'dishwasher_yes': CHECKBOX_PDF_TYPE,
    'dishwasher_details': STRING_PDF_TYPE,
    'garbage_disposal_yes': CHECKBOX_PDF_TYPE,
    'garbage_disposal_details': STRING_PDF_TYPE,
    'trash_compactor_yes': CHECKBOX_PDF_TYPE,
    'trash_compactor_details': STRING_PDF_TYPE,
    'washer_yes': CHECKBOX_PDF_TYPE,
    'washer_details': STRING_PDF_TYPE,
    'dryer_yes': CHECKBOX_PDF_TYPE,
    'dryer_details': STRING_PDF_TYPE,
    'water_softener_yes': CHECKBOX_PDF_TYPE,
    'water_softner_details': STRING_PDF_TYPE,
    'sump_pump_yes': CHECKBOX_PDF_TYPE,
    'sump_pump_details': STRING_PDF_TYPE,
    'smoke_and_monoxide_detectors_yes': CHECKBOX_PDF_TYPE,
    'smoke_and_carbon_monoxide_detectors_details': STRING_PDF_TYPE,
    'intercom_system_yes': CHECKBOX_PDF_TYPE,
    'intercom_system_details': STRING_PDF_TYPE,
    'security_system_yes': CHECKBOX_PDF_TYPE,
    'security_system_details': STRING_PDF_TYPE,
    'security_system_rented_yes': CHECKBOX_PDF_TYPE,
    'security_system_owned_yes': CHECKBOX_PDF_TYPE,
    'satellite_dish_yes': CHECKBOX_PDF_TYPE,
    'satellite_dish_details': STRING_PDF_TYPE,
    'attached_tv_yes': CHECKBOX_PDF_TYPE,
    'attached_tv_details': STRING_PDF_TYPE,
    'tv_antenna_yes': CHECKBOX_PDF_TYPE,
    'tv_antenna_details': STRING_PDF_TYPE,
    'multimedia_equipment_yes': CHECKBOX_PDF_TYPE,
    'multimedia_equipment_details': STRING_PDF_TYPE,
    'central_air_conditioner_yes': CHECKBOX_PDF_TYPE,
    'central_air_conditioner_details': STRING_PDF_TYPE,
    'window_air_conditioner_yes': CHECKBOX_PDF_TYPE,
    'window_air_conditioner_details': STRING_PDF_TYPE,
    'electronic_air_filter_yes': CHECKBOX_PDF_TYPE,
    'electronic_air_filter_details': STRING_PDF_TYPE,
    'central_humidifier_yes': CHECKBOX_PDF_TYPE,
    'central_humidifier_details': STRING_PDF_TYPE,
    'lighting_fixtures_yes': CHECKBOX_PDF_TYPE,
    'lighting_fixtures_details': STRING_PDF_TYPE,
    'electronic_garage_door_yes': CHECKBOX_PDF_TYPE,
    'electronic_garage_door_with_remote_unit_details': STRING_PDF_TYPE,
    'tacked_down_carpeting_yes': CHECKBOX_PDF_TYPE,
    'fireplace_screen_and_equipment_yes': CHECKBOX_PDF_TYPE,
    'fireplace_screen_and_equipment_details': STRING_PDF_TYPE,
    'fireplace_gas_log_yes': CHECKBOX_PDF_TYPE,
    'fireplace_gas_log_details': STRING_PDF_TYPE,
    'firewood_yes': CHECKBOX_PDF_TYPE,
    'firewood_details': STRING_PDF_TYPE,
    'attached_gas_grill_yes': CHECKBOX_PDF_TYPE,
    'attached_gas_grill_details': STRING_PDF_TYPE,
    'existing_storms_and_screens_yes': CHECKBOX_PDF_TYPE,
    'existing_storms_and_screens_details': STRING_PDF_TYPE,
    'window_treatments_yes': CHECKBOX_PDF_TYPE,
    'window_treatments_details': STRING_PDF_TYPE,
    'other_equipment_yes': CHECKBOX_PDF_TYPE,
    'other_equipment_details': STRING_PDF_TYPE,
    'built_in_or_attached_shelves_or_cabinets_yes': CHECKBOX_PDF_TYPE,
    'built_int_or_attached_shelves_or_cabinets_details': STRING_PDF_TYPE,
    'ceiling_fan_yes': CHECKBOX_PDF_TYPE,
    'ceiling_fan_details': STRING_PDF_TYPE,
    'radiator_covers_yes': CHECKBOX_PDF_TYPE,
    'radiator_covers_details': STRING_PDF_TYPE,
    'all_planted_vegetation_yes': CHECKBOX_PDF_TYPE,
    'outdoor_play_set_or_swings_yes': CHECKBOX_PDF_TYPE,
    'outdoor_shed_yes': CHECKBOX_PDF_TYPE,
    'purchase_price': STRING_PDF_TYPE,
    'credit_buyer_at_closing_yes': CHECKBOX_PDF_TYPE,
    'credit_buyer_at_closing_if_yes_amount': STRING_PDF_TYPE,
    'credit_buyer_at_closing_no': CHECKBOX_PDF_TYPE,
    'credit_buyer_at_closing_if_no_percentage': STRING_PDF_TYPE,
    'home_warranty_amount': STRING_PDF_TYPE,
    'brokerage_for_earnest_money': STRING_PDF_TYPE,
    'initial_earnest_money_amount': STRING_PDF_TYPE,
    'how_buyer_deposits_earnest_money': STRING_PDF_TYPE,
    'initial_earnest_money_due_date': STRING_PDF_TYPE,
    'balance_of_earnest_money_amount': STRING_PDF_TYPE,
    'balance_of_earnest_money_due_date': STRING_PDF_TYPE,
    'contract_subject_to_mortgage_yes': CHECKBOX_PDF_TYPE,
    'contract_subject_to_mortgage_no': CHECKBOX_PDF_TYPE,
    'mortgage_contingency_date': STRING_PDF_TYPE,
    'buyer_loan_to_value': STRING_PDF_TYPE,
    'buyer_interest_rate': STRING_PDF_TYPE,
    'buyer_loan_term': STRING_PDF_TYPE,
    'closing_date': STRING_PDF_TYPE,
    'homeowner_yes': CHECKBOX_PDF_TYPE,
    'homeowner_no': CHECKBOX_PDF_TYPE,
    'dual_agent_broker_name': STRING_PDF_TYPE,
    'length_of_attorney_review': STRING_PDF_TYPE,
    'length_of_inspection_period': STRING_PDF_TYPE,
    'riders_or_addendums': STRING_PDF_TYPE,
    'offer_deadline': STRING_PDF_TYPE,
    'offer_date': STRING_PDF_TYPE,
    'designated_agent': STRING_PDF_TYPE,
    'agent_mls': STRING_PDF_TYPE,
    'agent_license': STRING_PDF_TYPE,
    'brokerage': STRING_PDF_TYPE,
    'brokerage_mls': STRING_PDF_TYPE,
    'brokerage_license': STRING_PDF_TYPE,
    'broker_address': STRING_PDF_TYPE,
    'agent_phone': STRING_PDF_TYPE,
    'agent_fax': STRING_PDF_TYPE,
    'broker_email': STRING_PDF_TYPE,
    'attorney_name': STRING_PDF_TYPE,
    'attorney_address': STRING_PDF_TYPE,
    'attorney_phone': STRING_PDF_TYPE,
    'attorney_fax': STRING_PDF_TYPE,
    'attorney_email': STRING_PDF_TYPE,
    'lender_name': STRING_PDF_TYPE,
    'lender_company': STRING_PDF_TYPE,
    'lender_address': STRING_PDF_TYPE,
    'lender_phone': STRING_PDF_TYPE,
    'lender_fax': STRING_PDF_TYPE,
    'lender_email': STRING_PDF_TYPE,
    'buyer_name': STRING_PDF_TYPE,
    'seller_name': STRING_PDF_TYPE,
    'special_assessment_yes': CHECKBOX_PDF_TYPE,
    'special_assessment_no': CHECKBOX_PDF_TYPE,
    'deliver_association': STRING_PDF_TYPE,
    'homeowner': CHECKBOX_PDF_TYPE,
    'senior': CHECKBOX_PDF_TYPE,
    'senior_freeze': CHECKBOX_PDF_TYPE,
    'historical': CHECKBOX_PDF_TYPE,
    'prorated': STRING_PDF_TYPE,
    'parking_space_numbers': STRING_PDF_TYPE,
    'deeded': CHECKBOX_PDF_TYPE,
    'assigned': CHECKBOX_PDF_TYPE,
    'indoor': CHECKBOX_PDF_TYPE,
    'outdoor': CHECKBOX_PDF_TYPE,
    'limited_common_element': CHECKBOX_PDF_TYPE,
    'parking_pin': STRING_PDF_TYPE,
})

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}

url_to_scrape = None
page = None
data_dict = dict()


def get_request(url):
    global page, url_to_scrape
    url_to_scrape = str(url)
    # urlToScrape = 'https://www.redfin.com/IL/Chicago/824-W-Armitage-Ave-60614/unit-2A/home/13352313'
    page = requests.get(url=url_to_scrape, headers=HEADERS)


def parse_bs4():
    global page
    hoa_dues = None
    tax = None
    tax_exemptions = None
    tax_year = None
    parcel_identification_number = None
    soup = BeautifulSoup(page.content, 'html.parser')
    street_address_span = soup.find(class_='street-address')
    city_state_zip_span_locality = soup.find(
        class_='citystatezip').find(class_='locality')
    city_state_zip_span_region = soup.find(
        class_='citystatezip').find(class_='region')
    city_state_zip_span_postal_code = soup.find(
        class_='citystatezip').find(class_='postal-code')
    agent_details = soup.find(
        class_='agent-basic-details font-color-gray-dark')
    divs_details = soup.findAll(
        class_='keyDetail font-weight-roman font-size-base')
    for div in divs_details:
        if 'HOA Dues' in div.get_text():
            hoa_dues = div.find(class_='content text-right')

    divs_details = soup.findAll(
        class_='amenity-group')
    for div in divs_details:
        if 'Financial Information' in div.get_text():
            temp = div.find(
                class_='no-break-inside').findAll(class_='entryItemContent')
            tax = temp[0]
            tax_year = temp[1]
            for li in div.findAll(class_='entryItem'):
                if 'Homeowner' in li.get_text():
                    tax_exemptions = li

        if 'Property Information' in div.get_text():
            for span in div.findAll(class_='entryItemContent'):
                if 'Parcel Identification Number' in span.get_text():
                    parcel_identification_number = span

    details_dict = dict()
    details_dict.update({
        'property_street_address': street_address_span.get_text().strip(),
        'property_locality': city_state_zip_span_locality.get_text().strip()[:-1],
        'property_region': city_state_zip_span_region.get_text().strip(),
        'property_postal_code': city_state_zip_span_postal_code.get_text().strip(),
        'agent_details_name': agent_details.get_text().split(sep='•')[0][10:].strip(),
        'agent_details_company': agent_details.get_text().split(sep='•')[1].strip()
    })
    if hoa_dues:
        details_dict.update({
            'hoa_dues': hoa_dues.get_text()[1:].strip()
        })
    if tax:
        details_dict.update({
            'tax': tax.get_text().split(sep='$')[1].strip()
        })
    if tax_year:
        details_dict.update({
            'tax_year': tax_year.get_text().split(sep=':')[1].split(sep='20')[1].strip()
        })
    if tax_exemptions:
        details_dict.update({
            'tax_exemptions': tax_exemptions.get_text().split(sep=':')[1].strip()
        })
    if parcel_identification_number:
        details_dict.update({
            'parcel_identification_number': parcel_identification_number.get_text().split(sep=':')[1].strip()
        })
    return details_dict


def create_data_for_pdf(body_request):
    data_dict.update({
        'property_details': body_request.property_street_address + ' ' + body_request.property_locality
                            + ' ' + body_request.property_region + ' ' + body_request.property_postal_code,
        'parcel_identification_number': body_request.parcel_identification_number,
        'agent_details_name': body_request.agent_details_name,
        'agent_details_company_page_1': body_request.agent_details_company,
        'agent_details_company_page_3': body_request.agent_details_company,
        'hoa_dues': body_request.hoa_dues,
        'tax': body_request.tax,
        'tax_year': body_request.tax_year,
        'tax_exemptions_yes': True if body_request.tax_exemptions is not None else False,
        'tax_exemptions_no': True if body_request.tax_exemptions is None else False,
        'refrigerator_yes': body_request.refrigerator,
        'refrigerator_details': body_request.refrigerator_details,
        'oven_or_range_yes': body_request.oven_or_range,
        'oven_or_range_details': body_request.oven_or_range_details,
        'microware_yes': body_request.microware,
        'microwave_details': body_request.microwave_details,
        'dishwasher_yes': body_request.dishwasher,
        'dishwasher_details': body_request.dishwasher_details,
        'garbage_disposal_yes': body_request.garbage_disposal,
        'garbage_disposal_details': body_request.garbage_disposal_details,
        'trash_compactor_yes': body_request.trash_compactor,
        'trash_compactor_details': body_request.trash_compactor_details,
        'washer_yes': body_request.washer,
        'washer_details': body_request.washer_details,
        'dryer_yes': body_request.dryer,
        'dryer_details': body_request.dryer_details,
        'water_softener_yes': body_request.water_softener,
        'water_softner_details': body_request.water_softner_details,
        'sump_pump_yes': body_request.sump_pump,
        'sump_pump_details': body_request.sump_pump_details,
        'smoke_and_monoxide_detectors_yes': body_request.smoke_and_monoxide_detectors,
        'smoke_and_carbon_monoxide_detectors_details': body_request.smoke_and_carbon_monoxide_detectors_details,
        'intercom_system_yes': body_request.intercom_system,
        'intercom_system_details': body_request.intercom_system_details,
        'security_system_yes': body_request.security_system,
        'security_system_details': body_request.security_system_details,
        'security_system_rented_yes': body_request.security_system_rented,
        'security_system_owned_yes': body_request.security_system_owned,
        'satellite_dish_yes': body_request.satellite_dish,
        'satellite_dish_details': body_request.satellite_dish_details,
        'attached_tv_yes': body_request.attached_tv,
        'attached_tv_details': body_request.attached_tv_details,
        'tv_antenna_yes': body_request.tv_antenna,
        'tv_antenna_details': body_request.tv_antenna_details,
        'multimedia_equipment_yes': body_request.multimedia_equipment,
        'multimedia_equipment_details': body_request.multimedia_equipment_details,
        'central_air_conditioner_yes': body_request.central_air_conditioner,
        'central_air_conditioner_details': body_request.central_air_conditioner_details,
        'window_air_conditioner_yes': body_request.window_air_conditioner,
        'window_air_conditioner_details': body_request.window_air_conditioner_details,
        'electronic_air_filter_yes': body_request.electronic_air_filter,
        'electronic_air_filter_details': body_request.electronic_air_filter_details,
        'central_humidifier_yes': body_request.central_humidifier,
        'central_humidifier_details': body_request.central_humidifier_details,
        'lighting_fixtures_yes': body_request.lighting_fixtures,
        'lighting_fixtures_details': body_request.lighting_fixtures_details,
        'electronic_garage_door_yes': body_request.electronic_garage_door,
        'electronic_garage_door_with_remote_unit_details': body_request.electronic_garage_door_with_remote_unit_details,
        'tacked_down_carpeting_yes': body_request.tacked_down_carpeting,
        'fireplace_screen_and_equipment_yes': body_request.fireplace_screen_and_equipment,
        'fireplace_screen_and_equipment_details': body_request.fireplace_screen_and_equipment_details,
        'fireplace_gas_log_yes': body_request.fireplace_gas_log,
        'fireplace_gas_log_details': body_request.fireplace_gas_log_details,
        'firewood_yes': body_request.firewood,
        'firewood_details': body_request.firewood_details,
        'attached_gas_grill_yes': body_request.attached_gas_grill,
        'attached_gas_grill_details': body_request.attached_gas_grill_details,
        'existing_storms_and_screens_yes': body_request.existing_storms_and_screens,
        'existing_storms_and_screens_details': body_request.existing_storms_and_screens_details,
        'window_treatments_yes': body_request.window_treatments,
        'window_treatments_details': body_request.window_treatments_details,
        'other_equipment_yes': body_request.other_equipment,
        'other_equipment_details': body_request.other_equipment_details,
        'built_in_or_attached_shelves_or_cabinets_yes': body_request.built_in_or_attached_shelves_or_cabinets,
        'built_int_or_attached_shelves_or_cabinets_details':
            body_request.built_int_or_attached_shelves_or_cabinets_details,
        'ceiling_fan_yes': body_request.ceiling_fan,
        'ceiling_fan_details': body_request.ceiling_fan_details,
        'radiator_covers_yes': body_request.radiator_covers,
        'radiator_covers_details': body_request.radiator_covers_details,
        'all_planted_vegetation_yes': body_request.all_planted_vegetation,
        'outdoor_play_set_or_swings_yes': body_request.outdoor_play_set_or_swings,
        'outdoor_shed_yes': body_request.outdoor_shed,
        'purchase_price': body_request.purchase_price,
        'credit_buyer_at_closing_yes': body_request.credit_buyer_at_closing_yes,
        'credit_buyer_at_closing_if_yes_amount': body_request.credit_buyer_at_closing_if_yes_amount,
        'credit_buyer_at_closing_no': body_request.credit_buyer_at_closing_no,
        'credit_buyer_at_closing_if_no_percentage': body_request.credit_buyer_at_closing_if_no_percentage,
        'home_warranty_amount': body_request.home_warranty_amount,
        'brokerage_for_earnest_money': body_request.brokerage_for_earnest_money,
        'initial_earnest_money_amount': body_request.initial_earnest_money_amount,
        'how_buyer_deposits_earnest_money': body_request.how_buyer_deposits_earnest_money,
        'initial_earnest_money_due_date': body_request.initial_earnest_money_due_date,
        'balance_of_earnest_money_amount': body_request.balance_of_earnest_money_amount,
        'balance_of_earnest_money_due_date': body_request.balance_of_earnest_money_due_date,
        'contract_subject_to_mortgage_yes': body_request.contract_subject_to_mortgage_yes,
        'contract_subject_to_mortgage_no': body_request.contract_subject_to_mortgage_no,
        'mortgage_contingency_date': body_request.mortgage_contingency_date,
        'buyer_loan_to_value': body_request.buyer_loan_to_value,
        'buyer_interest_rate': body_request.buyer_interest_rate,
        'buyer_loan_term': body_request.buyer_loan_term,
        'closing_date': body_request.closing_date,
        'disclosures_a_yes': body_request.disclosures_a_yes,
        'disclosures_a_no': body_request.disclosures_a_no,
        'disclosures_b_yes': body_request.disclosures_b_yes,
        'disclosures_b_no': body_request.disclosures_b_no,
        'disclosures_c_yes': body_request.disclosures_c_yes,
        'disclosures_c_no': body_request.disclosures_c_no,
        'disclosures_d_yes': body_request.disclosures_d_yes,
        'disclosures_d_no': body_request.disclosures_d_no,
        'dual_agent_broker_yes': body_request.dual_agent_broker_yes,
        'dual_agent_broker_no': body_request.dual_agent_broker_no,
        'dual_agent_broker_name': body_request.dual_agent_broker_name,
        'length_of_attorney_review': body_request.length_of_attorney_review,
        'length_of_inspection_period': body_request.length_of_inspection_period,
        'offer_date': body_request.offer_date,
        'designated_agent': body_request.designated_agent,
        'agent_mls': body_request.agent_mls,
        'agent_license': body_request.agent_license,
        'brokerage': body_request.brokerage,
        'brokerage_mls': body_request.brokerage_mls,
        'brokerage_license': body_request.brokerage_license,
        'broker_address': body_request.broker_address,
        'agent_phone': body_request.agent_phone,
        'agent_fax': body_request.agent_fax,
        'broker_email': body_request.broker_email,
        'attorney_name': body_request.attorney_name,
        'attorney_address': body_request.attorney_address,
        'attorney_phone': body_request.attorney_phone,
        'attorney_fax': body_request.attorney_fax,
        'attorney_email': body_request.attorney_email,
        'lender_name': body_request.lender_name,
        'lender_company': body_request.lender_company,
        'lender_address': body_request.lender_address,
        'lender_phone': body_request.lender_phone,
        'lender_fax': body_request.lender_fax,
        'lender_email': body_request.lender_email,
        'riders_or_addendums': body_request.riders_or_addendums,
        'offer_deadline': body_request.offer_deadline,
        'homeowner_yes': body_request.homeowner_yes,
        'homeowner_no': body_request.homeowner_no,
        'buyer_name': body_request.buyer_name,
        'buyer_email': body_request.buyer_email,
        'seller_name': body_request.seller_name,
        'seller_email': body_request.seller_email,
        'special_assessment_yes': body_request.special_assessment_yes,
        'special_assessment_no': body_request.special_assessment_no,
        'deliver_association': body_request.deliver_association,
        'homeowner': body_request.homeowner,
        'senior': body_request.senior,
        'senior_freeze': body_request.senior_freeze,
        'historical': body_request.historical,
        'prorated': body_request.prorated,
        'parking_space_numbers': body_request.parking_space_numbers,
        'deeded': body_request.deeded,
        'assigned': body_request.assigned,
        'indoor': body_request.indoor,
        'outdoor': body_request.outdoor,
        'limited_common_element': body_request.limited_common_element,
        'parking_pin': body_request.parking_pin,
    })


def encode_pdf_string(value, type_pdf):
    if type_pdf == STRING_PDF_TYPE:
        if value:
            return pdfrw.objects.pdfstring.PdfString.encode(value.upper())
        else:
            return pdfrw.objects.pdfstring.PdfString.encode('')
    elif type_pdf == CHECKBOX_PDF_TYPE:
        if value == 'True' or value is True:
            return pdfrw.PdfName('Yes')
        else:
            return pdfrw.PdfName('No')
    return ''


def fill_pdf_attached():
    global data_dict, FORM_KEYS_ATTACHED, url_to_scrape
    pdf_template = pdfrw.PdfReader('pdf/services/Contract_Template_Attached.pdf')
    for page_pdf in pdf_template.pages:
        annotations = page_pdf['/Annots']
        if annotations is None:
            continue
        for annotation in annotations:
            if annotation['/Subtype'] == '/Widget':
                if annotation['/T']:
                    key = annotation['/T'][1:-1]
                    if re.search(r'.-[0-9]+', key):
                        key = key[:-2]
                    if key in data_dict:
                        if FORM_KEYS_ATTACHED[key] == CHECKBOX_PDF_TYPE:
                            annotation.update(pdfrw.PdfDict(
                                AS=encode_pdf_string(data_dict[key], CHECKBOX_PDF_TYPE)))
                        else:
                            annotation.update(pdfrw.
                                              PdfDict(V=encode_pdf_string(data_dict[key],
                                                                          STRING_PDF_TYPE)))
                    annotation.update(pdfrw.PdfDict(Ff=1))
    pdf_template.Root.AcroForm.update(pdfrw.PdfDict(
        NeedAppearances=pdfrw.PdfObject('true')))
    pdfrw.PdfWriter().write('files/Contract_Attached_' + url_to_scrape.split(sep='/')[-1] + '.pdf', pdf_template)


def fill_pdf_detached():
    global data_dict, FORM_KEYS_DETACHED, url_to_scrape
    pdf_template = pdfrw.PdfReader('pdf/services/Contract_Template_Detached.pdf')
    for page_pdf in pdf_template.pages:
        annotations = page_pdf['/Annots']
        if annotations is None:
            continue
        for annotation in annotations:
            if annotation['/Subtype'] == '/Widget':
                if annotation['/T']:
                    key = annotation['/T'][1:-1]
                    if re.search(r'.-[0-9]+', key):
                        key = key[:-2]
                    if key in data_dict:
                        if FORM_KEYS_DETACHED[key] == CHECKBOX_PDF_TYPE:
                            annotation.update(pdfrw.PdfDict(
                                AS=encode_pdf_string(data_dict[key], CHECKBOX_PDF_TYPE)))
                        else:
                            annotation.update(pdfrw.
                                              PdfDict(V=encode_pdf_string(data_dict[key],
                                                                          STRING_PDF_TYPE)))
                    annotation.update(pdfrw.PdfDict(Ff=1))
    pdf_template.Root.AcroForm.update(pdfrw.PdfDict(
        NeedAppearances=pdfrw.PdfObject('true')))
    pdfrw.PdfWriter().write('files/Contract_Detached_' + url_to_scrape.split(sep='/')[-1] + '.pdf', pdf_template)


def convert_to_pdf(body_request):
    global url_to_scrape
    url_to_scrape = body_request.url
    create_data_for_pdf(body_request)
    if body_request.property_type == 'attached':
        fill_pdf_attached()
        return 'files/Contract_Attached_' + url_to_scrape.split(sep='/')[-1] + '.pdf'
    elif body_request.property_type == 'detached':
        fill_pdf_detached()
        return 'files/Contract_Detached_' + url_to_scrape.split(sep='/')[-1] + '.pdf'
    else:
        raise InvalidPropertyType()


def scraper_redfin(url):
    get_request(url)
    return parse_bs4()
