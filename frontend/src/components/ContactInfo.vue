<template>
  <div>
    <H1>Contact Info</H1>
    <b-progress-bar :value="5" :max="5" :label="'Progress: 5/5'" show-progress animated></b-progress-bar>
    <b-row align-v="baseline">
      <b-col sm="4">
        <div>
          <p>Designated Agent</p>
          <TextInput v-model="pdfBody.designated_agent"></TextInput>
        </div>
      </b-col>
      <b-col sm="4">
        <div>
          <p>Attorney Name</p>
          <TextInput v-model="pdfBody.attorney_name"></TextInput>
        </div>
      </b-col>
      <b-col sm="4">
        <div>
          <p>Lender Name</p>
          <TextInput v-model="pdfBody.lender_name"></TextInput>
        </div>
      </b-col>
    </b-row>

    <b-row align-v="baseline">
      <b-col sm="4">
        <b-row align-v="stretch">
          <b-col sm="6">
            <div>
              <p>Agent Mls</p>
              <TextInput v-model="pdfBody.agent_mls"></TextInput>
            </div>
          </b-col>
          <b-col sm="6">
            <div>
              <p>Agent License</p>
              <TextInput v-model="pdfBody.agent_license"></TextInput>
            </div>
          </b-col>
        </b-row>
      </b-col>
      <b-col sm="4">
        <div>
          <p>Attorney Address</p>
          <TextInput v-model="pdfBody.attorney_address"></TextInput>
        </div>
      </b-col>
      <b-col sm="4">
        <div>
          <p>Lender Company</p>
          <TextInput v-model="pdfBody.lender_company"></TextInput>
        </div>
      </b-col>
    </b-row>

    <b-row align-v="baseline">
      <b-col sm="4">
        <div>
          <p>Brokerage</p>
          <TextInput v-model="pdfBody.brokerage"></TextInput>
        </div>
      </b-col>
      <b-col sm="4">
        <b-row align-v="baseline">
          <b-col sm="6">
            <div>
              <p>Attorney Phone</p>
              <TextInput v-model="pdfBody.attorney_phone"></TextInput>
            </div>
          </b-col>
          <b-col sm="6">
            <div>
              <p>Attorney Fax</p>
              <TextInput v-model="pdfBody.attorney_fax"></TextInput>
            </div>
          </b-col>
        </b-row>
      </b-col>
      <b-col sm="4">
        <div>
          <p>Lender Address</p>
          <TextInput v-model="pdfBody.lender_address"></TextInput>
        </div>
      </b-col>
    </b-row>
    <b-row align-v="baseline">
      <b-col sm="4">
        <b-row align-v="baseline">
          <b-col sm="6">
            <div>
              <p>Brokerage Mls</p>
              <TextInput v-model="pdfBody.brokerage_mls"></TextInput>
            </div>
          </b-col>
          <b-col sm="6">
            <div>
              <p>Brokerage License</p>
              <TextInput v-model="pdfBody.brokerage_license"></TextInput>
            </div>
          </b-col>
        </b-row>
      </b-col>
      <b-col sm="4">
        <div>
          <p>Attorney Email</p>
          <TextInput v-model="pdfBody.attorney_email"></TextInput>
        </div>
      </b-col>
      <b-col sm="4">
        <b-row align-v="baseline">
          <b-col sm="6">
            <div>
              <p>Lender Phone</p>
              <TextInput v-model="pdfBody.lender_phone"></TextInput>
            </div>
          </b-col>
          <b-col sm="6">
            <div>
              <p>Lender Fax</p>
              <TextInput v-model="pdfBody.lender_fax"></TextInput>
            </div>
          </b-col>
        </b-row>
      </b-col>
    </b-row>
    <b-row align-v="baseline">
      <b-col sm="4">
        <div>
          <p>Broker Address</p>
          <TextInput v-model="pdfBody.broker_address"></TextInput>
        </div>
      </b-col>
      <b-col sm="4"/>
      <b-col sm="4">
        <div>
          <p>Lender Email</p>
          <TextInput v-model="pdfBody.lender_email"></TextInput>
        </div>
      </b-col>
    </b-row>

    <b-row align-v="baseline">
      <b-col sm="4">
        <b-row align-v="baseline">
          <b-col sm="6">
            <div>
              <p>Agent Phone</p>
              <TextInput v-model="pdfBody.agent_phone"></TextInput>
            </div>
          </b-col>
          <b-col sm="6">
            <div>
              <p>Agent Fax</p>
              <TextInput v-model="pdfBody.agent_fax"></TextInput>
            </div>
          </b-col>
        </b-row>
      </b-col>
      <b-col sm="4">
      </b-col>
      <b-col sm="4">

      </b-col>
    </b-row>

    <b-row align-v="baseline">
      <b-col sm="4">
        <div>
          <p>Broker Email</p>
          <TextInput v-model="pdfBody.broker_email"></TextInput>
        </div>
      </b-col>
      <b-col sm="4"/>
      <b-col sm="4"/>
    </b-row>

    <div>
      <b-row>
        <b-col sm="5"/>

        <b-col sm="2">
          <b-button variant="primary" @click="convertPdf"> Generate PDF</b-button>
          <b-spinner v-if="loading" variant="primary" label="Spinning"></b-spinner>
        </b-col>
        <b-col sm="5"/>
      </b-row>

    </div>
    <div>

    </div>
  </div>
</template>

<script>
import CheckboxInput from './CheckboxInput'
import TextInput from './TextInput'
import PdfBody from '../models/PdfBody'
import * as axios from 'axios'

export default {
  name: 'ContactInfo',
  components: {CheckboxInput, TextInput},
  data () {
    return {
      loading: false,
      pdfBody: new PdfBody()
    }
  },
  mounted () {
    if (localStorage.pdfBody) {
      this.pdfBody = Object.assign(new PdfBody(), JSON.parse(localStorage.pdfBody))
    }
  },
  methods: {
    convertPdf: function () {
      if (this.redfinUrl !== null) {
        this.loading = true
        axios({
          url: 'http://localhost:5000/api/pdfs',
          method: 'POST',
          data: JSON.stringify(this.pdfBody),
          headers: {
            'Content-Type': 'application/json;charset=utf-8'
          },
          responseType: 'blob'
        }).then(response => {
          axios({
            url: 'http://localhost:5000/api/pdf?url=' + this.pdfBody.url,
            method: 'GET'
          })
            .then(responseGet => {
              this.pdfBody = new PdfBody()
              var fileURL = window.URL.createObjectURL(new Blob([response.data]))
              var fileLink = document.createElement('a')
              fileLink.href = fileURL
              fileLink.setAttribute('download', responseGet.data.pdf_src.split('/').pop())
              document.body.appendChild(fileLink)
              fileLink.click()
              this.loading = false
            })
            .catch(err => {
              console.log(err)
            })
        })
          .catch(err => {
            console.log(err)
          })
      }
    }
  }
}
</script>

<style scoped>

</style>
