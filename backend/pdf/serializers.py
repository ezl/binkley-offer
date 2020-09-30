from types import SimpleNamespace

from rest_framework import serializers

from .models import Pdf
from .services import pdf_service


class SearchSerializer(serializers.Serializer):
    url = serializers.CharField()


class RedfinScrapperSerializer(serializers.Serializer):
    url = serializers.URLField()


class GetPdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdf
        fields = [
            'id',
            'redfin_src',
            'pdf_src',
            'deleted'
        ]


class CreatePdfSerializer(serializers.Serializer):
    url = serializers.URLField()
    property_street_address = serializers.CharField(required=True)
    property_locality = serializers.CharField(required=True)
    property_region = serializers.CharField(required=True)
    property_postal_code = serializers.CharField(required=True)
    agent_details_name = serializers.CharField(required=True)
    agent_details_company = serializers.CharField(required=True)
    hoa_dues = serializers.CharField(required=True)
    tax = serializers.CharField(required=True)
    tax_year = serializers.CharField(required=True)
    tax_exemptions = serializers.CharField(allow_null=True, required=True)
    parcel_identification_number = serializers.CharField(required=True)
    refrigerator = serializers.BooleanField(default=False)
    refrigerator_details = serializers.CharField(allow_null=True, default="")
    oven_or_range = serializers.BooleanField(default=False)
    oven_or_range_details = serializers.CharField(allow_null=True, default="")
    microware = serializers.BooleanField(default=False)
    microwave_details = serializers.CharField(allow_null=True, default="")
    dishwasher = serializers.BooleanField(default=False)
    dishwasher_details = serializers.CharField(allow_null=True, default="")
    garbage_disposal = serializers.BooleanField(default=False)
    garbage_disposal_details = serializers.CharField(allow_null=True, default="")
    trash_compactor = serializers.BooleanField(default=False)
    trash_compactor_details = serializers.CharField(allow_null=True, default="")
    washer = serializers.BooleanField(default=False)
    washer_details = serializers.CharField(allow_null=True, default="")
    dryer = serializers.BooleanField(default=False)
    dryer_details = serializers.CharField(allow_null=True, default="")
    water_softener = serializers.BooleanField(default=False)
    water_softner_details = serializers.CharField(allow_null=True, default="")
    sump_pump = serializers.BooleanField(default=False)
    sump_pump_details = serializers.CharField(allow_null=True, default="")
    smoke_and_monoxide_detectors = serializers.BooleanField(default=False)
    smoke_and_carbon_monoxide_detectors_details = serializers.CharField(allow_null=True, default="")
    intercom_system = serializers.BooleanField(default=False)
    intercom_system_details = serializers.CharField(allow_null=True, default="")
    security_system = serializers.BooleanField(default=False)
    security_system_details = serializers.CharField(allow_null=True, default="")
    security_system_rented = serializers.BooleanField(default=False)
    security_system_owned = serializers.BooleanField(default=False)
    satellite_dish = serializers.BooleanField(default=False)
    satellite_dish_details = serializers.CharField(allow_null=True, default="")
    attached_tv = serializers.BooleanField(default=False)
    attached_tv_details = serializers.CharField(allow_null=True, default="")
    tv_antenna = serializers.BooleanField(default=False)
    tv_antenna_details = serializers.CharField(allow_null=True, default="")
    multimedia_equipment = serializers.BooleanField(default=False)
    multimedia_equipment_details = serializers.CharField(allow_null=True, default="")
    central_air_conditioner = serializers.BooleanField(default=False)
    central_air_conditioner_details = serializers.CharField(allow_null=True, default="")
    window_air_conditioner = serializers.BooleanField(default=False)
    window_air_conditioner_details = serializers.CharField(allow_null=True, default="")
    electronic_air_filter = serializers.BooleanField(default=False)
    electronic_air_filter_details = serializers.CharField(allow_null=True, default="")
    central_humidifier = serializers.BooleanField(default=False)
    central_humidifier_details = serializers.CharField(allow_null=True, default="")
    lighting_fixtures = serializers.BooleanField(default=False)
    lighting_fixtures_details = serializers.CharField(allow_null=True, default="")
    electronic_garage_door = serializers.BooleanField(default=False)
    electronic_garage_door_with_remote_unit_details = serializers.CharField(allow_null=True, default="")
    tacked_down_carpeting = serializers.BooleanField(default=False)
    fireplace_screen_and_equipment = serializers.BooleanField(default=False)
    fireplace_screen_and_equipment_details = serializers.CharField(allow_null=True, default="")
    fireplace_gas_log = serializers.BooleanField(default=False)
    fireplace_gas_log_details = serializers.CharField(allow_null=True, default="")
    firewood = serializers.BooleanField(default=False)
    firewood_details = serializers.CharField(allow_null=True, default="")
    attached_gas_grill = serializers.BooleanField(default=False)
    attached_gas_grill_details = serializers.CharField(allow_null=True, default="")
    existing_storms_and_screens = serializers.BooleanField(default=False)
    existing_storms_and_screens_details = serializers.CharField(allow_null=True, default="")
    window_treatments = serializers.BooleanField(default=False)
    window_treatments_details = serializers.CharField(allow_null=True, default="")
    other_equipment = serializers.BooleanField(default=False)
    other_equipment_details = serializers.CharField(allow_null=True, default="")
    built_in_or_attached_shelves_or_cabinets = serializers.BooleanField(default=False)
    built_int_or_attached_shelves_or_cabinets_details = serializers.CharField(allow_null=True, default="")
    ceiling_fan = serializers.BooleanField(default=False)
    ceiling_fan_details = serializers.CharField(allow_null=True, default="")
    radiator_covers = serializers.BooleanField(default=False)
    radiator_covers_details = serializers.CharField(allow_null=True, default="")
    all_planted_vegetation = serializers.BooleanField(default=False)
    outdoor_play_set_or_swings = serializers.BooleanField(default=False)
    outdoor_shed = serializers.BooleanField(default=False)
    purchase_price = serializers.CharField(allow_null=True, default="")
    credit_buyer_at_closing_yes = serializers.BooleanField(default=False)
    credit_buyer_at_closing_if_yes_amount = serializers.CharField(allow_null=True, default="")
    credit_buyer_at_closing_no = serializers.BooleanField(default=False)
    credit_buyer_at_closing_if_no_percentage = serializers.CharField(allow_null=True, default="")
    home_warranty_amount = serializers.CharField(allow_null=True, default="")
    brokerage_for_earnest_money = serializers.CharField(allow_null=True, default="")
    initial_earnest_money_amount = serializers.CharField(allow_null=True, default="")
    how_buyer_deposits_earnest_money = serializers.CharField(allow_null=True, default="")
    initial_earnest_money_due_date = serializers.CharField(allow_null=True, default="")
    balance_of_earnest_money_amount = serializers.CharField(allow_null=True, default="")
    balance_of_earnest_money_due_date = serializers.CharField(allow_null=True, default="")
    contract_subject_to_mortgage_yes = serializers.BooleanField(default=False)
    contract_subject_to_mortgage_no = serializers.BooleanField(default=False)
    mortgage_contingency_date = serializers.CharField(allow_null=True, default="")
    buyer_loan_to_value = serializers.CharField(allow_null=True, default="")
    buyer_interest_rate = serializers.CharField(allow_null=True, default="")
    buyer_loan_term = serializers.CharField(allow_null=True, default="")
    closing_date = serializers.CharField(allow_null=True, default="")
    disclosures_a_yes = serializers.BooleanField(default=False)
    disclosures_a_no = serializers.BooleanField(default=False)
    disclosures_b_yes = serializers.BooleanField(default=False)
    disclosures_b_no = serializers.BooleanField(default=False)
    disclosures_c_yes = serializers.BooleanField(default=False)
    disclosures_c_no = serializers.BooleanField(default=False)
    disclosures_d_yes = serializers.BooleanField(default=False)
    disclosures_d_no = serializers.BooleanField(default=False)
    dual_agent_broker_name = serializers.CharField(allow_null=True, default="")
    length_of_attorney_review = serializers.CharField(allow_null=True, default="")
    length_of_inspection_period = serializers.CharField(allow_null=True, default="")
    offer_date = serializers.CharField(allow_null=True, default="")
    designated_agent = serializers.CharField(allow_null=True, default="")
    agent_mls = serializers.CharField(allow_null=True, default="")
    agent_license = serializers.CharField(allow_null=True, default="")
    brokerage = serializers.CharField(allow_null=True, default="")
    brokerage_mls = serializers.CharField(allow_null=True, default="")
    brokerage_license = serializers.CharField(allow_null=True, default="")
    broker_address = serializers.CharField(allow_null=True, default="")
    agent_phone = serializers.CharField(allow_null=True, default="")
    agent_fax = serializers.CharField(allow_null=True, default="")
    broker_email = serializers.CharField(allow_null=True, default="")
    attorney_name = serializers.CharField(allow_null=True, default="")
    attorney_address = serializers.CharField(allow_null=True, default="")
    attorney_phone = serializers.CharField(allow_null=True, default="")
    attorney_fax = serializers.CharField(allow_null=True, default="")
    attorney_email = serializers.CharField(allow_null=True, default="")
    lender_name = serializers.CharField(allow_null=True, default="")
    lender_company = serializers.CharField(allow_null=True, default="")
    lender_address = serializers.CharField(allow_null=True, default="")
    lender_phone = serializers.CharField(allow_null=True, default="")
    lender_fax = serializers.CharField(allow_null=True, default="")
    lender_email = serializers.CharField(allow_null=True, default="")

    def create(self, validated_data):
        # Turns a dictionary into an object so that keys can be accessed with the . operator
        validated_data = SimpleNamespace(**validated_data)

        pdf_from_database = Pdf.objects.filter(redfin_src=validated_data.url).first()

        if pdf_from_database:
            return pdf_from_database

        pdf_src = pdf_service.convert_to_pdf(validated_data)

        return Pdf.objects.create(redfin_src=validated_data.url, pdf_src=pdf_src)
