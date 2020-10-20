<template>
  <div :key="forceUpdateCount">
    <b-container>
      <b-row>
        <b-col>
          <H1 class="title">Contact Info</H1>
          <b-progress class="my-2">
            <b-progress-bar :value="6" :max="6" :label="'6 of 6'" show-progress animated></b-progress-bar>
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
            <TextInput :special-field="true" v-model="pdfBody.designated_agent" title="Designated Agent"
                       text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.agent_mls" title="Agent MLS" text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.agent_license" title="Agent License"
                       text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.brokerage" title="Brokerage" text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.brokerage_mls" title="Brokerage MLS"
                       text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.brokerage_license" title="Brokerage License"
                       text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.broker_address" title="Broker Address"
                       text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.agent_phone" title="Agent Phone"
                       text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.agent_fax" title="Agent Fax" text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.broker_email" title="Broker Email"
                       text-label=" "></TextInput>
            <CheckboxInput v-model="saveForFutureUseBroker" :special-field="true"
                           text-label="Save for future use"></CheckboxInput>
            <CheckboxInput v-model="saveForFutureUseBrokerProfile" :special-field="true"
                           text-label="Save this profile for future use"></CheckboxInput>
            <b-dropdown id="dropdown-grouped" text="Buyer Broker Profiles" class="m-2">
              <b-dropdown-group v-for="(item, index) in brokerProfiles" :key="index">
                <b-dropdown-item-button @click="selectProfile(index, 'broker')"> Profile {{index + 1}} </b-dropdown-item-button>
                <b-dropdown-text>Designated Agent: <b>{{item.designated_agent}}</b></b-dropdown-text>
                <b-dropdown-text>Agent Mls: <b>{{item.agent_mls}}</b></b-dropdown-text>
                <b-dropdown-text>Agent License: <b>{{item.agent_license}}</b></b-dropdown-text>
                <b-dropdown-text>Brokerage: <b>{{item.brokerage}}</b></b-dropdown-text>
                <b-dropdown-text>Brokerage Mls: <b>{{item.brokerage_mls}}</b></b-dropdown-text>
                <b-dropdown-text>Brokerage License: <b>{{item.brokerage_license}}</b></b-dropdown-text>
                <b-dropdown-text>Broker Address: <b>{{item.broker_address}}</b></b-dropdown-text>
                <b-dropdown-text>Agent Phone: <b>{{item.agent_phone}}</b></b-dropdown-text>
                <b-dropdown-text>Agent Fax: <b>{{item.agent_fax}}</b></b-dropdown-text>
                <b-dropdown-text>Broker Email: <b>{{item.broker_email}}</b></b-dropdown-text>
                <b-dropdown-divider></b-dropdown-divider>
              </b-dropdown-group>
          </b-dropdown>
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
            <TextInput :special-field="true" v-model="pdfBody.attorney_name" title="Attorney Name"
                       text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.attorney_address" title="Attorney Address"
                       text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.attorney_phone" title="Attorney Phone"
                       text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.attorney_fax" title="Attorney Fax"
                       text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.attorney_email" title="Attorney Email"
                       text-label=" "></TextInput>
            <CheckboxInput v-model="saveForFutureUseAttorney" :special-field="true"
                           text-label="Save for future use"></CheckboxInput>
            <CheckboxInput v-model="saveForFutureUseAttorneyProfile" :special-field="true"
                           text-label="Save this profile for future use"></CheckboxInput>
            <b-dropdown id="dropdown-grouped" text="Buyer Attorney Profiles" class="m-2">
              <b-dropdown-group v-for="(item, index) in attorneyProfiles" :key="index">
                <b-dropdown-item-button @click="selectProfile(index, 'attorney')"> Profile {{index + 1}} </b-dropdown-item-button>
                <b-dropdown-text>Attorney Name: <b>{{item.attorney_name}}</b></b-dropdown-text>
                <b-dropdown-text>Attorney Address: <b>{{item.attorney_address}}</b></b-dropdown-text>
                <b-dropdown-text>Attorney Phone: <b>{{item.attorney_phone}}</b></b-dropdown-text>
                <b-dropdown-text>Attorney Fax: <b>{{item.attorney_fax}}</b></b-dropdown-text>
                <b-dropdown-text>Attorney Email: <b>{{item.attorney_email}}</b></b-dropdown-text>
                <b-dropdown-divider></b-dropdown-divider>
              </b-dropdown-group>
          </b-dropdown>
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
            <TextInput :special-field="true" v-model="pdfBody.lender_name" title="Lender Name"
                       text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.lender_company" title="Lender Company"
                       text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.lender_address" title="Lender Address"
                       text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.lender_phone" title="Lender Phone"
                       text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.lender_fax" title="Lender Fax" text-label=" "></TextInput>
            <TextInput :special-field="true" v-model="pdfBody.lender_email" title="Lender Email"
                       text-label=" "></TextInput>
            <CheckboxInput v-model="saveForFutureUseLender" :special-field="true"
                           text-label="Save for future use"></CheckboxInput>
            <CheckboxInput v-model="saveForFutureUseLenderProfile" :special-field="true"
                           text-label="Save this profile for future use"></CheckboxInput>
            <b-dropdown id="dropdown-grouped" text="Buyer Lender Profiles" class="m-2">
              <b-dropdown-group v-for="(item, index) in lenderProfiles" :key="index">
                <b-dropdown-item-button @click="selectProfile(index, 'lender')"> Profile {{index + 1}} </b-dropdown-item-button>
                <b-dropdown-text>Lender Name: <b>{{item.lender_name}}</b></b-dropdown-text>
                <b-dropdown-text>Lender Company: <b>{{item.lender_company}}</b></b-dropdown-text>
                <b-dropdown-text>Lender Address: <b>{{item.lender_address}}</b></b-dropdown-text>
                <b-dropdown-text>Lender Phone: <b>{{item.lender_phone}}</b></b-dropdown-text>
                <b-dropdown-text>Lender Fax: <b>{{item.lender_fax}}</b></b-dropdown-text>
                <b-dropdown-text>Lender Email: <b>{{item.lender_email}}</b></b-dropdown-text>
                <b-dropdown-divider></b-dropdown-divider>
              </b-dropdown-group>
          </b-dropdown>
          </b-form-group>
          <b-row>
            <b-col>
              <b-button v-if="!loading" variant="primary" class="btn float-right" @click="convertPdf"> Generate PDF
              </b-button>
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
import PersistentChoicesContactBroker from '../models/PersistentChoicesContactBroker'
import PersistentChoicesContactAttorney from '../models/PersistentChoicesContactAttorney'
import PersistentChoicesContactLender from '../models/PersistentChoicesContactLender'

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
      forceUpdateCount: 0,
      isLoaded: false,
      loading: false,
      pdfBody: new PdfBody(),
      persistentChoices: new PersistentChoices(),
      saveForFutureUseBroker: false,
      saveForFutureUseAttorney: false,
      saveForFutureUseLender: false,
      saveForFutureUseBrokerProfile: false,
      saveForFutureUseAttorneyProfile: false,
      saveForFutureUseLenderProfile: false,
      brokerProfiles: [],
      attorneyProfiles: [],
      lenderProfiles: [],
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
      if (localStorage.token) {
        this.fillWithDataFromDatabase()
      }
      if (localStorage.brokerProfiles) {
        this.brokerProfiles = Object.assign([], JSON.parse(localStorage.brokerProfiles))
      }
      if (localStorage.attorneyProfiles) {
        this.attorneyProfiles = Object.assign([], JSON.parse(localStorage.attorneyProfiles))
      }
      if (localStorage.lenderProfiles) {
        this.lenderProfiles = Object.assign([], JSON.parse(localStorage.lenderProfiles))
      }
      if (localStorage.persistentChoices && !localStorage.token) {
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
              // var fileURL = window.URL.createObjectURL(new Blob([response.data]))
              // var fileLink = document.createElement('a')
              // fileLink.href = fileURL
              // fileLink.setAttribute('download', responseGet.data.pdf_src.split('/').pop())
              // document.body.appendChild(fileLink)
              // fileLink.click()
              this.showFile(response.data, responseGet.data.pdf_src.split('/').pop())
              this.loading = false
              localStorage.pdfBody = null
              localStorage.persistentChoices = null
              let newPersistentChoices = new PersistentChoices()
              Object.keys(new PersistentChoices()).forEach(key => {
                if (key in new PdfBody() && !(key in new PersistentChoicesContactBroker()) &&
                !(key in new PersistentChoicesContactAttorney()) &&
                !(key in new PersistentChoicesContactLender())) {
                  newPersistentChoices[key] = this.pdfBody[key]
                }
              }
              )
              if (this.saveForFutureUseBroker) {
                this.putDataOnLocalStorage(newPersistentChoices, new PersistentChoicesContactBroker())
              }
              if (this.saveForFutureUseAttorney) {
                this.putDataOnLocalStorage(newPersistentChoices, new PersistentChoicesContactAttorney())
              }
              if (this.saveForFutureUseLender) {
                this.putDataOnLocalStorage(newPersistentChoices, new PersistentChoicesContactAttorney())
              }
              if (this.saveForFutureUseBrokerProfile) {
                localStorage.brokerProfiles = JSON.stringify(this.createProfileForSectionInLocalStorage(this.brokerProfiles, new PersistentChoicesContactBroker()))
              }
              if (this.saveForFutureUseAttorneyProfile) {
                localStorage.attorneyProfiles = JSON.stringify(this.createProfileForSectionInLocalStorage(this.attorneyProfiles, new PersistentChoicesContactAttorney()))
              }
              if (this.saveForFutureUseLenderProfile) {
                localStorage.lenderProfiles = JSON.stringify(this.createProfileForSectionInLocalStorage(this.lenderProfiles, new PersistentChoicesContactLender()))
              }
              localStorage.persistentChoices = JSON.stringify(newPersistentChoices)
              if (localStorage.token) {
                axios({
                  url: 'http://50.116.19.93:8000/api/user-preferences/',
                  method: 'POST',
                  headers: {
                    'Authorization': 'Token ' + localStorage.token
                  },
                  data: newPersistentChoices
                })
              }
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
            if (key in new PdfBody() && key in new PersistentChoicesContact()) {
              this.pdfBody[key] = response.data[key]
            }
          })
          this.isLoaded = true
        }
      })
    },
    putDataOnLocalStorage (newPersistentChoices, type) {
      Object.keys(new PersistentChoices()).forEach(key => {
        if (key in type) {
          newPersistentChoices[key] = this.pdfBody[key]
        }
      }
      )
    },
    createProfileForSectionInLocalStorage (storage, type) {
      let item = type
      Object.keys(new PersistentChoices()).forEach(key => {
        if (key in type) {
          item[key] = this.pdfBody[key]
        }
      }
      )
      storage.push(item)
      return storage
    },
    selectProfile (index, type) {
      switch (type) {
        case 'broker':
          if (this.brokerProfiles.length > 0) {
            this.pdfBody.designated_agent = this.brokerProfiles[index].designated_agent
            this.pdfBody.agent_mls = this.brokerProfiles[index].agent_mls
            this.pdfBody.agent_license = this.brokerProfiles[index].agent_license
            this.pdfBody.brokerage = this.brokerProfiles[index].brokerage
            this.pdfBody.brokerage_mls = this.brokerProfiles[index].brokerage_mls
            this.pdfBody.brokerage_license = this.brokerProfiles[index].brokerage_license
            this.pdfBody.broker_address = this.brokerProfiles[index].broker_address
            this.pdfBody.agent_phone = this.brokerProfiles[index].agent_phone
            this.pdfBody.agent_fax = this.brokerProfiles[index].agent_fax
            this.pdfBody.broker_email = this.brokerProfiles[index].broker_email
          }
          break
        case 'attorney':
          if (this.attorneyProfiles.length > 0) {
            this.pdfBody.attorney_name = this.attorneyProfiles[index].attorney_name
            this.pdfBody.attorney_address = this.attorneyProfiles[index].attorney_address
            this.pdfBody.attorney_phone = this.attorneyProfiles[index].attorney_phone
            this.pdfBody.attorney_fax = this.attorneyProfiles[index].attorney_fax
            this.pdfBody.attorney_email = this.attorneyProfiles[index].attorney_email
          }
          break
        case 'lender':
          if (this.lenderProfiles.length > 0) {
            this.pdfBody.lender_name = this.lenderProfiles[index].lender_name
            this.pdfBody.lender_company = this.lenderProfiles[index].lender_company
            this.pdfBody.lender_address = this.lenderProfiles[index].lender_address
            this.pdfBody.lender_phone = this.lenderProfiles[index].lender_phone
            this.pdfBody.lender_fax = this.lenderProfiles[index].lender_fax
            this.pdfBody.lender_email = this.lenderProfiles[index].lender_email
          }
          break
      }
      this.forceUpdate()
    },
    showFile (blob, fileName) {
      var newBlob = new Blob([blob], {type: 'application/pdf'})
      if (window.navigator && window.navigator.msSaveOrOpenBlob) {
        window.navigator.msSaveOrOpenBlob(newBlob)
        return
      }
      const data = window.URL.createObjectURL(newBlob)
      var link = document.createElement('a')
      link.href = data
      link.download = fileName
      link.click()
      setTimeout(function () {
        // For Firefox it is necessary to delay revoking the ObjectURL
        window.URL.revokeObjectURL(data)
      }, 100)
    },
    forceUpdate () {
      this.forceUpdateCount += 1
    }
  }
}
</script>

<style scoped>

</style>
