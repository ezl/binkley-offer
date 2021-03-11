<template>
  <div>
    <b-card bg-variant="white" class="border-0" body-class="p-0">
      <b-row align-v="baseline">
        <b-col>
          <H1 class="title">Binkley Offer: Write an offer letter from your phone</H1>
          <b-progress class="my-2">
            <b-progress-bar v-if="propertyType === 'attached'" :value="1" :max="8" :label="'1 of 8'" show-progress
                            animated></b-progress-bar>
            <b-progress-bar v-else-if="propertyType === 'detached'" :value="1" :max="7" :label="'1 of 7'" show-progress
                            animated></b-progress-bar>
          </b-progress>
        </b-col>
      </b-row>
    </b-card>
    <b-card bg-variant="white" class="border-0" body-class="p-0">
      <b-row align-v="start">
        <b-col sm="6">
          <TextInput class="mb-0 pb-0" v-model="queryUrl" text-label="Type property address..."></TextInput>
          <p class="mt-0 pt-0 text-muted font-weight-lighter font-weight-italic redfinURL">{{ pdfBody.url }}</p>
        </b-col>
        <b-col sm="6">
          <b-button block variant="outline-success" :disabled="!pdfBody.url" @click="nextPage">Next Page
            <arrow-right-circle/>
          </b-button>
        </b-col>
      </b-row>

      <b-row align-v="baseline">
        <b-col sm="6">
          <b-list-group class="py-sm-1 cursor-selectable" v-for="(property, index) in propertiesList"
                        :key="index">
            <b-list-group-item class="mt-1" v-bind:class="{ 'active' : isSelected(index)}" @click="saveUrl(index)">
              {{ property.name }} {{ property.subName }}
            </b-list-group-item>
          </b-list-group>
        </b-col>
        <b-col sm="6">
          <p class="mt-0 pt-0 text-muted font-weight-lighter font-weight-italic" v-if="pdfCacheLoaded">A previous
            version of pdf was loaded</p>
          <b-dropdown v-if="pdfIds.length > 0" id="dropdown-grouped" text="Previous PDFs"
                      class="m-2" variant="primary">
            <b-dropdown-group v-for="(item, indexPdf) in pdfIds" :key="indexPdf">
              <b-dropdown-item-button @click="selectPdf(indexPdf)">
                <b>{{ indexPdf + 1 }}</b>
              </b-dropdown-item-button>
              <b-dropdown-divider v-if="indexPdf + 1 < pdfIds.length"></b-dropdown-divider>
            </b-dropdown-group>
          </b-dropdown>
        </b-col>
      </b-row>
    </b-card>
  </div>
</template>

<script>
import * as axios from 'axios'
import PdfBody from '../models/PdfBody.js'
import TextInput from '../components/TextInput'
import CheckboxInput from '../components/CheckboxInput'
import ArrowRightCircle from '../components/icons/ArrowRightCircle'
import * as _ from 'debounce'

export default {
  name: 'Search',
  components: {
    CheckboxInput,
    TextInput,
    ArrowRightCircle
  },
  metaInfo: {
    meta: [
      {charset: 'utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1'}
    ]
  },
  data () {
    return {
      selected: null,
      propertyType: '',
      pdfBody: new PdfBody(),
      redfinUrl: '',
      pdfName: '',
      queryUrl: null,
      propertiesList: [],
      pdfCacheLoaded: false,
      pdfIds: []
    }
  },
  mounted () {
    this.searchRedfinUrl()
    localStorage.pdfCacheLoaded = JSON.stringify(false)
    this.propertyType = localStorage.propertyType
    localStorage.pdfBody = new PdfBody()
    if (localStorage.pdfIds) {
      this.pdfIds = Object.assign([], JSON.parse(localStorage.pdfIds))
    }
  },
  watch: {
    queryUrl: _.debounce(function () {
      this.searchRedfinUrl()
    }, 500)
  },
  methods: {
    isSelected (i) {
      return i === this.selected
    },
    searchRedfinUrl () {
      this.propertiesList = []
      if (this.queryUrl) {
        axios({
          url: 'http://50.116.19.93:8000/api/search/',
          method: 'POST',
          data: {url: 'https://www.redfin.com/stingray/do/location-autocomplete?location=' + this.queryUrl + '&count=10&v=2'}
        }).then(response => {
          if (response.data) {
            this.propertiesList = []
            response.data.properties.forEach(property => {
              this.propertiesList.push(property)
            })
          }
        })
      }
    },
    saveUrl (index) {
      this.pdfBody.url = 'https://www.redfin.com' + this.propertiesList[index].url
      this.selected = index
    },
    selectPdf (index) {
      axios({
        url: 'http://50.116.19.93:8000/api/fields?id=' + this.pdfIds[index],
        method: 'GET'
      })
        .then(response => {
          let pdfBodyTemp = new PdfBody()
          for (let key in this.pdfBody) {
            pdfBodyTemp[key] = response.data[key]
          }
          this.pdfBody = pdfBodyTemp
          this.pdfCacheLoaded = true
          localStorage.pdfCacheLoaded = JSON.stringify(true)
        })
        .catch(err => {
          console.log(err)
        })
    },
    nextPage () {
      this.pdfBody.property_type = localStorage.propertyType
      localStorage.pdfBody = JSON.stringify(this.pdfBody)
      this.$router.push({name: 'ConfirmPropertyDetails'})
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.cursor-selectable {
  cursor: pointer;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
.redfinURL {
  font-size: 0.7em;
}
</style>
