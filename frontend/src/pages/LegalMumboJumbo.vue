<template>
  <div>
    <b-container v-if="isLoaded" :fluid="true">
      <b-row>
        <b-col>
          <H1>Legal Mumbo Jumbo</H1>
          <b-progress-bar :value="5" :max="6" :label="'Progress: 5/6'" show-progress animated></b-progress-bar>
        </b-col>
      </b-row>
      <b-row align-v="baseline">
        <b-col md="2"/>
        <b-col cols="12" sm="6" md="4">
          <RadioInputTwoOptions :item="disclosuresARadioItem"
                                item-one-label="Disclosures A Yes "
                                item-two-label="Disclosures A No "></RadioInputTwoOptions>
        </b-col>
        <b-col cols="12" sm="6" md="4">
          <RadioInputTwoOptions :item="disclosuresBRadioItem"
                                item-one-label="Disclosures B Yes "
                                item-two-label="Disclosures B No "></RadioInputTwoOptions>
        </b-col>
        <b-col md="2"/>
      </b-row>

      <b-row align-v="baseline">
        <b-col md="2"/>
        <b-col cols="12" sm="6" md="4">
          <RadioInputTwoOptions :item="disclosuresCRadioItem"
                                item-one-label="Disclosures C Yes "
                                item-two-label="Disclosures C No "></RadioInputTwoOptions>
        </b-col>
        <b-col cols="12" sm="6" md="4">
          <RadioInputTwoOptions :item="disclosuresDRadioItem"
                                item-one-label="Disclosures D Yes "
                                item-two-label="Disclosures D No "></RadioInputTwoOptions>
        </b-col>
        <b-col md="2"/>
      </b-row>

      <b-row align-v="baseline">
        <b-col cols="12" sm="12" md="6" lg="3">
          <div>
            <TextInput v-model="pdfBody.dual_agent_broker_name" text-label="Dual Agent Broker Name"></TextInput>
          </div>
        </b-col>
        <b-col cols="12" sm="12" md="6" lg="3">
          <div>
            <TextInput v-model="pdfBody.length_of_attorney_review" text-label="Length of Attorney Review"></TextInput>
          </div>
        </b-col>
        <b-col cols="12" sm="12" md="6" lg="3">
          <div>
            <TextInput v-model="pdfBody.length_of_inspection_period"
                       text-label="Length of Inspection Period"></TextInput>
          </div>
        </b-col>
        <b-col cols="12" sm="12" md="6" lg="3">
          <div>
            <TextInputDate v-model="pdfBody.offer_date" text-label="Offer Date"></TextInputDate>
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
import TextInputDate from '../components/TextInputDate'
import TextInput from '../components/TextInput'
import RadioInputTwoOptions from '../components/RadioInputTwoOptions'
import PersistentChoices from '../models/PersistentChoices'
import PersistentChoicesMumboJumbo from '../models/PersistentChoicesMumboJumbo'

export default {
  name: 'LegalMumboJumbo',
  components: {RadioInputTwoOptions, CheckboxInput, TextInput, TextInputDate},
  data () {
    return {
      isLoaded: false,
      pdfBody: new PdfBody(),
      persistentChoices: new PersistentChoices(),
      disclosuresARadioItem: {
        first: false,
        second: false
      },
      disclosuresBRadioItem: {
        first: false,
        second: false
      },
      disclosuresCRadioItem: {
        first: false,
        second: false
      },
      disclosuresDRadioItem: {
        first: false,
        second: false
      }
    }
  },
  watch: {
    disclosuresARadioItem: {
      deep: true,
      handler () {
        this.pdfBody.disclosures_a_yes = Boolean(this.disclosuresARadioItem.first)
        this.pdfBody.disclosures_a_no = Boolean(this.disclosuresARadioItem.second)
      }
    },
    disclosuresBRadioItem: {
      deep: true,
      handler () {
        this.pdfBody.disclosures_b_yes = Boolean(this.disclosuresBRadioItem.first)
        this.pdfBody.disclosures_b_no = Boolean(this.disclosuresBRadioItem.second)
      }
    },
    disclosuresCRadioItem: {
      deep: true,
      handler () {
        this.pdfBody.disclosures_c_yes = Boolean(this.disclosuresCRadioItem.first)
        this.pdfBody.disclosures_c_no = Boolean(this.disclosuresCRadioItem.second)
      }
    },
    disclosuresDRadioItem: {
      deep: true,
      handler () {
        this.pdfBody.disclosures_d_yes = Boolean(this.disclosuresDRadioItem.first)
        this.pdfBody.disclosures_d_no = Boolean(this.disclosuresDRadioItem.second)
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
      this.$router.push({name: 'ContactInfo'})
    },
    fillPersistentData (pdfBody, persistentChoices) {
      Object.keys(new PersistentChoices()).forEach(key => {
        if (key in new PdfBody() && key in new PersistentChoicesMumboJumbo()) {
          pdfBody[key] = persistentChoices[key]
        }
      }
      )
      this.changeRadioButtons()
      this.isLoaded = true
    },
    changeRadioButtons () {
      this.disclosuresARadioItem.first = this.pdfBody.disclosures_a_yes
      this.disclosuresARadioItem.second = this.pdfBody.disclosures_a_no
      this.disclosuresBRadioItem.first = this.pdfBody.disclosures_b_yes
      this.disclosuresBRadioItem.second = this.pdfBody.disclosures_b_no
      this.disclosuresCRadioItem.first = this.pdfBody.disclosures_c_yes
      this.disclosuresCRadioItem.second = this.pdfBody.disclosures_c_no
      this.disclosuresDRadioItem.first = this.pdfBody.disclosures_c_yes
      this.disclosuresDRadioItem.second = this.pdfBody.disclosures_c_no
    }
  }
}
</script>

<style scoped>

</style>
