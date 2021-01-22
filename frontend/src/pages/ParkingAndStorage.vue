<template>
  <div v-if="isLoaded">
    <b-card bg-variant="white" class="border-0">
      <b-row>
        <b-col>
          <H1 class="title">Parking And Storage</H1>
          <p class="mt-0 pt-0 text-center text-muted">{{ propertyType | capitalize }}</p>
          <b-progress class="my-2">
            <b-progress-bar :value="5" :max="8" :label="'5 of 8'" show-progress animated></b-progress-bar>
          </b-progress>
        </b-col>
      </b-row>
      <HeaderSiteMap :site-map="siteMap"></HeaderSiteMap>
    </b-card>
    <b-card bg-variant="light" class="border-0 mb-3" title="Parking">
      <b-row align-v="baseline">
        <b-col cols="6" sm="3" md="3">
          <div>
            <TextInput v-model="pdfBody.parking_space_numbers" text-label='Parking space number(s)'></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="3">
          <div>
            <CheckboxInput v-model="pdfBody.deeded" text-label="Deeded"></CheckboxInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="3">
          <div>
            <CheckboxInput v-model="pdfBody.assigned" text-label="Assigned"></CheckboxInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="3">
          <div>
            <CheckboxInput v-model="pdfBody.indoor" text-label="Indoor"></CheckboxInput>
          </div>
        </b-col>
      </b-row>
      <b-row align-v="baseline">
        <b-col cols="6" sm="3" md="3">
          <div>
            <CheckboxInput v-model="pdfBody.outdoor" text-label="Outdoor"></CheckboxInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="3">
          <div>
            <CheckboxInput v-model="pdfBody.limited_common_element" text-label="Limited common element"></CheckboxInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="3">
          <div>
            <TextInput v-model="pdfBody.parking_pin" text-label="Parking PIN"></TextInput>
          </div>
        </b-col>
        <b-col cols="6" sm="3" md="3"/>
      </b-row>
    </b-card>
    <b-card bg-variant="white" class="border-0">
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
import HeaderSiteMap from '../components/HeaderSiteMap'
import CheckboxInput from '../components/CheckboxInput'
import TextInput from '../components/TextInput'

export default {
  name: 'ParkingAndStorage',
  components: {TextInput, CheckboxInput, HeaderSiteMap},
  metaInfo: {
    meta: [
      {charset: 'utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1'}
    ]
  },
  data () {
    return {
      isLoaded: true,
      propertyType: '',
      pdfBody: new PdfBody(),
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
          isDisabled: true,
          color: 'gray'
        }
      ]
    }
  },
  mounted () {
    if (localStorage.pdfBody) {
      this.propertyType = localStorage.propertyType
      this.pdfBody = Object.assign(new PdfBody(), JSON.parse(localStorage.pdfBody))
      if (localStorage.token) {
        this.fillWithDataFromDatabase()
      }
      this.isLoaded = true
    }
  },
  methods: {
    nextPage () {
      localStorage.pdfBody = JSON.stringify(this.pdfBody)
      this.$router.push({name: 'OfferDetails'})
    },
    fillWithDataFromDatabase () {
      console.log('TODO')
    }
  }
}
</script>

<style scoped>

</style>
