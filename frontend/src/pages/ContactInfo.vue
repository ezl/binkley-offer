<template>
  <div>
    <b-container :fluid="true">
      <b-row>
        <b-col>
          <H1>Contact Info</H1>
          <b-progress class="my-2">
            <b-progress-bar :value="6" :max="6" :label="'Progress: 6/6'" show-progress animated></b-progress-bar>
          </b-progress>
        </b-col>
      </b-row>
      <HeaderSiteMap :site-map="siteMap"></HeaderSiteMap>
      <div v-if="isLoaded">
        <b-card bg-variant="white" class="border-top-0 border-right-0 border-left-0">
          <b-form-group
            label-cols-lg="3"
            label="Buyer's Broker's Information:"
            label-size="lg"
            label-class="font-weight-bold pt-0"
            class="mb-0"
          >
            <TextInput :special-field="true" v-model="pdfBody.designated_agent" title="Designated Agent" text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.agent_mls" title="Agent Mls" text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.agent_license" title="Agent License" text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.brokerage" title="Brokerage" text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.brokerage_mls" title="Brokerage Mls" text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.brokerage_license" title="Brokerage License" text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.broker_address" title="Broker Address" text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.agent_phone" title="Agent Phone" text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.agent_fax" title="Agent Fax" text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.broker_email" title="Broker Email" text-label=" "></TextInput>
            <CheckboxInput :special-field="true" text-label="Save for future use"></CheckboxInput>
          </b-form-group>
        </b-card>
        <b-card bg-variant="white" class="border-top-0 border-right-0 border-left-0">
          <b-form-group
            label-cols-lg="3"
            label="Buyer's Attorney's Information:"
            label-size="lg"
            label-class="font-weight-bold pt-0"
            class="mb-0"
          >
            <TextInput :special-field="true" v-model="pdfBody.attorney_name" title="Attorney Name" text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.attorney_address" title="Attorney Address" text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.attorney_phone" title="Attorney Phone" text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.attorney_fax" title="Attorney Fax" text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.attorney_email" title="Attorney Email" text-label=" "></TextInput>
          </b-form-group>
        </b-card>
        <b-card bg-variant="white" class="border-0">
          <b-form-group
            label-cols-lg="3"
            label="Buyer's Lender's Information:"
            label-size="lg"
            label-class="font-weight-bold pt-0"
            class="mb-0"
          >
            <TextInput :special-field="true" v-model="pdfBody.lender_name" title="Lender Name" text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.lender_company" title="Lender Company" text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.lender_address" title="Lender Address" text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.lender_phone" title="Lender Phone" text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.lender_fax" title="Lender Fax" text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.lender_email" title="Lender Email" text-label=" "></TextInput>
          </b-form-group>
          <b-row>
            <b-col>
              <b-button variant="primary" class="btn float-right" @click="convertPdf"> Generate PDF</b-button>
              <b-spinner v-if="loading" class="float-right" variant="primary" label="Spinning"></b-spinner>
            </b-col>
          </b-row>
        </b-card>
      </div>
    </b-container>
  </div>
</template>

<script>
import CheckboxInput from '../components/CheckboxInput'
import TextInput from '../components/TextInput'
import PdfBody from '../models/PdfBody'
import * as axios from 'axios'
import FormGroupInput from '../components/FormGroupInput'
import PersistentChoices from '../models/PersistentChoices'
import PersistentChoicesContact from '../models/PersistentChoicesContact'
import HeaderSiteMap from '../components/HeaderSiteMap'

export default {
  name: 'ContactInfo',
  metaInfo: {
    meta: [
      {charset: 'utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1'}
    ]
  },
  components: {HeaderSiteMap, FormGroupInput, CheckboxInput, TextInput},
  data () {
    return {
      isLoaded: false,
      loading: false,
      pdfBody: new PdfBody(),
      persistentChoices: new PersistentChoices(),
      siteMap: [
        {
          displayName: 'Address/',
          pageUrl: 'Home',
          isDisabled: false,
          color: 'dodgerblue'
        },
        {
          displayName: 'Property Details/',
          pageUrl: 'ConfirmPropertyDetails',
          isDisabled: false,
          color: 'dodgerblue'
        },
        {
          displayName: 'Fixtures And Personal Property/',
          pageUrl: 'FixturesAndPersonalProperty',
          isDisabled: false,
          color: 'dodgerblue'
        },
        {
          displayName: 'Offer Details/',
          pageUrl: 'OfferDetails',
          isDisabled: false,
          color: 'dodgerblue'
        },
        {
          displayName: 'Contact Info',
          pageUrl: 'ContactInfo',
          isDisabled: true,
          color: 'gray'
        }
      ]
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
    convertPdf: function () {
      if (this.redfinUrl !== null) {
        this.loading = true
        axios({
          url: 'http://50.116.19.93:8000/api/pdf/',
          method: 'POST',
          data: this.pdfBody,
          responseType: 'blob'
        }).then(response => {
          axios({
            url: 'http://50.116.19.93:8000/api/pdf?url=' + this.pdfBody.url,
            method: 'GET'
          })
            .then(responseGet => {
              var fileURL = window.URL.createObjectURL(new Blob([response.data]))
              var fileLink = document.createElement('a')
              fileLink.href = fileURL
              fileLink.setAttribute('download', responseGet.data.pdf_src.split('/').pop())
              document.body.appendChild(fileLink)
              fileLink.click()
              this.loading = false
              localStorage.pdfBody = null
              localStorage.persistentChoices = null
              let newPersistentChoices = new PersistentChoices()
              Object.keys(new PersistentChoices()).forEach(key => {
                if (key in new PdfBody()) {
                  newPersistentChoices[key] = this.pdfBody[key]
                }
              }
              )
              localStorage.persistentChoices = JSON.stringify(newPersistentChoices)
            })
            .catch(err => {
              console.log(err)
            })
        })
          .catch(err => {
            console.log(err)
          })
      }
    },
    fillPersistentData (pdfBody, persistentChoices) {
      Object.keys(new PersistentChoices()).forEach(key => {
        if (key in new PdfBody() && key in new PersistentChoicesContact()) {
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
