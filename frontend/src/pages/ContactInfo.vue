<template>
  <div>
    <H1>Contact Info</H1>
    <b-progress-bar :value="6" :max="6" :label="'Progress: 6/6'" show-progress animated></b-progress-bar>
    <div v-if="isLoaded">
      <b-card bg-variant="light">
        <b-form-group
          label-cols-lg="3"
          label="Buyer's Broker's Information:"
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mb-0"
        >
          <FormGroupInput v-model="pdfBody.designated_agent" text-label="Designated Agent"></FormGroupInput>
          <FormGroupInput v-model="pdfBody.agent_mls" text-label="Agent Mls"></FormGroupInput>
          <FormGroupInput v-model="pdfBody.agent_license" text-label="Agent License"></FormGroupInput>
          <FormGroupInput v-model="pdfBody.brokerage" text-label="Brokerage"></FormGroupInput>
          <FormGroupInput v-model="pdfBody.brokerage_mls" text-label="Brokerage Mls"></FormGroupInput>
          <FormGroupInput v-model="pdfBody.brokerage_license" text-label="Brokerage License"></FormGroupInput>
          <FormGroupInput v-model="pdfBody.broker_address" text-label="Broker Address"></FormGroupInput>
          <FormGroupInput v-model="pdfBody.agent_phone" text-label="Agent Phone"></FormGroupInput>
          <FormGroupInput v-model="pdfBody.agent_fax" text-label="Agent Fax"></FormGroupInput>
          <FormGroupInput v-model="pdfBody.broker_email" text-label="Broker Email"></FormGroupInput>
        </b-form-group>
      </b-card>
      <b-card bg-variant="light">
        <b-form-group
          label-cols-lg="3"
          label="Buyer's Attorney's Information:"
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mb-0"
        >
          <FormGroupInput v-model="pdfBody.attorney_name" text-label="Attorney Name"></FormGroupInput>
          <FormGroupInput v-model="pdfBody.attorney_address" text-label="Attorney Address"></FormGroupInput>
          <FormGroupInput v-model="pdfBody.attorney_phone" text-label="Attorney Phone"></FormGroupInput>
          <FormGroupInput v-model="pdfBody.attorney_fax" text-label="Attorney Fax"></FormGroupInput>
          <FormGroupInput v-model="pdfBody.attorney_email" text-label="Attorney Email"></FormGroupInput>
        </b-form-group>
      </b-card>
      <b-card bg-variant="light">
        <b-form-group
          label-cols-lg="3"
          label="Buyer's Lender's Information:"
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mb-0"
        >
          <FormGroupInput v-model="pdfBody.lender_name" text-label="Lender Name"></FormGroupInput>
          <FormGroupInput v-model="pdfBody.lender_company" text-label="Lender Company"></FormGroupInput>
          <FormGroupInput v-model="pdfBody.lender_address" text-label="Lender Address"></FormGroupInput>
          <FormGroupInput v-model="pdfBody.lender_phone" text-label="Lender Phone"></FormGroupInput>
          <FormGroupInput v-model="pdfBody.lender_fax" text-label="Lender Fax"></FormGroupInput>
          <FormGroupInput v-model="pdfBody.lender_email" text-label="Lender Email"></FormGroupInput>
        </b-form-group>
        <b-row>
          <b-col sm="5"/>

          <b-col sm="2">
            <b-button variant="primary" @click="convertPdf"> Generate PDF</b-button>
            <b-spinner v-if="loading" variant="primary" label="Spinning"></b-spinner>
          </b-col>
          <b-col sm="5"/>
        </b-row>
      </b-card>
    </div>
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

export default {
  name: 'ContactInfo',
  components: {FormGroupInput, CheckboxInput, TextInput},
  data () {
    return {
      isLoaded: false,
      loading: false,
      pdfBody: new PdfBody(),
      persistentChoices: new PersistentChoices()
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
