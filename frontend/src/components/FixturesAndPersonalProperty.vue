<template>
  <div>
    <H1>Fixtures And Personal Property</H1>
    <b-progress-bar :value="2" :max="5" :label="'Progress: 2/5'" show-progress animated></b-progress-bar>
    <b-row align-v="baseline">
      <b-col sm="3">
        <div>
          <p>Refrigerator</p>
          <CheckboxInput v-model="pdfBody.refrigerator"></CheckboxInput>
          <TextInput v-if="pdfBody.refrigerator" v-model="pdfBody.refrigerator_details"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Oven or Range</p>
          <CheckboxInput v-model="pdfBody.oven_or_range"></CheckboxInput>
          <TextInput v-if="pdfBody.oven_or_range" v-model="pdfBody.oven_or_range_details"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Microwave</p>
          <CheckboxInput v-model="pdfBody.microware"></CheckboxInput>
          <TextInput v-if="pdfBody.microware" v-model="pdfBody.microwave_details"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Dishwasher</p>
          <CheckboxInput v-model="pdfBody.dishwasher"></CheckboxInput>
          <TextInput v-if="pdfBody.dishwasher" v-model="pdfBody.dishwasher_details"></TextInput>
        </div>
      </b-col>
    </b-row>

    <b-row align-v="baseline">
      <b-col sm="3">
        <div>
          <p>Garbage Disposal</p>
          <CheckboxInput v-model="pdfBody.garbage_disposal"></CheckboxInput>
          <TextInput v-if="pdfBody.garbage_disposal" v-model="pdfBody.garbage_disposal_details"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Trash_Compactor</p>
          <CheckboxInput v-model="pdfBody.trash_compactor"></CheckboxInput>
          <TextInput v-if="pdfBody.trash_compactor" v-model="pdfBody.trash_compactor_details"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Washer</p>
          <CheckboxInput v-model="pdfBody.washer"></CheckboxInput>
          <TextInput v-if="pdfBody.washer" v-model="pdfBody.washer_details"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Dryer</p>
          <CheckboxInput v-model="pdfBody.dryer"></CheckboxInput>
          <TextInput v-if="pdfBody.dryer" v-model="pdfBody.dryer_details"></TextInput>
        </div>
      </b-col>
    </b-row>

    <b-row align-v="baseline">
      <b-col sm="3">
        <div>
          <p>Water Softener</p>
          <CheckboxInput v-model="pdfBody.water_softener"></CheckboxInput>
          <TextInput v-if="pdfBody.water_softener" v-model="pdfBody.water_softner_details"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Sump Pump</p>
          <CheckboxInput v-model="pdfBody.sump_pump"></CheckboxInput>
          <TextInput v-if="pdfBody.sump_pump" v-model="pdfBody.sump_pump_details"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Smoke And Monoxide Detectors</p>
          <CheckboxInput v-model="pdfBody.smoke_and_monoxide_detectors"></CheckboxInput>
          <TextInput v-if="pdfBody.smoke_and_monoxide_detectors"
                     v-model="pdfBody.smoke_and_carbon_monoxide_detectors_details"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Intercom System</p>
          <CheckboxInput v-model="pdfBody.intercom_system"></CheckboxInput>
          <TextInput v-if="pdfBody.intercom_system" v-model="pdfBody.intercom_system_details"></TextInput>
        </div>
      </b-col>
    </b-row>

    <b-row align-v="baseline">
      <b-col sm="3">
        <div>
          <p>Security System</p>
          <CheckboxInput v-model="pdfBody.security_system"></CheckboxInput>
          <TextInput v-if="pdfBody.security_system" v-model="pdfBody.security_system_details"></TextInput>
          <b-row align-v="baseline">
            <b-col>
              <div v-if="pdfBody.security_system">
                <p>Security System Rented</p>
                <CheckboxInput v-model="pdfBody.security_system_rented"></CheckboxInput>
              </div>
            </b-col>
            <b-col>
              <div v-if="pdfBody.security_system">
                <p>Security System Rented</p>
                <CheckboxInput v-model="pdfBody.security_system_owned"></CheckboxInput>
              </div>
            </b-col>
          </b-row>

        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Satellite Dish</p>
          <CheckboxInput v-model="pdfBody.satellite_dish"></CheckboxInput>
          <TextInput v-if="pdfBody.satellite_dish" v-model="pdfBody.satellite_dish_details"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Attached Tv</p>
          <CheckboxInput v-model="pdfBody.attached_tv"></CheckboxInput>
          <TextInput v-if="pdfBody.attached_tv" v-model="pdfBody.attached_tv_details"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Tv Antenna</p>
          <CheckboxInput v-model="pdfBody.tv_antenna"></CheckboxInput>
          <TextInput v-if="pdfBody.tv_antenna" v-model="pdfBody.tv_antenna_details"></TextInput>
        </div>
      </b-col>
    </b-row>

    <b-row align-v="baseline">
      <b-col sm="3">
        <div>
          <p>Multimedia Equipment</p>
          <CheckboxInput v-model="pdfBody.multimedia_equipment"></CheckboxInput>
          <TextInput v-if="pdfBody.multimedia_equipment" v-model="pdfBody.multimedia_equipment_details"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Central Air Conditioner</p>
          <CheckboxInput v-model="pdfBody.central_air_conditioner"></CheckboxInput>
          <TextInput v-if="pdfBody.central_air_conditioner"
                     v-model="pdfBody.central_air_conditioner_details"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Window Air Conditioner</p>
          <CheckboxInput v-model="pdfBody.window_air_conditioner"></CheckboxInput>
          <TextInput v-if="pdfBody.window_air_conditioner" v-model="pdfBody.window_air_conditioner_details"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Electronic Air Filter</p>
          <CheckboxInput v-model="pdfBody.electronic_air_filter"></CheckboxInput>
          <TextInput v-if="pdfBody.electronic_air_filter" v-model="pdfBody.electronic_air_filter_details"></TextInput>
        </div>
      </b-col>
    </b-row>

    <b-row align-v="baseline">
      <b-col sm="3">
        <div>
          <p>Central Humidifier</p>
          <CheckboxInput v-model="pdfBody.central_humidifier"></CheckboxInput>
          <TextInput v-if="pdfBody.central_humidifier" v-model="pdfBody.central_humidifier_details"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Lighting Fixtures</p>
          <CheckboxInput v-model="pdfBody.lighting_fixtures"></CheckboxInput>
          <TextInput v-if="pdfBody.lighting_fixtures" v-model="pdfBody.lighting_fixtures_details"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Electronic Garage Door</p>
          <CheckboxInput v-model="pdfBody.electronic_garage_door"></CheckboxInput>
          <TextInput v-if="pdfBody.electronic_garage_door"
                     v-model="pdfBody.electronic_garage_door_with_remote_unit_details"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Tacked Down Carpeting</p>
          <CheckboxInput v-model="pdfBody.tacked_down_carpeting"></CheckboxInput>
        </div>
      </b-col>
    </b-row>

    <b-row align-v="baseline">
      <b-col sm="3">
        <div>
          <p>Fireplace Screen And Equipment</p>
          <CheckboxInput v-model="pdfBody.fireplace_screen_and_equipment"></CheckboxInput>
          <TextInput v-if="pdfBody.fireplace_screen_and_equipment"
                     v-model="pdfBody.fireplace_screen_and_equipment_details"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Fireplace Gas Log</p>
          <CheckboxInput v-model="pdfBody.fireplace_gas_log"></CheckboxInput>
          <TextInput v-if="pdfBody.fireplace_gas_log" v-model="pdfBody.fireplace_gas_log_details"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Firewood</p>
          <CheckboxInput v-model="pdfBody.firewood"></CheckboxInput>
          <TextInput v-if="pdfBody.firewood" v-model="pdfBody.firewood_details"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Attached Gas Grill</p>
          <CheckboxInput v-model="pdfBody.attached_gas_grill"></CheckboxInput>
          <TextInput v-if="pdfBody.attached_gas_grill" v-model="pdfBody.attached_gas_grill_details"></TextInput>
        </div>
      </b-col>
    </b-row>

    <b-row align-v="baseline">
      <b-col sm="3">
        <div>
          <p>Existing Storms And Screens</p>
          <CheckboxInput v-model="pdfBody.existing_storms_and_screens"></CheckboxInput>
          <TextInput v-if="pdfBody.existing_storms_and_screens"
                     v-model="pdfBody.existing_storms_and_screens_details"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Window Treatments</p>
          <CheckboxInput v-model="pdfBody.window_treatments"></CheckboxInput>
          <TextInput v-if="pdfBody.window_treatments" v-model="pdfBody.window_treatments_details"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Other Equipment</p>
          <CheckboxInput v-model="pdfBody.other_equipment"></CheckboxInput>
          <TextInput v-if="pdfBody.other_equipment" v-model="pdfBody.other_equipment_details"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Built-in or Attached Shelves or Cabinets</p>
          <CheckboxInput v-model="pdfBody.built_in_or_attached_shelves_or_cabinets"></CheckboxInput>
          <TextInput v-if="pdfBody.built_in_or_attached_shelves_or_cabinets"
                     v-model="pdfBody.built_int_or_attached_shelves_or_cabinets_details"></TextInput>
        </div>
      </b-col>
    </b-row>

    <b-row align-v="baseline">
      <b-col sm>
        <div>
          <p>Ceiling Fan</p>
          <CheckboxInput v-model="pdfBody.ceiling_fan"></CheckboxInput>
          <TextInput v-if="pdfBody.ceiling_fan" v-model="pdfBody.ceiling_fan_details"></TextInput>
        </div>
      </b-col>
      <b-col sm>
        <div>
          <p>Radiator Covers</p>
          <CheckboxInput v-model="pdfBody.radiator_covers"></CheckboxInput>
          <TextInput v-if="pdfBody.radiator_covers" v-model="pdfBody.radiator_covers_details"></TextInput>
        </div>
      </b-col>
      <b-col sm>
        <div>
          <p>All Planted Vegetation</p>
          <CheckboxInput v-model="pdfBody.all_planted_vegetation"></CheckboxInput>
        </div>
      </b-col>
      <b-col sm>
        <div>
          <p>Outdoor Play Set or Swings</p>
          <CheckboxInput v-model="pdfBody.outdoor_play_set_or_swings"></CheckboxInput>
        </div>
      </b-col>
      <b-col sm>
        <div>
          <p>Outdoor Shed</p>
          <CheckboxInput v-model="pdfBody.outdoor_shed"></CheckboxInput>
        </div>
      </b-col>
    </b-row>
    <div>
      <b-button variant="primary" @click="nextPage"> Next Page</b-button>
    </div>
  </div>
</template>

<script>

import PdfBody from '../models/PdfBody'
import CheckboxInput from './CheckboxInput'
import TextInput from './TextInput'

export default {
  name: 'FixturesAndPersonalProperty',
  components: {CheckboxInput, TextInput},
  data () {
    return {
      pdfBody: new PdfBody()
    }
  },
  mounted () {
    if (localStorage.pdfBody) {
      this.pdfBody = Object.assign(new PdfBody(), JSON.parse(localStorage.pdfBody))
    }
  },
  methods: {
    nextPage () {
      localStorage.pdfBody = JSON.stringify(this.pdfBody)
      this.$router.push({name: 'OfferDetails'})
    }
  }
}
</script>

<style scoped>

</style>
