<template>
  <div>
    <H1>Offer Details</H1>
    <b-progress-bar :value="3" :max="5" :label="'Progress: 3/5'" show-progress animated></b-progress-bar>
    <b-row align-v="baseline">
      <b-col sm="4"/>
      <b-col sm="4">
        <div>
          <p>Purchase Price</p>
          <b-input-group prepend="$" size="md">
            <b-form-input v-model="pdfBody.purchase_price"></b-form-input>
          </b-input-group>
        </div>
      </b-col>
      <b-col sm="4"/>
    </b-row>
    <b-row align-v="baseline">
      <b-col sm="3"/>
      <b-col sm="3">
        <div>
          <p>Credit Buyer at Closing Yes</p>
          <CheckboxInput v-model="pdfBody.credit_buyer_at_closing_yes"></CheckboxInput>
          <TextInput v-if="pdfBody.credit_buyer_at_closing_yes"
                     v-model="pdfBody.credit_buyer_at_closing_if_yes_amount"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Credit Buyer at Closing No</p>
          <CheckboxInput v-model="pdfBody.credit_buyer_at_closing_no"></CheckboxInput>
          <TextInput v-if="pdfBody.credit_buyer_at_closing_no"
                     v-model="pdfBody.credit_buyer_at_closing_if_no_percentage"></TextInput>
        </div>
      </b-col>
      <b-col sm="3"/>
    </b-row>

    <b-row align-v="bottom">
      <b-col sm="3">
        <div>
          <p>Home Warranty Amount</p>
          <TextInput v-model="pdfBody.home_warranty_amount"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Brokerage For Earnest Money</p>
          <TextInput v-model="pdfBody.brokerage_for_earnest_money"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Initial Earnest Money Amount</p>
          <TextInput v-model="pdfBody.initial_earnest_money_amount"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>How Buyer Deposits Earnest Money</p>
          <TextInput v-model="pdfBody.how_buyer_deposits_earnest_money"></TextInput>
        </div>
      </b-col>
    </b-row>

    <b-row align-v="baseline">
      <b-col sm="3">
        <div>
          <p>Initial Earnest Money Due Date</p>
          <TextInput v-model="pdfBody.initial_earnest_money_due_date"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Balance of Earnest Money Amount</p>
          <TextInput v-model="pdfBody.balance_of_earnest_money_amount"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Balance of Earnest Money Due Date</p>
          <TextInput v-model="pdfBody.balance_of_earnest_money_due_date"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Mortgage Contingency Date</p>
          <TextInput v-model="pdfBody.mortgage_contingency_date"></TextInput>
        </div>
      </b-col>
    </b-row>

    <b-row align-v="baseline">
      <b-col sm="3"/>
      <b-col sm="3">
        <div>
          <p>Contract Subject to Mortgage <b>YES</b></p>
          <CheckboxInput v-model="pdfBody.contract_subject_to_mortgage_yes"></CheckboxInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Contract Subject to Mortgage <b>NO</b></p>
          <CheckboxInput v-model="pdfBody.contract_subject_to_mortgage_no"></CheckboxInput>
        </div>
      </b-col>
      <b-col sm="3"/>
    </b-row>

    <b-row align-v="baseline">
      <b-col sm="3">
        <div>
          <p>Buyer Loan to Value</p>
          <TextInput v-model="pdfBody.buyer_loan_to_value"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Buyer Interest Rate</p>
          <TextInput v-model="pdfBody.buyer_interest_rate"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Buyer Loan Term</p>
          <TextInput v-model="pdfBody.buyer_loan_term"></TextInput>
        </div>
      </b-col>
      <b-col sm="3">
        <div>
          <p>Closing Date</p>
          <TextInput v-model="pdfBody.closing_date"></TextInput>
        </div>
      </b-col>
    </b-row>

    <div>
      <b-button variant="primary" @click="nextPage"> Next Page</b-button>
    </div>
  </div>
</template>

<script>
import CheckboxInput from './CheckboxInput'
import TextInput from './TextInput'
import PdfBody from '../models/PdfBody'

export default {
  name: 'OfferDetails',
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
      this.$router.push({name: 'LegalMumboJumbo'})
    }
  }
}
</script>

<style scoped>

</style>
