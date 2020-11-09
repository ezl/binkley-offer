<template>
  <div>
    <b-container v-if="isLoaded">
      <b-row>
        <b-col>
          <H1 class="title">Offer Details</H1>
          <b-progress class="my-2">
            <b-progress-bar :value="4" :max="6" :label="'4 of 6'" show-progress animated></b-progress-bar>
          </b-progress>
        </b-col>
      </b-row>
      <HeaderSiteMap :site-map="siteMap"></HeaderSiteMap>
      <b-card bg-variant="white" class="border-top-0 border-right-0 border-left-0">
        <b-form-group
          label-cols-lg="3"
          label="Purchase Price: "
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mb-0"
        >
          <TextInputMoney prepend="$" title="Purchase Price" v-model="pdfBody.purchase_price"
                          text-label=" "></TextInputMoney>
        </b-form-group>
      </b-card>
      <b-card bg-variant="white" class="border-top-0 border-right-0 border-left-0">
        <b-form-group
          label-cols-lg="3"
          label="Closing Cost Credit: "
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mb-0"
        >
          <RadioInputTwoOptions :special-field="true" text-label="Credit Buyer at Closing: "
                                :item="creditBuyerAtClosingRadioItem" item-one-label=" Yes"
                                item-two-label="No"></RadioInputTwoOptions>
          <TextInputMoney v-if="this.pdfBody.credit_buyer_at_closing_yes" title="Dollar Amount" prepend="$"
                          :special-field="true" text-label="Dollar Amount"
                          v-model="pdfBody.credit_buyer_at_closing_if_yes_amount"></TextInputMoney>
          <b-form-group v-if="this.pdfBody.credit_buyer_at_closing_yes"
                        label-cols-sm="3"
                        label="or"
                        label-align-sm="right">
          </b-form-group>
          <TextInputMoney v-if="this.pdfBody.credit_buyer_at_closing_yes" title="Percent Amount" prepend="%"
                          :special-field="true" text-label="Percent Amount"
                          v-model="pdfBody.credit_buyer_at_closing_if_no_percentage"></TextInputMoney>
        </b-form-group>
      </b-card>
      <b-card bg-variant="white" class="border-top-0 border-right-0 border-left-0">
        <b-form-group
          label-cols-lg="3"
          label="Home Warranty: "
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mb-0"
        >
          <TextInputMoney title="Home Warranty Amount" prepend="$" v-model="pdfBody.home_warranty_amount"
                          text-label=""></TextInputMoney>
        </b-form-group>
      </b-card>
      <b-card bg-variant="white" class="border-top-0 border-right-0 border-left-0">
        <b-form-group
          label-cols-lg="3"
          label="Earnest Money: "
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mb-0"
        >
          <TextInput :special-field=true title="Escrowee"
                     v-model="pdfBody.brokerage_for_earnest_money" text-label="(Brokerage For Earnest Money)"
          ></TextInput>
          <p><strong>The initial earnest money amount after the acceptance date shall be</strong></p>
          <TextInputMoney title="Amount" prepend="$" v-model="pdfBody.initial_earnest_money_amount"
                          text-label="Initial Earnest Money Dollar Amount"></TextInputMoney>
          <b-form-group label-cols-sm="3" label="paid via" label-align-sm="right"></b-form-group>
          <TextInput :special-field="true" title="Payment Type"
                     v-model="pdfBody.how_buyer_deposits_earnest_money"
                     text-label="e.g. check, wire, etc."></TextInput>
          <b-form-group label-cols-sm="3" label="within" label-align-sm="right"></b-form-group>
          <TextInput :special-field="true" append="Days" title="Initial Earnest Money Due"
                     v-model="pdfBody.initial_earnest_money_due_date"
                     text-label=" "></TextInput>
          <p><strong>After the attorney approval period, the earnest money shall be increased to:</strong></p>
          <TextInputMoney title="Amount" prepend="$"
                          v-model="pdfBody.balance_of_earnest_money_amount"
                          text-label="Total Earnest Money Dollar Amount"></TextInputMoney>

          <b-form-group label-cols-sm="3" label="within" label-align-sm="right"></b-form-group>

          <TextInput :special-field="true" title="Balance of Earnest Money Due" append="Days"
                     v-model="pdfBody.balance_of_earnest_money_due_date"
                     text-label=" "></TextInput>
        </b-form-group>
      </b-card>
      <b-card bg-variant="white" class="border-top-0 border-right-0 border-left-0">
        <b-form-group
          label-cols-lg="3"
          label="Mortgage Contingency: "
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mb-0"
        >
          <RadioInputTwoOptions :special-field="true" :item="mortgageRadioItem"
                                text-label="Contract Subject to Mortgage: "
                                item-one-label="Yes"
                                item-two-label="No"></RadioInputTwoOptions>
          <TextInputDate v-if="this.pdfBody.contract_subject_to_mortgage_yes" title="Mortgage Contingency Date"
                         v-model="pdfBody.mortgage_contingency_date"
                         text-label="Mortgage Contingency Date"></TextInputDate>
          <TextInputMoney v-if="this.pdfBody.contract_subject_to_mortgage_yes" title="Buyer Loan to Value" prepend="%"
                          v-model="pdfBody.buyer_loan_to_value"
                          text-label=" "></TextInputMoney>
          <TextInputMoney v-if="this.pdfBody.contract_subject_to_mortgage_yes" title="Buyer Interest Rate" prepend="%"
                          v-model="pdfBody.buyer_interest_rate"
                          text-label=" "></TextInputMoney>
          <TextInput v-if="this.pdfBody.contract_subject_to_mortgage_yes" :special-field="true" title="Buyer Loan Term"
                     v-model="pdfBody.buyer_loan_term"
                     text-label="(Years) "></TextInput>
        </b-form-group>
      </b-card>
      <b-card bg-variant="white" class="border-0">
        <b-form-group
          label-cols-lg="3"
          label="Closing: "
          label-size="lg"
          label-class="font-weight-bold pt-0"
          class="mb-0"
        >
          <TextInputDate title="Closing Date" v-model="pdfBody.closing_date" text-label="Closing Date"></TextInputDate>
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
import CheckboxInput from '../components/CheckboxInput'
import TextInput from '../components/TextInput'
import TextInputMoney from '../components/TextInputMoney'
import PdfBody from '../models/PdfBody'
import TextInputDate from '../components/TextInputDate'
import RadioInputTwoOptions from '../components/RadioInputTwoOptions'
import HeaderSiteMap from '../components/HeaderSiteMap'

