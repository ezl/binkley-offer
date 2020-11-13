<template>
  <div v-if="isLoaded">
      <b-row>
        <b-col>
          <H1 class="title">Legal Mumbo Jumbo</H1>
          <b-progress class="my-2">
            <b-progress-bar :value="7" :max="8" :label="'7 of 8'" show-progress animated></b-progress-bar>
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
          <RadioInputTwoOptions :special-field="true" :item="isHomeownerAssociation"
                                text-label="Is this home in a Homeowners Association?"
                                item-one-label="Yes "
                                item-two-label="No "></RadioInputTwoOptions>
          <RadioInputTwoOptions :special-field="true" :item="dualAgencyRadioItem"
                                text-label="Dual Agent"
                                item-one-label="Yes "
                                item-two-label="No "></RadioInputTwoOptions>
          <TextInput :special-field="true" v-if="pdfBody.dual_agent_broker_yes" v-model="pdfBody.dual_agent_broker_name"
                     title="Dual Agent Broker Name" text-label=" "></TextInput>
          <TextInput :special-field="true" v-model="pdfBody.length_of_attorney_review" append="Days"
                     title="Length of Attorney Review" text-label=" "></TextInput>
          <TextInput :special-field="true" v-model="pdfBody.length_of_inspection_period" append="Days"
                     title="Length of Inspection Period" text-label=" "></TextInput>
          <RadioInputTwoOptions :special-field="true" :item="ridersOrAddendums"
                                text-label="Any riders or addendums to add to contract?"
                                item-one-label="Yes "
                                item-two-label="No "></RadioInputTwoOptions>
          <TextInput :special-field="true" v-if="pdfBody.riders_or_addendums_yes" v-model="pdfBody.riders_or_addendums" title="Rider/Addendum Details" text-label=" "></TextInput>
          <RadioInputTwoOptions :special-field="true" :item="offerDeadline"
                                text-label="Add an offer deadline?"
                                item-one-label="Yes "
                                item-two-label="No "></RadioInputTwoOptions>
          <TextInputDate :special-field="true" v-if="pdfBody.offer_deadline_yes" v-model="pdfBody.offer_deadline" title="Offer Deadline" text-label=" "></TextInputDate>
          <TextInputDate v-model="pdfBody.offer_date" title="Offer Date" text-label=" "></TextInputDate>
          <b-form-group
                        label-cols-sm="3"
                        label="Attached Riders and Addendums"
                        label-align-sm="right">
              <b-form-textarea
                  id="textarea"
                  v-model="pdfBody.attached_riders_and_addendums"
                  placeholder="Enter something..."
                  rows="3"
                  max-rows="6"/>
          </b-form-group>
          <TextInputDate v-model="pdfBody.contract_accepted_on_or_before" title="Contract accepted by seller on or before" text-label=" "></TextInputDate>

        </b-form-group>
        <b-row>
          <b-col>
            <b-button class="btn float-right mr-auto" variant="primary" @click="nextPage">
              <b-icon icon="arrow-right-circle"></b-icon>
              Next Page
            </b-button>
          </b-col>
        </b-row>
      </b-card>
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
  metaInfo: {
    meta: [
      {charset: 'utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1'}
    ]
  },
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
      dualAgencyRadioItem: {
        first: false,
        second: false
      },
      isHomeownerAssociation: {
        first: false,
        second: false
      },
      offerDeadline: {
        first: false,
        second: false
      },
      ridersOrAddendums: {
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
          displayName: 'Buyer And Seller',
          pageUrl: 'BuyerAndSeller',
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
          displayName: 'Parking And Storage',
          pageUrl: 'ParkingAndStorage',
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
    },
    dualAgencyRadioItem: {
      deep: true,
      handler () {
        this.pdfBody.dual_agent_broker_yes = Boolean(this.dualAgencyRadioItem.first)
        this.pdfBody.dual_agent_broker_no = Boolean(this.dualAgencyRadioItem.second)
      }
    },
    isHomeownerAssociation: {
      deep: true,
      handler () {
        this.pdfBody.homeowner_yes = Boolean(this.isHomeownerAssociation.first)
        this.pdfBody.homeowner_no = Boolean(this.isHomeownerAssociation.second)
      }
    },
    offerDeadline: {
      deep: true,
      handler () {
        this.pdfBody.offer_deadline_yes = Boolean(this.offerDeadline.first)
        this.pdfBody.offer_deadline_no = Boolean(this.offerDeadline.second)
      }
    },
    ridersOrAddendums: {
      deep: true,
      handler () {
        this.pdfBody.riders_or_addendums_yes = Boolean(this.ridersOrAddendums.first)
        this.pdfBody.riders_or_addendums_no = Boolean(this.ridersOrAddendums.second)
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
      }
      if (this.pdfBody.offer_date) {
        this.pdfBody.offer_date = this.getDate(new Date(this.pdfBody.offer_date))
      } else {
        this.pdfBody.offer_date = this.getDate(null)
      }
      if (this.pdfBody.offer_deadline) {
        this.pdfBody.offer_deadline = this.getDate(new Date(this.pdfBody.offer_deadline))
      } else {
        this.pdfBody.offer_deadline = this.getDate(null)
      }
      if (this.pdfBody.contract_accepted_on_or_before) {
        this.pdfBody.contract_accepted_on_or_before = this.getDate(new Date(this.pdfBody.contract_accepted_on_or_before))
      } else {
        this.pdfBody.contract_accepted_on_or_before = this.getDate(null)
      }
      this.isLoaded = true
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
    getDate (dateGiven) {
      const toTwoDigits = num => num < 10 ? '0' + num : num
      let date = dateGiven || new Date()
      let year = date.getFullYear()
      let month = toTwoDigits(date.getMonth() + 1)
      let day = toTwoDigits(date.getDate())
      return `${year}-${month}-${day}`
    }
  }
}
</script>

<style scoped></style>
