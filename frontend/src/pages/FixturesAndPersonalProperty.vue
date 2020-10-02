<template>
  <div>
    <b-container v-if="isLoaded" :fluid="true">
      <b-row>
        <b-col>
          <H1>Fixtures And Personal Property</H1>
          <b-progress-bar :value="3" :max="6" :label="'Progress: 3/7'" show-progress animated></b-progress-bar>
        </b-col>
      </b-row>
      <b-row align-v="baseline">
        <b-col md="2"/>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.refrigerator" text-label='Refrigerator'></CheckboxInput>
            <TextInput v-if="pdfBody.refrigerator" v-model="pdfBody.refrigerator_details"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.oven_or_range" text-label="Oven or Range"></CheckboxInput>
            <TextInput v-if="pdfBody.oven_or_range" v-model="pdfBody.oven_or_range_details"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.microware" text-label="Microwave"></CheckboxInput>
            <TextInput v-if="pdfBody.microware" v-model="pdfBody.microwave_details"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.dishwasher" text-label="Dishwasher"></CheckboxInput>
            <TextInput v-if="pdfBody.dishwasher" v-model="pdfBody.dishwasher_details"></TextInput>
          </div>
        </b-col>
        <b-col md="2"/>
      </b-row>

      <b-row align-v="baseline">
        <b-col md="2"/>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.garbage_disposal" text-label="Garbage Disposal"></CheckboxInput>
            <TextInput v-if="pdfBody.garbage_disposal" v-model="pdfBody.garbage_disposal_details"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.trash_compactor" text-label="Trash Compactor"></CheckboxInput>
            <TextInput v-if="pdfBody.trash_compactor" v-model="pdfBody.trash_compactor_details"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.washer" text-label="Washer"></CheckboxInput>
            <TextInput v-if="pdfBody.washer" v-model="pdfBody.washer_details"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.dryer" text-label="Dryer"></CheckboxInput>
            <TextInput v-if="pdfBody.dryer" v-model="pdfBody.dryer_details"></TextInput>
          </div>
        </b-col>
        <b-col md="2"/>
      </b-row>

      <b-row align-v="baseline">
        <b-col md="2"/>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.water_softener" text-label="Water Softener"></CheckboxInput>
            <TextInput v-if="pdfBody.water_softener" v-model="pdfBody.water_softner_details"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.sump_pump" text-label="Sump Pump"></CheckboxInput>
            <TextInput v-if="pdfBody.sump_pump" v-model="pdfBody.sump_pump_details"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.smoke_and_monoxide_detectors"
                           text-label="Smoke And Monoxide Detectors"></CheckboxInput>
            <TextInput v-if="pdfBody.smoke_and_monoxide_detectors"
                       v-model="pdfBody.smoke_and_carbon_monoxide_detectors_details"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.intercom_system" text-label="Intercom System"></CheckboxInput>
            <TextInput v-if="pdfBody.intercom_system" v-model="pdfBody.intercom_system_details"></TextInput>
          </div>
        </b-col>
        <b-col md="2"/>
      </b-row>

      <b-row align-v="baseline">
        <b-col md="2"/>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.security_system" text-label="Security System"></CheckboxInput>
            <TextInput v-if="pdfBody.security_system" v-model="pdfBody.security_system_details"></TextInput>
            <b-row align-v="baseline">
              <RadioInputTwoOptions v-if="pdfBody.security_system" :item="securitySystemRadioItem"
                                    item-one-label="Security System Rented"
                                    item-two-label="Security System Owned"></RadioInputTwoOptions>
            </b-row>

          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.satellite_dish" text-label="Satellite Dish"></CheckboxInput>
            <TextInput v-if="pdfBody.satellite_dish" v-model="pdfBody.satellite_dish_details"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.attached_tv" text-label="Attached Tv"></CheckboxInput>
            <TextInput v-if="pdfBody.attached_tv" v-model="pdfBody.attached_tv_details"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.tv_antenna" text-label="Tv Antenna"></CheckboxInput>
            <TextInput v-if="pdfBody.tv_antenna" v-model="pdfBody.tv_antenna_details"></TextInput>
          </div>
        </b-col>
        <b-col md="2"/>
      </b-row>

      <b-row align-v="baseline">
        <b-col md="2"/>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.multimedia_equipment" text-label="Multimedia Equipment"></CheckboxInput>
            <TextInput v-if="pdfBody.multimedia_equipment" v-model="pdfBody.multimedia_equipment_details"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.central_air_conditioner"
                           text-label="Central Air Conditioner"></CheckboxInput>
            <TextInput v-if="pdfBody.central_air_conditioner"
                       v-model="pdfBody.central_air_conditioner_details"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.window_air_conditioner" text-label="Window Air Conditioner"></CheckboxInput>
            <TextInput v-if="pdfBody.window_air_conditioner"
                       v-model="pdfBody.window_air_conditioner_details"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.electronic_air_filter" text-label="Electronic Air Filter"></CheckboxInput>
            <TextInput v-if="pdfBody.electronic_air_filter" v-model="pdfBody.electronic_air_filter_details"></TextInput>
          </div>
        </b-col>
        <b-col md="2"/>
      </b-row>

      <b-row align-v="baseline">
        <b-col md="2"/>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.central_humidifier" text-label="Central Humidifier"></CheckboxInput>
            <TextInput v-if="pdfBody.central_humidifier" v-model="pdfBody.central_humidifier_details"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.lighting_fixtures" text-label="Lighting Fixtures"></CheckboxInput>
            <TextInput v-if="pdfBody.lighting_fixtures" v-model="pdfBody.lighting_fixtures_details"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.electronic_garage_door" text-label="Electronic Garage Door"></CheckboxInput>
            <TextInput v-if="pdfBody.electronic_garage_door"
                       v-model="pdfBody.electronic_garage_door_with_remote_unit_details"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.tacked_down_carpeting" text-label="Tacked Down Carpeting"></CheckboxInput>
          </div>
        </b-col>
        <b-col md="2"/>
      </b-row>

      <b-row align-v="baseline">
        <b-col md="2"/>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.fireplace_screen_and_equipment"
                           text-label="Fireplace Screen And Equipment"></CheckboxInput>
            <TextInput v-if="pdfBody.fireplace_screen_and_equipment"
                       v-model="pdfBody.fireplace_screen_and_equipment_details"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.fireplace_gas_log" text-label="Fireplace Gas Log"></CheckboxInput>
            <TextInput v-if="pdfBody.fireplace_gas_log" v-model="pdfBody.fireplace_gas_log_details"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.firewood" text-label="Firewood"></CheckboxInput>
            <TextInput v-if="pdfBody.firewood" v-model="pdfBody.firewood_details"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <!--          <p>Attached Gas Grill</p>-->
            <CheckboxInput v-model="pdfBody.attached_gas_grill" text-label="Attached Gas Grill"></CheckboxInput>
            <TextInput v-if="pdfBody.attached_gas_grill" v-model="pdfBody.attached_gas_grill_details"></TextInput>
          </div>
        </b-col>
        <b-col md="2"/>
      </b-row>

      <b-row align-v="baseline">
        <b-col md="2"/>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.existing_storms_and_screens"
                           text-label="Attached Gas Grill"></CheckboxInput>
            <TextInput v-if="pdfBody.existing_storms_and_screens"
                       v-model="pdfBody.existing_storms_and_screens_details"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.window_treatments" text-label="Window Treatments"></CheckboxInput>
            <TextInput v-if="pdfBody.window_treatments" v-model="pdfBody.window_treatments_details"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.other_equipment" text-label="Other Equipment"></CheckboxInput>
            <TextInput v-if="pdfBody.other_equipment" v-model="pdfBody.other_equipment_details"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.built_in_or_attached_shelves_or_cabinets"
                           text-label="Built-in or Attached Shelves or Cabinets"></CheckboxInput>
            <TextInput v-if="pdfBody.built_in_or_attached_shelves_or_cabinets"
                       v-model="pdfBody.built_int_or_attached_shelves_or_cabinets_details"></TextInput>
          </div>
        </b-col>
        <b-col md="2"/>
      </b-row>

      <b-row align-v="baseline">
        <b-col md="2"/>
        <b-col cols="6" sm="3" md="2">
          <div>
            <!--          <p>Ceiling Fan</p>-->
            <CheckboxInput v-model="pdfBody.ceiling_fan" text-label="Ceiling Fan"></CheckboxInput>
            <TextInput v-if="pdfBody.ceiling_fan" v-model="pdfBody.ceiling_fan_details"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.radiator_covers" text-label="Radiator Covers"></CheckboxInput>
            <TextInput v-if="pdfBody.radiator_covers" v-model="pdfBody.radiator_covers_details"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.all_planted_vegetation" text-label="All Planted Vegetation"></CheckboxInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.outdoor_play_set_or_swings"
                           text-label="Outdoor Play Set or Swings"></CheckboxInput>
          </div>
        </b-col>
        <b-col md="2"/>
      </b-row>
      <b-row align-v="baseline">
        <b-col md="2"/>
        <b-col cols="6" sm="3" md="2">
          <div>
            <CheckboxInput v-model="pdfBody.outdoor_shed" text-label="Outdoor Shed"></CheckboxInput>
          </div>
        </b-col>
      </b-row>
    </b-container>
    <div>
      <b-button variant="primary" @click="nextPage"> Next Page</b-button>
    </div>
  </div>
