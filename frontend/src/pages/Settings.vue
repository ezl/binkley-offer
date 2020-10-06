<template>
  <div>
    <b-button @click="getAuth" class="g-signin-button" v-if="!authCodeFromLocalStorage" :disabled="!isInit">Get Auth
      Code
    </b-button>
    <b-button @click="signIn" class="g-signin-button" v-if="!isSignIn" :disabled="!isInit">Sign in with Google
    </b-button>
    <b-button @click="signOut" class="g-signin-button" v-if="isSignIn" :disabled="!isInit">Sign out</b-button>
  </div>
</template>

<script>
import * as axios from 'axios'

export default {
  name: 'Settings',
  metaInfo: {
    meta: [
      {charset: 'utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1'}
    ]
  },
  data () {
    return {
      isSignIn: false,
      isInit: false,
      authCodeFromLocalStorage: ''
    }
  },
  mounted () {
    let thisLoaded = this
    let checkGAuthLoad = setInterval(function () {
      thisLoaded.isInit = thisLoaded.$gAuth.isInit
      thisLoaded.isSignIn = thisLoaded.$gAuth.isAuthorized
      if (thisLoaded.isInit) clearInterval(checkGAuthLoad)
    }, 1000)
    thisLoaded.authCodeFromLocalStorage = localStorage.authCode
  },
  methods: {
    getAuth: async function () {
      const authCode = localStorage.authCode ? localStorage.authCode : await this.$gAuth.getAuthCode()
      localStorage.authCode = authCode
      this.authCodeFromLocalStorage = authCode
      axios({
        url: 'http://50.116.19.93:8000/api/auth-google/',
        method: 'POST',
        data: {
          code: authCode,
          redirect_uri: 'postmessage'
        }
      }).then(response => {
        /// TODO things when get response from backend
      }).catch(err => {
        console.log(err)
        localStorage.removeItem('authCode')
        this.authCodeFromLocalStorage = null
      })
    },
    signIn: async function () {
      const googleUser = await this.$gAuth.signIn()
      console.log(googleUser)
      this.isSignIn = this.$gAuth.isAuthorized
    },
    signOut: async function () {
      const response = await this.$gAuth.signOut()
      console.log(response)
      this.isSignIn = this.$gAuth.isAuthorized
    }
  }

}
</script>

<style scoped>
.g-signin-button {
  display: inline-block;
  padding: 4px 8px;
  border-radius: 3px;
  background-color: #3c82f7;
  color: #fff;
  box-shadow: 0 3px 0 #0f69ff;
}
</style>
