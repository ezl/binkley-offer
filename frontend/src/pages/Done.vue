<template>
  <div>
    <b-jumbotron bg-variant="white" class="text-center">
      <template #header>
        Tada!
        <br>
        <ConfettiIcon/>
      </template>

      <template #lead>
        <p class="text-left">Here's your offer letter PDF for <strong> {{ pdfBody.property_street_address }}</strong> - {{ propertyType | capitalize }}</p>
        <br>
        <p class="text-left">For best results, <span style="color: #ff0000">view PDF in Safari after downloading.</span> Then Print or Save.</p>
        <br>
        <b-button v-if="!loading" variant="primary" class="btn" @click="convertPdf"> Download PDF
        </b-button>
        <b-spinner v-if="loading" variant="primary" label="Spinning"></b-spinner>
      </template>

      <hr class="my-4">

      <div class="text-left">
        <p>
          Now didn't that suck less than filling it out manually?
          <br>
          <br>
          If you'd like to be able to:
        </p>
        <ul>
          <li>Save profiles (e.g. broker, lender, attorney info) to reuse</li>
          <li>Save PDFs to download again later</li>
          <li>Connect to your Gmail account to get buyer info (name, email, attachments like pre-approval letters)</li>
          <li>Send to Docusign for signing (coming soon)</li>
        </ul>
        <strong>Then create an account for next time.</strong>
      </div>
      <br>
      <b-button variant="primary" class="btn" @click="createAccount()"> Create An Account
      </b-button>

    </b-jumbotron>
  </div>
</template>

<script>
import PdfBody from '../models/PdfBody'
import * as axios from 'axios'
import HeaderSiteMap from '../components/HeaderSiteMap'
import ConfettiIcon from '../components/icons/ConfettiIcon'
import LoggedUserDetails from '../models/LoggedUserDetails'

export default {
  name: 'Done',
  components: {ConfettiIcon, HeaderSiteMap},
  metaInfo: {
    meta: [
      {charset: 'utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1'}
    ]
  },
  data () {
    return {
      isLoaded: false,
      loading: false,
      pdfBody: new PdfBody(),
      propertyType: '',
      futureUserDetails: new LoggedUserDetails(),
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
          isDisabled: false,
          color: 'dodgerblue'
        },
        {
          displayName: 'Done',
          pageUrl: 'Done',
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
      Object.keys(new LoggedUserDetails()).forEach(key => {
        if (key in new PdfBody()) {
          this.futureUserDetails[key] = this.pdfBody[key]
        }
      })
      localStorage.futureUserDetails = JSON.stringify(this.futureUserDetails)
    }
    this.isLoaded = true
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
              this.showFile(response.data, responseGet.data.pdf_src.split('/').pop())
              this.loading = false
              this.localStorage = null
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
    showFile (blob, fileName) {
      var newBlob = new Blob([blob], {type: 'application/pdf'})
      console.log(newBlob)
      if (window.navigator && window.navigator.msSaveOrOpenBlob) {
        window.navigator.msSaveOrOpenBlob(newBlob)
        return
      }
      const data = window.URL.createObjectURL(newBlob)
      var link = document.createElement('a')
      link.href = data
      link.download = fileName
      console.log(link)
      link.click()
      setTimeout(function () {
        // For Firefox it is necessary to delay revoking the ObjectURL
        window.URL.revokeObjectURL(data)
      }, 100)
    },
    createAccount () {
      this.$router.push({name: 'Register'})
    }
  }
}
</script>

<style scoped>

</style>