</template>

<script>

import PdfBody from '../models/PdfBody'
import CheckboxInput from '../components/CheckboxInput'
import TextInput from '../components/TextInput'
import RadioInputTwoOptions from '../components/RadioInputTwoOptions'
import PersistentChoices from '../models/PersistentChoices'
import PersistentChoicesFixtures from '../models/PersistentChoicesFixtures'

export default {
  name: 'FixturesAndPersonalProperty',
  components: {RadioInputTwoOptions, CheckboxInput, TextInput},
  data () {
    return {
      isLoaded: false,
      pdfBody: new PdfBody(),
      securitySystemRadioItem: {
        first: false,
        second: false
      },
      persistentChoices: new PersistentChoices()
    }
  },
  watch: {
    securitySystemRadioItem: {
      deep: true,
      handler () {
        this.pdfBody.security_system_rented = Boolean(this.securitySystemRadioItem.first)
        this.pdfBody.security_system_owned = Boolean(this.securitySystemRadioItem.second)
      }
    }
  },
  mounted () {
    if (localStorage.pdfBody) {
      this.pdfBody = Object.assign(new PdfBody(), JSON.parse(localStorage.pdfBody))
      if (localStorage.persistentChoices) {
        this.persistentChoices = Object.assign(new PersistentChoices(), JSON.parse(localStorage.persistentChoices))
        this.fillPersistentData(this.pdfBody, this.persistentChoices)
      } else {
        this.isLoaded = true
      }
    }
  },
  methods: {
    nextPage () {
      localStorage.pdfBody = JSON.stringify(this.pdfBody)
      this.$router.push({name: 'OfferDetails'})
    },
    fillPersistentData (pdfBody, persistentChoices) {
      Object.keys(new PersistentChoices()).forEach(key => {
        if (key in new PdfBody() && key in new PersistentChoicesFixtures()) {
          pdfBody[key] = persistentChoices[key]
        }
      }
      )
      this.isLoaded = true
    }
  }
}
</script>

<style scoped>

</style>
