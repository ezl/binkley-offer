<template>
  <div>
    <b-container v-if="isLoaded">
      <b-row>
        <b-col>
          <H1 class="title">Legal Mumbo Jumbo</H1>
          <b-progress class="my-2">
            <b-progress-bar :value="5" :max="6" :label="'5 of 6'" show-progress animated></b-progress-bar>
          </b-progress>
        </b-col>
      </b-row>
      <HeaderSiteMap :site-map="siteMap"></HeaderSiteMap>
      <b-card bg-variant="white" class="border-top-0 border-right-0 border-left-0">
        <b-form-group
          label-cols-lg="3"
          label="Disclosures: "
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mb-0"
        >
          <RadioInputTwoOptions :special-field="true" :item="disclosuresARadioItem"
                                text-label="Illinois Residential Real Property Disclosure Report"
                                item-one-label="Yes"
                                item-two-label="No"></RadioInputTwoOptions>
          <RadioInputTwoOptions :special-field="true" :item="disclosuresBRadioItem"
                                text-label="Heat Disclosure (gas/electric)"
                                item-one-label="Yes "
                                item-two-label="No "></RadioInputTwoOptions>
          <RadioInputTwoOptions :special-field="true" :item="disclosuresCRadioItem"
                                text-label="Lead Paint Disclosure and Pamphlet"
                                item-one-label="Yes "
                                item-two-label="No "></RadioInputTwoOptions>
          <RadioInputTwoOptions :special-field="true" :item="disclosuresDRadioItem"
                                text-label="Radon Disclosure and Pamphlet"
                                item-one-label="Yes "
                                item-two-label="No "></RadioInputTwoOptions>
        </b-form-group>
      </b-card>

      <b-card bg-variant="white" class="border-0">
        <b-form-group
          label-cols-lg="3"
          label="Additional Info : "
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mb-0"
        >
          <TextInput :special-field="true" v-model="pdfBody.dual_agent_broker_name"
                     title="Dual Agent Broker Name" text-label=" "></TextInput>
          <TextInput :special-field="true" v-model="pdfBody.length_of_attorney_review" append="Days"
                     title="Length of Attorney Review" text-label=" "></TextInput>
          <TextInput :special-field="true" v-model="pdfBody.length_of_inspection_period" append="Days"
                     title="Length of Inspection Period" text-label=" "></TextInput>
          <TextInputDate v-model="pdfBody.offer_date" title="Offer Date" text-label=" "></TextInputDate>

        </b-form-group>
        <b-row>
          <b-col>
            <b-button class="btn float-right mr-auto" variant="primary" @click="nextPage"><b-icon icon="arrow-right-circle"></b-icon> Next Page</b-button>
          </b-col>
        </b-row>
      </b-card>
    </b-container>
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
import HeaderSiteMap from '../components/HeaderSiteMap'
import * as axios from 'axios'

export default {
  name: 'LegalMumboJumbo',
  components: {HeaderSiteMap, RadioInputTwoOptions, CheckboxInput, TextInput, TextInputDate},
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
      },
      siteMap: [
        {
          displayName: 'Address',
          pageUrl: 'Home',
          isDisabled: false,
          color: 'dodgerblue'
        },
        {
          displayName: 'Property Details',
          pageUrl: 'ConfirmPropertyDetails',
          isDisabled: false,
          color: 'dodgerblue'
        },
        {
          displayName: 'Fixtures And Personal Property',
          pageUrl: 'FixturesAndPersonalProperty',
          isDisabled: false,
          color: 'dodgerblue'
        },
        {
          displayName: 'Offer Details',
          pageUrl: 'OfferDetails',
          isDisabled: false,
          color: 'dodgerblue'
        },
        {
          displayName: 'Legal Mumbo Jumbo',
          pageUrl: 'LegalMumboJumbo',
          isDisabled: true,
          color: 'gray'
        }
      ]
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
      this.changeRadioButtons()
      if (localStorage.token) {
        this.fillWithDataFromDatabase()
      }
      if (localStorage.persistentChoices && !localStorage.token) {
        this.persistentChoices = Object.assign(new PersistentChoices(), JSON.parse(localStorage.persistentChoices))
        this.fillPersistentData(this.pdfBody, this.persistentChoices)
      } else {
        this.isLoaded = true
      }
    }
    if (!this.pdfBody.offer_date) {
      this.getDate()
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
      })
      this.changeRadioButtons()
      this.isLoaded = true
    },
    fillWithDataFromDatabase () {
      axios({
        url: 'http://50.116.19.93:8000/api/user-preferences/',
        method: 'GET',
        headers: {
          'Authorization': 'Token ' + localStorage.token
        }
      }).then(response => {
        if (response.status === 200) {
          Object.keys(new PersistentChoices()).forEach(key => {
            if (key in new PdfBody() && key in new PersistentChoicesMumboJumbo()) {
              this.pdfBody[key] = response.data[key]
            }
          })
          this.changeRadioButtons()
          this.isLoaded = true
        }
      })
    },
    changeRadioButtons () {
      this.disclosuresARadioItem.first = this.pdfBody.disclosures_a_yes
      this.disclosuresARadioItem.second = this.pdfBody.disclosures_a_no
      this.disclosuresBRadioItem.first = this.pdfBody.disclosures_b_yes
      this.disclosuresBRadioItem.second = this.pdfBody.disclosures_b_no
      this.disclosuresCRadioItem.first = this.pdfBody.disclosures_c_yes
      this.disclosuresCRadioItem.second = this.pdfBody.disclosures_c_no
      this.disclosuresDRadioItem.first = this.pdfBody.disclosures_d_yes
      this.disclosuresDRadioItem.second = this.pdfBody.disclosures_d_no
    },
    getDate () {
      const toTwoDigits = num => num < 10 ? '0' + num : num
      let today = new Date()
      let year = today.getFullYear()
      let month = toTwoDigits(today.getMonth() + 1)
      let day = toTwoDigits(today.getDate())
      this.pdfBody.offer_date = `${year}-${month}-${day}`
    }
  }
}
</script>

<style scoped></style>
