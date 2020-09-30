<template>
  <div>
    <H1>Offer Details</H1>
    <b-progress-bar :value="4" :max="6" :label="'Progress: 4/6'" show-progress animated></b-progress-bar>
    <b-container :fluid="true">
      <b-row align-v="baseline">
        <b-col sm="4"/>
        <b-col sm="4">
          <div>
            <TextInputMoney v-model="pdfBody.purchase_price" text-label="Purchase Price"></TextInputMoney>
          </div>
        </b-col>
        <b-col sm="4"/>
      </b-row>
      <b-row align-v="baseline">
        <b-col sm="3" md="3" lg="4"/>
        <b-col cols="12" sm="6" md="6" lg="4">
          <RadioInputTwoOptions :item="creditBuyerAtClosingRadioItem" item-one-label="Credit Buyer at Closing Yes"
                                item-two-label="Credit Buyer at Closing No"></RadioInputTwoOptions>
          <TextInput v-if="pdfBody.credit_buyer_at_closing_yes"
                     v-model="pdfBody.credit_buyer_at_closing_if_yes_amount"></TextInput>
          <TextInput v-if="pdfBody.credit_buyer_at_closing_no"
                     v-model="pdfBody.credit_buyer_at_closing_if_no_percentage"></TextInput>
        </b-col>
        <b-col sm="3" md="3" lg="4"/>
      </b-row>

      <b-row align-v="baseline">
        <b-col cols="12" sm="12" md="6" lg="3">
          <div>
            <TextInputMoney v-model="pdfBody.home_warranty_amount" text-label="Home Warranty Amount"></TextInputMoney>
          </div>
        </b-col>
        <b-col cols="12" sm="12" md="6" lg="3">
          <div>
            <TextInputMoney v-model="pdfBody.brokerage_for_earnest_money"
                            text-label="Brokerage For Earnest Money"></TextInputMoney>
          </div>
        </b-col>
        <b-col cols="12" sm="12" md="6" lg="3">
          <div>
            <TextInputMoney v-model="pdfBody.initial_earnest_money_amount"
                            text-label="Initial Earnest Money Amount"></TextInputMoney>
          </div>
        </b-col>
        <b-col cols="12" sm="12" md="6" lg="3">
          <div>
            <TextInputMoney v-model="pdfBody.how_buyer_deposits_earnest_money"
                            text-label="How Buyer Deposits Earnest Money"></TextInputMoney>
          </div>
        </b-col>
      </b-row>

      <b-row align-v="baseline">
        <b-col cols="12" sm="12" md="6" lg="3">
          <div>
            <TextInputDate v-model="pdfBody.initial_earnest_money_due_date"
                           text-label="Initial Earnest Money Due Date"></TextInputDate>
          </div>
        </b-col>
        <b-col cols="12" sm="12" md="6" lg="3">
          <div>
            <TextInputMoney v-model="pdfBody.balance_of_earnest_money_amount"
                            text-label="Balance of Earnest Money Amount"></TextInputMoney>
          </div>
        </b-col>
        <b-col cols="12" sm="12" md="6" lg="3">
          <div>
            <TextInputDate v-model="pdfBody.balance_of_earnest_money_due_date"
                           text-label="Balance of Earnest Money Due Date"></TextInputDate>
          </div>
        </b-col>
        <b-col cols="12" sm="12" md="6" lg="3">
          <div>
            <TextInputDate v-model="pdfBody.mortgage_contingency_date"
                           text-label="Mortgage Contingency Date"></TextInputDate>
          </div>
        </b-col>
      </b-row>

      <b-row align-v="baseline">
        <b-col sm="3" md="3" lg="4"/>

        <b-col cols="12" sm="6" md="6" lg="4">
          <RadioInputTwoOptions :item="mortgageRadioItem" item-one-label="Contract Subject to Mortgage Yes"
                                item-two-label="Contract Subject to Mortgage No"></RadioInputTwoOptions>
        </b-col>
        <b-col sm="3" md="3" lg="4"/>
      </b-row>

      <b-row align-v="baseline">
        <b-col cols="12" sm="12" md="6" lg="3">
          <div>
            <TextInputMoney v-model="pdfBody.buyer_loan_to_value" text-label="Buyer Loan to Value"></TextInputMoney>
          </div>
        </b-col>
        <b-col cols="12" sm="12" md="6" lg="3">
          <div>
            <TextInput v-model="pdfBody.buyer_interest_rate" text-label="Buyer Interest Rate"></TextInput>
          </div>
        </b-col>
        <b-col cols="12" sm="12" md="6" lg="3">
          <div>
            <TextInput v-model="pdfBody.buyer_loan_term" text-label="Buyer Loan Term"></TextInput>
          </div>
        </b-col>
        <b-col cols="12" sm="12" md="6" lg="3">
          <div>
            <TextInputDate v-model="pdfBody.closing_date" text-label="Closing Date"></TextInputDate>
          </div>
        </b-col>
      </b-row>
    </b-container>
    <div>
      <b-button variant="primary" @click="nextPage"> Next Page</b-button>
    </div>
  </div>
</template>

<script>
import CheckboxInput from '../components/CheckboxInput'
import TextInput from '../components/TextInput'
import TextInputMoney from '../components/TextInputMoney'
import PdfBody from '../models/PdfBody'
import TextInputDate from '../components/TextInputDate'
import RadioInputTwoOptions from '../components/RadioInputTwoOptions'

export default {
  name: 'OfferDetails',
  components: {RadioInputTwoOptions, TextInputDate, CheckboxInput, TextInput, TextInputMoney},
  data () {
    return {
      pdfBody: new PdfBody(),
      mortgageRadioItem: {
        first: false,
        second: false
      },
      creditBuyerAtClosingRadioItem: {
        first: false,
        second: false
      }
    }
  },
  watch: {
    creditBuyerAtClosingRadioItem: {
      deep: true,
      handler () {
        this.pdfBody.credit_buyer_at_closing_yes = Boolean(this.creditBuyerAtClosingRadioItem.first)
        this.pdfBody.credit_buyer_at_closing_no = Boolean(this.creditBuyerAtClosingRadioItem.second)
      }
    },
    mortgageRadioItem: {
      deep: true,
      handler () {
        this.pdfBody.contract_subject_to_mortgage_yes = Boolean(this.mortgageRadioItem.first)
        this.pdfBody.contract_subject_to_mortgage_no = Boolean(this.mortgageRadioItem.second)
      }
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
