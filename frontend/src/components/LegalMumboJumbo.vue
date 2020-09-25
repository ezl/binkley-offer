<template>
  <div>
    <H1>Legal Mumbo Jumbo</H1>
    <b-progress-bar :value="4" :max="5" :label="'Progress: 4/5'" show-progress animated></b-progress-bar>
    <b-row align-v="baseline">
      <b-col sm="3">
        <div>
          <p>Disclosures A <b>Yes</b></p>
          <CheckboxInput v-model="pdfBody.disclosures_a_yes"></CheckboxInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Disclosures A <b>No</b></p>
          <CheckboxInput v-model="pdfBody.disclosures_a_no"></CheckboxInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Disclosures B <b>Yes</b></p>
          <CheckboxInput v-model="pdfBody.disclosures_b_yes"></CheckboxInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Disclosures B <b>No</b></p>
          <CheckboxInput v-model="pdfBody.disclosures_b_no"></CheckboxInput>
        </div>
      </b-col>
    </b-row>

    <b-row align-v="baseline">
      <b-col sm="3">
        <div>
          <p>Disclosures C <b>Yes</b></p>
          <CheckboxInput v-model="pdfBody.disclosures_c_yes"></CheckboxInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Disclosures C <b>No</b></p>
          <CheckboxInput v-model="pdfBody.disclosures_c_no"></CheckboxInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Disclosures D <b>Yes</b></p>
          <CheckboxInput v-model="pdfBody.disclosures_d_yes"></CheckboxInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Disclosures D <b>No</b></p>
          <CheckboxInput v-model="pdfBody.disclosures_d_no"></CheckboxInput>
        </div>
      </b-col>
    </b-row>

    <b-row align-v="baseline">
      <b-col sm="3">
        <div>
          <p>Dual Agent Broker Name</p>
          <TextInput v-model="pdfBody.dual_agent_broker_name"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Length of Attorney Review</p>
          <TextInput v-model="pdfBody.length_of_attorney_review"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Length of Inspection Period</p>
          <TextInput v-model="pdfBody.length_of_inspection_period"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Offer Date</p>
          <TextInput v-model="pdfBody.offer_date"></TextInput>
        </div>
      </b-col>
    </b-row>
    <div>
      <b-button variant="primary" @click="nextPage"> Next Page</b-button>
    </div>
  </div>
</template>

<script>
import PdfBody from '../models/PdfBody'
import CheckboxInput from './CheckboxInput'
import TextInput from './TextInput'

export default {
  name: 'LegalMumboJumbo',
  components: {CheckboxInput, TextInput},
  data () {
    return {
      pdfBody: new PdfBody()
    }
  },
  mounted () {
    if (localStorage.pdfBody) {
      this.pdfBody = Object.assign(new PdfBody(), JSON.parse(localStorage.pdfBody))
    }
  },
  methods: {
    nextPage () {
      localStorage.pdfBody = JSON.stringify(this.pdfBody)
      this.$router.push({name: 'ContactInfo'})
    }
  }
}
</script>

<style scoped>

</style>