export default {
  name: 'OfferDetails',
  components: {HeaderSiteMap, RadioInputTwoOptions, TextInputDate, CheckboxInput, TextInput, TextInputMoney},
  data () {
    return {
      isLoaded: false,
      pdfBody: new PdfBody(),
      mortgageRadioItem: {
        first: false,
        second: false
      },
      creditBuyerAtClosingRadioItem: {
        first: false,
        second: false
      },
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
          isDisabled: true,
          color: 'gray'
        }
      ]
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
      this.creditBuyerAtClosingRadioItem.first = this.pdfBody.credit_buyer_at_closing_yes
      this.creditBuyerAtClosingRadioItem.second = this.pdfBody.credit_buyer_at_closing_no
      this.mortgageRadioItem.first = this.pdfBody.contract_subject_to_mortgage_yes
      this.mortgageRadioItem.second = this.pdfBody.contract_subject_to_mortgage_no
      if (this.pdfBody.closing_date) {
        this.pdfBody.closing_date = this.getDate(new Date(this.pdfBody.closing_date))
      } else {
        this.pdfBody.closing_date = this.getDate(null)
      }
      if (this.pdfBody.mortgage_contingency_date) {
        this.pdfBody.mortgage_contingency_date = this.getDate(new Date(this.pdfBody.mortgage_contingency_date))
      } else {
        this.pdfBody.mortgage_contingency_date = this.getDate(null)
      }
      this.isLoaded = true
    }
  },
  methods: {
    nextPage () {
      localStorage.pdfBody = JSON.stringify(this.pdfBody)
      this.$router.push({name: 'LegalMumboJumbo'})
    },
    getDate (dateGiven) {
      const toTwoDigits = num => num < 10 ? '0' + num : num
      let date = dateGiven || new Date()
      let year = date.getFullYear()
      let month = toTwoDigits(date.getMonth() + 1)
      let day = toTwoDigits(date.getDate())
      return `${year}-${month}-${day}`
    }
  }
}
</script>

<style scoped>

</style>
