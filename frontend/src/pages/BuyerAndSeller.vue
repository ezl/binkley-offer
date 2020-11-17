<template>
  <div>
    <b-container v-if="isLoaded">
      <b-row>
        <b-col>
          <H1 class="title">Buyer and Seller </H1>
          <b-progress class="my-2">
            <b-progress-bar :value="3" :max="8" :label="'3 of 8'" show-progress animated></b-progress-bar>
          </b-progress>
        </b-col>
      </b-row>
      <HeaderSiteMap :site-map="siteMap"></HeaderSiteMap>
      <b-card bg-variant="white" class="border-top-0 border-right-0 border-left-0">
        <b-form-group
          label-cols-lg="3"
          label="Buyer:"
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mb-0"
        >
          <TextInput :special-field="true" v-model="pdfBody.buyer_name" title="Name"
                     text-label=" "></TextInput>
          <TextInput :special-field="true" v-model="pdfBody.buyer_email" title="Email" text-label=" "></TextInput>
        </b-form-group>
      </b-card>
      <b-card bg-variant="white" class="border-0">
        <b-form-group
          label-cols-lg="3"
          label="Seller:"
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mb-0"
        >
          <TextInput :special-field="true" v-model="pdfBody.seller_name" title="Name"
                     text-label=" "></TextInput>
          <TextInput :special-field="true" v-model="pdfBody.seller_email" title="Email" text-label=" "></TextInput>
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
    </b-container>
  </div>
</template>

<script>
import HeaderSiteMap from '../components/HeaderSiteMap'
import PdfBody from '../models/PdfBody'
import PersistentChoices from '../models/PersistentChoices'
import TextInput from '../components/TextInput'

export default {
  name: 'BuyerAndSeller',
  metaInfo: {
    meta: [
      {charset: 'utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1'}
    ]
  },
  components: {TextInput, HeaderSiteMap},
  data () {
    return {
      isLoaded: false,
      pdfBody: new PdfBody(),
      persistentChoices: new PersistentChoices(),
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
          isDisabled: true,
          color: 'gray'
        }
      ]
    }
  },
  mounted () {
    if (localStorage.pdfBody) {
      this.pdfBody = Object.assign(new PdfBody(), JSON.parse(localStorage.pdfBody))
      this.isLoaded = true
    }
  },
  methods: {
    nextPage () {
      localStorage.pdfBody = JSON.stringify(this.pdfBody)
      this.$router.push({name: 'FixturesAndPersonalProperty'})
    }
  }
}
</script>

<style scoped>

</style>
