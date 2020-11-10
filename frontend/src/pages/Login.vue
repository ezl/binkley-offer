<template>
  <div>
    <b-container>
      <b-card bg-variant="light" class="border-0">
        <b-form @submit="loginAccount" class="text-center">
          <h1>Login</h1>
          <b-form-group
            id="input-group-1"
            label-for="input-1">
            <b-form-input
              id="input-1"
              v-model="loginAccountBody.email"
              type="email"
              required
              placeholder="E-mail"
            ></b-form-input>
          </b-form-group>
          <b-form-group
            id="input-group-2"
            label-for="input-2">
            <b-form-input
              id="input-2"
              v-model="loginAccountBody.password"
              type="password"
              required
              placeholder="Password"
            ></b-form-input>
          </b-form-group>
          <b-form-group>
            <b-button type="submit" class="btn" variant="primary">Login</b-button>
            <b-form-text text-variant="danger" v-if="serverError">
              {{ serverError }}
            </b-form-text>
          </b-form-group>
          <b-form-group>
            <CheckboxInput v-model="rememberUser" text-label="Remember Me"></CheckboxInput>
            <b-form-text>
              <a class="hyperlink-text" @click="forgotPassword">Forgot Password?</a>
            </b-form-text>
          </b-form-group>
        </b-form>
      </b-card>
    </b-container>
  </div>
</template>

<script>

import * as axios from 'axios'
import LoginAccount from '../models/LoginAccount'
import CheckboxInput from '../components/CheckboxInput'

export default {
  name: 'Login',
  components: {CheckboxInput},
  metaInfo: {
    meta: [
      {charset: 'utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1'}
    ]
  },
  data () {
    return {
      loginAccountBody: new LoginAccount(),
      serverError: '',
      rememberUser: false
    }
  },
  methods: {
    loginAccount (evt) {
      evt.preventDefault()
      axios({
        url: 'http://50.116.19.93:8000/api/user-login/',
        data: this.loginAccountBody,
        method: 'POST'
      }).then(response => {
        if (response.status === 200) {
          localStorage.loggedUserDetails = JSON.stringify(response.data)
          this.$router.push({name: 'PropertyType'})
        }
      }).catch(err => {
        if (err.response.status === 404) {
          this.serverError = err.response.data.detail
        }
      })
    },
    forgotPassword () {

    }
  }
}
</script>

<style scoped>

</style>
