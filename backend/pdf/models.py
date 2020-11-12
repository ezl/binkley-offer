from django.db import models
from django.contrib.auth.models import User


class Pdf(models.Model):
    redfin_src = models.TextField()
    pdf_src = models.TextField()
    deleted = models.BooleanField(default=False)
    user_email = models.TextField(default='')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_uid = models.TextField(unique=True)
    password = models.TextField()
    email = models.EmailField(unique=True)
    first_name = models.TextField(default=None, null=True)
    last_name = models.TextField(default=None, null=True)
    agent_mls = models.TextField(default=None, null=True)
    agent_license = models.TextField(default=None, null=True)
    brokerage = models.TextField(default=None, null=True)
    brokerage_mls = models.TextField(default=None, null=True)
    brokerage_license = models.TextField(default=None, null=True)
    agent_phone = models.TextField(default=None, null=True)
    agent_fax = models.TextField(default=None, null=True)
    data_joined = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)


class PersistentUserChoice(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    refrigerator = models.BooleanField(default=False)
    refrigerator_details = models.TextField(null=True, default=None)
    oven_or_range = models.BooleanField(default=False)
    oven_or_range_details = models.TextField(null=True, default=None)
    microware = models.BooleanField(default=False)
    microwave_details = models.TextField(null=True, default=None)
    dishwasher = models.BooleanField(default=False)
    dishwasher_details = models.TextField(null=True, default=None)
    garbage_disposal = models.BooleanField(default=False)
    garbage_disposal_details = models.TextField(null=True, default=None)
    trash_compactor = models.BooleanField(default=False)
    trash_compactor_details = models.TextField(null=True, default=None)
    washer = models.BooleanField(default=False)
    washer_details = models.TextField(null=True, default=None)
    dryer = models.BooleanField(default=False)
    dryer_details = models.TextField(null=True, default=None)
    water_softener = models.BooleanField(default=False)
    water_softner_details = models.TextField(null=True, default=None)
    sump_pump = models.BooleanField(default=False)
    sump_pump_details = models.TextField(null=True, default=None)
    smoke_and_monoxide_detectors = models.BooleanField(default=False)
    smoke_and_carbon_monoxide_detectors_details = models.TextField(null=True, default=None)
    intercom_system = models.BooleanField(default=False)
    intercom_system_details = models.TextField(null=True, default=None)
    security_system = models.BooleanField(default=False)
    security_system_details = models.TextField(null=True, default=None)
    security_system_rented = models.BooleanField(default=False)
    security_system_owned = models.BooleanField(default=False)
    satellite_dish = models.BooleanField(default=False)
    satellite_dish_details = models.TextField(null=True, default=None)
    attached_tv = models.BooleanField(default=False)
    attached_tv_details = models.TextField(null=True, default=None)
    tv_antenna = models.BooleanField(default=False)
    tv_antenna_details = models.TextField(null=True, default=None)
    multimedia_equipment = models.BooleanField(default=False)
    multimedia_equipment_details = models.TextField(null=True, default=None)
    central_air_conditioner = models.BooleanField(default=False)
    central_air_conditioner_details = models.TextField(null=True, default=None)
    window_air_conditioner = models.BooleanField(default=False)
    window_air_conditioner_details = models.TextField(null=True, default=None)
    electronic_air_filter = models.BooleanField(default=False)
    electronic_air_filter_details = models.TextField(null=True, default=None)
    central_humidifier = models.BooleanField(default=False)
    central_humidifier_details = models.TextField(null=True, default=None)
    lighting_fixtures = models.BooleanField(default=False)
    lighting_fixtures_details = models.TextField(null=True, default=None)
    electronic_garage_door = models.BooleanField(default=False)
    electronic_garage_door_with_remote_unit_details = models.TextField(null=True, default=None)
    tacked_down_carpeting = models.BooleanField(default=False)
    fireplace_screen_and_equipment = models.BooleanField(default=False)
    fireplace_screen_and_equipment_details = models.TextField(null=True, default=None)
    fireplace_gas_log = models.BooleanField(default=False)
    fireplace_gas_log_details = models.TextField(null=True, default=None)
    firewood = models.BooleanField(default=False)
    firewood_details = models.TextField(null=True, default=None)
    attached_gas_grill = models.BooleanField(default=False)
    attached_gas_grill_details = models.TextField(null=True, default=None)
    existing_storms_and_screens = models.BooleanField(default=False)
    existing_storms_and_screens_details = models.TextField(null=True, default=None)
    window_treatments = models.BooleanField(default=False)
    window_treatments_details = models.TextField(null=True, default=None)
    other_equipment = models.BooleanField(default=False)
    other_equipment_details = models.TextField(null=True, default=None)
    built_in_or_attached_shelves_or_cabinets = models.BooleanField(default=False)
    built_int_or_attached_shelves_or_cabinets_details = models.TextField(null=True, default=None)
    ceiling_fan = models.BooleanField(default=False)
    ceiling_fan_details = models.TextField(null=True, default=None)
    radiator_covers = models.BooleanField(default=False)
    radiator_covers_details = models.TextField(null=True, default=None)
    all_planted_vegetation = models.BooleanField(default=False)
    outdoor_play_set_or_swings = models.BooleanField(default=False)
    outdoor_shed = models.BooleanField(default=False)
    purchase_price = models.TextField(null=True, default=None)
    credit_buyer_at_closing_yes = models.BooleanField(default=False)
    credit_buyer_at_closing_if_yes_amount = models.TextField(null=True, default=None)
    credit_buyer_at_closing_no = models.BooleanField(default=False)
    credit_buyer_at_closing_if_no_percentage = models.TextField(null=True, default=None)
    home_warranty_amount = models.TextField(null=True, default=None)
    brokerage_for_earnest_money = models.TextField(null=True, default=None)
    initial_earnest_money_amount = models.TextField(null=True, default=None)
    how_buyer_deposits_earnest_money = models.TextField(null=True, default=None)
    initial_earnest_money_due_date = models.TextField(null=True, default=None)
    balance_of_earnest_money_amount = models.TextField(null=True, default=None)
    balance_of_earnest_money_due_date = models.TextField(null=True, default=None)
    contract_subject_to_mortgage_yes = models.BooleanField(default=False)
    contract_subject_to_mortgage_no = models.BooleanField(default=False)
    mortgage_contingency_date = models.TextField(null=True, default=None)
    buyer_loan_to_value = models.TextField(null=True, default=None)
    buyer_interest_rate = models.TextField(null=True, default=None)
    buyer_loan_term = models.TextField(null=True, default=None)
    closing_date = models.TextField(null=True, default=None)
    disclosures_a_yes = models.BooleanField(default=False)
    disclosures_a_no = models.BooleanField(default=False)
    disclosures_b_yes = models.BooleanField(default=False)
    disclosures_b_no = models.BooleanField(default=False)
    disclosures_c_yes = models.BooleanField(default=False)
    disclosures_c_no = models.BooleanField(default=False)
    disclosures_d_yes = models.BooleanField(default=False)
    disclosures_d_no = models.BooleanField(default=False)
    dual_agent_broker_name = models.TextField(null=True, default=None)
    length_of_attorney_review = models.TextField(null=True, default=None)
    length_of_inspection_period = models.TextField(null=True, default=None)
    offer_date = models.TextField(null=True, default=None)
    designated_agent = models.TextField(null=True, default=None)
    agent_mls = models.TextField(null=True, default=None)
    agent_license = models.TextField(null=True, default=None)
    brokerage = models.TextField(null=True, default=None)
    brokerage_mls = models.TextField(null=True, default=None)
    brokerage_license = models.TextField(null=True, default=None)
    broker_address = models.TextField(null=True, default=None)
    agent_phone = models.TextField(null=True, default=None)
    agent_fax = models.TextField(null=True, default=None)
    broker_email = models.TextField(null=True, default=None)
    attorney_name = models.TextField(null=True, default=None)
    attorney_address = models.TextField(null=True, default=None)
    attorney_phone = models.TextField(null=True, default=None)
    attorney_fax = models.TextField(null=True, default=None)
    attorney_email = models.TextField(null=True, default=None)
    lender_name = models.TextField(null=True, default=None)
    lender_company = models.TextField(null=True, default=None)
    lender_address = models.TextField(null=True, default=None)
    lender_phone = models.TextField(null=True, default=None)
    lender_fax = models.TextField(null=True, default=None)
    lender_email = models.TextField(null=True, default=None)
