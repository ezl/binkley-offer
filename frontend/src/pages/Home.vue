<template>
  <div>
    <b-container>
      <b-jumbotron bg-variant="white" class="text-center">
        <template #header>
          <b-button variant="primary" class="btn" @click="getStarted"> Get Started</b-button>
        </template>

        <template #lead>
          <p class="text-center">Already have and account? <a class="hyperlink-text" @click="login">Login</a></p>
        </template>
      </b-jumbotron>
    </b-container>
  </div>
</template>

<script>
export default {
  name: 'Home',
  metaInfo: {
    meta: [
      {charset: 'utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1'}
    ]
  },
  data () {
    return {}
  },
  methods: {
    getStarted () {
      this.$router.push({name: 'Register'})
    },
    login () {
      this.$router.push({name: 'Login'})
    }

  }
}
</script>

<style scoped>

</style>
