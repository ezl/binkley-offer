<template>
  <div>
    <b-container v-if="isLoaded">
      <b-row>
        <b-col>
          <H1 class="title">Create an Account</H1>
        </b-col>
      </b-row>
      <b-form @submit="registerAccount" @reset="onReset" v-if="show">
        <b-form-group
          label-cols-lg="2"
          id="input-group-1"
          label="E-mail address:"
          label-for="input-1"
          description="We'll never share your email with anyone else.">
          <b-form-input
            id="input-1"
            v-model="registerAccountBody.email"
            type="email"
            required
            placeholder="Enter email"
          ></b-form-input>
        </b-form-group>
        <b-form-group label-cols-lg="2" id="input-group-2" label="Password:" label-for="input-2"
                      description="Password should be at least 4 characters, contain one number, one uppercase letter and one special character">
          <b-form-input
            id="input-2"
            v-model="registerAccountBody.password"
            required
            type="password"
            placeholder="Enter Password"
          ></b-form-input>
          <b-form-text text-variant="danger" v-if="passwordError">
            {{ passwordError }}
          </b-form-text>
          <b-form-text text-variant="danger" v-if="passwordErrorServer">
            {{ passwordErrorServer }}
          </b-form-text>
        </b-form-group>
        <b-form-group label-cols-lg="2" id="input-group-12" label="Password (Confirm):" label-for="input-12"
                      description="Please confirm password">
          <b-form-input
            id="input-12"
            v-model="passwordConfirmation"
            required
            type="password"
            placeholder="Enter Password"
          ></b-form-input>
          <b-form-text text-variant="danger" v-if="passwordError">
            {{ passwordError }}
          </b-form-text>
        </b-form-group>
        <h5 class="text-center">Enter your information below for faster form completion in the future.</h5>
        <b-form-group label-cols-lg="2" id="input-group-3" label="First Name:" label-for="input-3">
          <b-form-input
            id="input-3"
            v-model="registerAccountBody.first_name"
          ></b-form-input>
        </b-form-group>
        <b-form-group label-cols-lg="2" id="input-group-4" label="Last Name:" label-for="input-4">
          <b-form-input
            id="input-4"
            v-model="registerAccountBody.last_name"
          ></b-form-input>
        </b-form-group>
        <b-form-group label-cols-lg="2" id="input-group-5" label="Agent MLS#:" label-for="input-5">
          <b-form-input
            id="input-5"
            v-model="registerAccountBody.agent_mls"
          ></b-form-input>
        </b-form-group>
        <b-form-group label-cols-lg="2" id="input-group-6" label="Agent License#:" label-for="input-6">
          <b-form-input
            id="input-6"
            v-model="registerAccountBody.agent_license"
          ></b-form-input>
        </b-form-group>
        <b-form-group label-cols-lg="2" id="input-group-7" label="Brokerage:" label-for="input-7">
          <b-form-input
            id="input-7"
            v-model="registerAccountBody.brokerage"
          ></b-form-input>
        </b-form-group>
        <b-form-group label-cols-lg="2" id="input-group-8" label="Broker MLS#:" label-for="input-8">
          <b-form-input
            id="input-8"
            v-model="registerAccountBody.brokerage_mls"
          ></b-form-input>
        </b-form-group>
        <b-form-group label-cols-lg="2" id="input-group-9" label="Brokerage License:" label-for="input-9">
          <b-form-input
            id="input-9"
            v-model="registerAccountBody.brokerage_license"
          ></b-form-input>
        </b-form-group>
        <b-form-group label-cols-lg="2" id="input-group-10" label="Agent Phone:" label-for="input-10">
          <b-form-input
            id="input-10"
            v-model="registerAccountBody.agent_phone"
          ></b-form-input>
        </b-form-group>
        <b-form-group label-cols-lg="2" id="input-group-11" label="Agent Fax:" label-for="input-11">
          <b-form-input
            id="input-11"
            v-model="registerAccountBody.agent_fax"
          ></b-form-input>
        </b-form-group>
        <b-form-group label-cols-lg="2">
          <b-button type="submit" variant="success">Create Account</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
          <b-button v-if="accountCreated" @click="goToHome" variant="success" class="float-right">Home <b-icon icon="arrow-right-circle"></b-icon></b-button>
        </b-form-group>
        <b-alert  v-if="accountCreated" :show="true" dismissible variant="success">
          <strong>Account Created Successfully </strong>
        </b-alert>
      </b-form>
    </b-container>
  </div>
</template>

<script>
import * as axios from 'axios'
import RegisterAccount from '../models/RegisterAccount'
import LoggedUserDetails from '../models/LoggedUserDetails'

export default {
  name: 'Register',
  metaInfo: {
    meta: [
      {charset: 'utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1'}
    ]
  },
  data () {
    return {
      registerAccountBody: new RegisterAccount(),
      futureUserDetails: new LoggedUserDetails(),
      passwordConfirmation: '',
      passwordError: '',
      passwordErrorServer: '',
      accountCreated: false,
      show: true,
      isLoaded: false
    }
  },
  mounted () {
    if (localStorage.futureUserDetails) {
      this.futureUserDetails = Object.assign(new LoggedUserDetails(), JSON.parse(localStorage.futureUserDetails))
      this.registerAccountBody.agent_mls = this.futureUserDetails.agent_mls
      this.registerAccountBody.agent_license = this.futureUserDetails.agent_license
      this.registerAccountBody.brokerage = this.futureUserDetails.brokerage
      this.registerAccountBody.brokerage_mls = this.futureUserDetails.brokerage_mls
      this.registerAccountBody.brokerage_license = this.futureUserDetails.brokerage_license
      this.registerAccountBody.agent_phone = this.futureUserDetails.agent_phone
      this.registerAccountBody.agent_fax = this.futureUserDetails.agent_fax
      console.log(this.futureUserDetails)
    }
    this.isLoaded = true
  },
  methods: {
    registerAccount (evt) {
      evt.preventDefault()
      this.passwordError = ''
      if (this.registerAccountBody.password === this.passwordConfirmation) {
        axios({
          // url: 'http://50.116.19.93:8000/api/user-auth/',
          url: '/api/user-auth/',
          data: this.registerAccountBody,
          method: 'POST'
        }).then(response => {
          if (response.status === 200) {
            this.accountCreated = true
          }
        }).catch(err => {
          if (err.response.status === 409) {
            this.passwordErrorServer = err.response.data.detail
          }
        })
      } else {
        this.passwordError = 'Passwords are not the same'
      }
    },
    goToHome () {
      this.$router.push({name: 'PropertyType'})
    },
    onReset (evt) {
      evt.preventDefault()
      this.registerAccountBody.email = ''
      this.registerAccountBody.password = ''
      this.registerAccountBody.first_name = ''
      this.registerAccountBody.last_name = ''
      this.registerAccountBody.agent_mls = ''
      this.registerAccountBody.agent_license = ''
      this.registerAccountBody.brokerage = ''
      this.registerAccountBody.brokerage_mls = ''
      this.registerAccountBody.brokerage_license = ''
      this.registerAccountBody.agent_phone = ''
      this.registerAccountBody.agent_fax = ''
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    }
  }
}
</script>

<style scoped>

</style>
