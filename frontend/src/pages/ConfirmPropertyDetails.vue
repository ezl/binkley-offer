<template>
  <div v-if="isLoaded">
      <b-row>
        <b-col>
          <H1 class="title">Confirm Property Details</H1>
          <b-progress class="my-2">
            <b-progress-bar :value="2" :max="8" :label="'2 of 8'" show-progress animated></b-progress-bar>
          </b-progress>
        </b-col>
      </b-row>
      <HeaderSiteMap :site-map="siteMap"></HeaderSiteMap>
      <b-alert  v-if="showError" :show="true" dismissible variant="danger">
        <strong><b-icon icon="exclamation-circle-fill" variant="danger"></b-icon> Error: We couldn't get the data for that property</strong>
        <br>
        <br>
        <p>Either we were unable to retrieve the data for that property address or that property address data from Redfin does not match the PDF template fields we were expecting.</p>
        <p>You can either manually enter the information in the form fields below or press this back button to search again.</p>
        <br>
        <b-button @click="backPage" variant="danger"><b-icon icon="arrow-left-circle"></b-icon> Back to Property Search</b-button>
      </b-alert>
      <b-card bg-variant="white" class="border-top-0 border-right-0 border-left-0">
        <b-form-group
          label-cols-lg="3"
          label="Property: "
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mb-0"
        >
          <TextInput :special-field="true" v-model="pdfBody.property_street_address"
                     title="Property Street Address" text-label=" "></TextInput>
          <TextInput :special-field="true" v-model="pdfBody.property_locality" title="Property Locality"
                     text-label=" "></TextInput>
          <TextInput :special-field="true" v-model="pdfBody.property_region" title="Property Region"
                     text-label=" "></TextInput>
          <TextInput :special-field="true" v-model="pdfBody.property_postal_code"
                     title="Property Postal Code" text-label=" "></TextInput>
          <TextInput :special-field="true" v-model="pdfBody.parcel_identification_number"
                     title="Parcel Identification Number" text-label=" "></TextInput>
        </b-form-group>
      </b-card>

    <b-card bg-variant="white" class="border-top-0 border-right-0 border-left-0">
      <b-form-group
        label-cols-lg="3"
        label="Agent Details: "
        label-size="lg"
        label-class="font-weight-bold pt-0"
        class="mb-0"
      >
        <TextInput :special-field="true" v-model="pdfBody.agent_details_name" title="Agent Details Name"
                    text-label=" "></TextInput>
        <TextInput :special-field="true" v-model="pdfBody.agent_details_company"
                    title="Agent Details Company" text-label=" "></TextInput>
      </b-form-group>
    </b-card>

    <b-card bg-variant="white" class="border-top-0 border-right-0 border-left-0">
      <b-form-group
          label-cols-lg="3"
          label="HOA Info: "
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mb-0"
      >
        <TextInput :special-field="true" v-model="pdfBody.hoa_dues" title="HOA Dues" text-label=" "></TextInput>
        <RadioInputTwoOptions :special-field="true" :item="specialAssessmentRadioItem"
                              text-label="Special Assessment?"
                              item-one-label="Yes "
                              item-two-label="No "></RadioInputTwoOptions>
        <TextInput :special-field="true" v-model="pdfBody.deliver_association" title="Buyer to deliver Association documents within :" append="business days" text-label=" "></TextInput>

      </b-form-group>
    </b-card>

    <b-card bg-variant="white" class="border-0">
      <b-form-group
        label-cols-lg="3"
        label="Tax Information:"
        label-size="lg"
        label-class="font-weight-bold pt-0"
        class="mb-0"
      >
        <TextInputMoney prepend="$" v-model="pdfBody.tax" title="Tax" text-label=" "></TextInputMoney>
        <TextInput :special-field="true" v-model="pdfBody.tax_year" title="Tax Year" text-label=" "></TextInput>
        <CheckboxInput :special-field="true" v-model="tax_exemptions" title="Tax Exemptions"></CheckboxInput>
      </b-form-group>
    </b-card>
    <b-card v-if="tax_exemptions" bg-variant="white" class="border-bottom-0 border-right-0 border-left-0">
      <b-form-group
          label-cols-lg="3"
          label="Exemptions: "
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mb-0"
      >
        <CheckboxInput :special-field="true" v-model="pdfBody.homeowner" title="Homeowner's"></CheckboxInput>
        <CheckboxInput :special-field="true" v-model="pdfBody.senior" title="Senior"></CheckboxInput>
        <CheckboxInput :special-field="true" v-model="pdfBody.senior_freeze" title="Senior Freeze"></CheckboxInput>
        <CheckboxInput :special-field="true" v-model="pdfBody.historical" title="Historical"></CheckboxInput>

      </b-form-group>
    </b-card>
    <b-card bg-variant="white" class="border-bottom-0 border-right-0 border-left-0">
      <b-form-group
          label-cols-lg="3"
          label="Other: "
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mb-0"
      >
        <TextInput :special-field="true" v-model="pdfBody.prorated" title="Prorated Based On" text-label=" "></TextInput>

        <div v-if="isLoaded">
        <b-row>
          <b-col>
            <b-button v-if="!showError" class="btn float-right mr-auto" variant="primary" @click="nextPage"><b-icon icon="arrow-right-circle"></b-icon>  Next Page
            </b-button>
          </b-col>
        </b-row>
      </div>
      </b-form-group>
    </b-card>
  </div>
