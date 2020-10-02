<template>
  <div>
    <b-container v-if="isLoaded && !showError" :fluid="true">
      <b-row>
        <b-col>
          <H1>Confirm Property Details</H1>
          <b-progress class="my-2">
            <b-progress-bar :value="2" :max="6" :label="'Progress: 2/6'" show-progress animated></b-progress-bar>
          </b-progress>
        </b-col>
      </b-row>
      <div v-if="showError">{{ showError }}</div>
      <b-row align-v="baseline">
        <b-col md="2"/>
        <b-col cols="6" sm="3" md="2">
          <div>
            <TextInput v-model="pdfBody.property_street_address" title="Property Street Address"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <TextInput v-model="pdfBody.property_locality" title="Property Locality"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <TextInput v-model="pdfBody.property_region" title="Property Region"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <TextInput v-model="pdfBody.property_postal_code" title="Property Postal Code"></TextInput>
          </div>
        </b-col>
        <b-col md="2"/>
      </b-row>

      <b-row align-v="baseline">
        <b-col md="2"/>
        <b-col cols="6" sm="3" md="2">
          <div>
            <TextInput v-model="pdfBody.agent_details_name" title="Agent Details Name"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <TextInput v-model="pdfBody.agent_details_company" title="Agent Details Company"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <TextInput v-model="pdfBody.hoa_dues" title="Hoa Dues"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <TextInput v-model="pdfBody.parcel_identification_number" title="Parcel Identification Number"></TextInput>
          </div>
        </b-col>
        <b-col md="2"/>
      </b-row>

      <b-row align-v="baseline">
        <b-col md="2"/>
        <b-col cols="6" sm="3" md="2">
          <div>
            <TextInput v-model="pdfBody.tax" title="Tax"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <TextInput v-model="pdfBody.tax_year" title="Tax Year"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="2">
          <div>
            <TextInput v-model="pdfBody.tax_exemptions" title="Tax Exemptions"></TextInput>
          </div>
        </b-col>
        <b-col md="2"/>
        <b-col md="2"/>
      </b-row>
      <div v-if="isLoaded">
        <b-row>
          <b-col>
            <b-button v-if="!showError" variant="primary" @click="nextPage"> Next Page</b-button>
            <b-button v-else variant="danger" @click="backPage">Back To Menu</b-button>
          </b-col>
        </b-row>
      </div>
    </b-container>
  </div>
</template>

<script>
import PdfBody from '../models/PdfBody'
import * as axios from 'axios'
import CheckboxInput from '../components/CheckboxInput'
import TextInput from '../components/TextInput'

export default {
  name: 'ConfirmPropertyDetails',
  components: {TextInput, CheckboxInput},
  data () {
    return {
      pdfBody: new PdfBody(),
      isLoaded: false,
      showError: ''
    }
  },
  mounted () {
    this.pdfBody = Object.assign(new PdfBody(), JSON.parse(localStorage.pdfBody))
    this.loadScrappedData()
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
      this.$router.push({name: 'FixturesAndPersonalProperty'})
    },
    backPage: function () {
      this.$router.push({name: 'Home'})
    }
  }
}
</script>

<style scoped>

</style>