</template>

<script>
import PdfBody from '../models/PdfBody'
import * as axios from 'axios'
import CheckboxInput from '../components/CheckboxInput'
import TextInput from '../components/TextInput'
import TextInputMoney from '../components/TextInputMoney'
import HeaderSiteMap from '../components/HeaderSiteMap'
import RadioInputTwoOptions from '../components/RadioInputTwoOptions'

export default {
  name: 'ConfirmPropertyDetails',
  metaInfo: {
    meta: [
      {charset: 'utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1'}
    ]
  },
  components: {RadioInputTwoOptions, HeaderSiteMap, TextInputMoney, TextInput, CheckboxInput},
  data () {
    return {
      pdfBody: new PdfBody(),
      isLoaded: false,
      showError: '',
      tax_exemptions: false,
      specialAssessmentRadioItem: {
        first: false,
        second: false
      },
      siteMap: [
        {
          displayName: 'Address',
          pageUrl: 'Search',
          isDisabled: false,
          color: 'dodgerblue'
        },
        {
          displayName: 'Property Details',
          pageUrl: 'ConfirmPropertyDetails',
          isDisabled: true,
          color: 'gray'
        }
      ]
    }
  },
  mounted () {
    this.pdfBody = Object.assign(new PdfBody(), JSON.parse(localStorage.pdfBody))
    this.loadScrappedData()
  },
  watch: {
    pdfBody: {
      deep: true,
      handler () {
        if (this.pdfBody.property_street_address || this.pdfBody.property_locality || this.pdfBody.property_region ||
          this.pdfBody.property_region || this.pdfBody.property_postal_code ||
          this.pdfBody.parcel_identification_number || this.pdfBody.agent_details_name ||
          this.pdfBody.agent_details_company || this.pdfBody.agent_details_company || this.pdfBody.hoa_dues ||
          this.pdfBody.tax || this.pdfBody.tax_year || this.pdfBody.tax_exemptions) {
          this.showError = ''
        }
      }
    },
    specialAssessmentRadioItem: {
      deep: true,
      handler () {
        this.pdfBody.special_assessment_yes = Boolean(this.specialAssessmentRadioItem.first)
        this.pdfBody.special_assessment_no = Boolean(this.specialAssessmentRadioItem.second)
      }
    }
  },
  methods: {
    loadScrappedData: function () {
      axios({
        url: 'http://50.116.19.93:8000/api/scrapper/',
        method: 'POST',
        data: {url: this.pdfBody.url}
      }).then(response => {
        if (response.data) {
          this.pdfBody.property_street_address = response.data.property_street_address
          this.pdfBody.property_locality = response.data.property_locality
          this.pdfBody.property_region = response.data.property_region
          this.pdfBody.property_postal_code = response.data.property_postal_code
          this.pdfBody.agent_details_name = response.data.agent_details_name
          this.pdfBody.agent_details_company = response.data.agent_details_company
          this.pdfBody.hoa_dues = response.data.hoa_dues
          this.pdfBody.tax = response.data.tax
          this.pdfBody.tax_year = response.data.tax_year
          this.pdfBody.tax_exemptions = response.data.tax_exemptions
          this.pdfBody.parcel_identification_number = response.data.parcel_identification_number
          this.isLoaded = true
        }
      }
      ).catch(e => {
        if (e.response.status === 409) {
          this.showError = e.response.data.detail
          this.isLoaded = true
        }
      })
    },
    nextPage: function () {
      localStorage.pdfBody = JSON.stringify(this.pdfBody)
      this.$router.push({name: 'BuyerAndSeller'})
    },
    backPage: function () {
      this.$router.push({name: 'Home'})
    }
  }
}
</script>

<style scoped>

</style>
