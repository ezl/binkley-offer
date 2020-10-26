<template>
  <b-container>
    <b-jumbotron bg-variant="white" class="text-center">
      <template #header class="text">Select Property Type</template>

      <template #lead>
        Before we start, what type of property are you writing a contract for ?
      </template>
      <br>
      <br>
      <b-card-group deck>
        <b-card border-variant="primary" v-if="isAttachedSelected"
                style="color: #007BFF"
                footer="Attached Property"
                footer-bg-variant="white"
                footer-border-variant="white">
          <b-icon-building font-scale="10"/>
        </b-card>
        <b-card v-else @click="selectAttached"
                footer="Attached Property"
                style="color: gray"
                footer-bg-variant="white"
                footer-border-variant="white">
          <b-icon-building font-scale="10"/>
        </b-card>
        <b-card border-variant="primary"
                v-if="isDetachedSelected"
                style="color: #007BFF"
                footer="Detached Property"
                footer-bg-variant="white"
                footer-border-variant="white">
          <b-icon-house-door font-scale="10"/>
        </b-card>
        <b-card v-else @click="selectDetached"
                style="color: gray"
                footer="Detached Property"
                footer-bg-variant="white"
                footer-border-variant="white">
          <b-icon-house-door font-scale="10"/>
        </b-card>
      </b-card-group>
      <br>
      <br>
      <b-button size="lg" variant="primary" class="btn" @click="getStarted()"> Get Started</b-button>
    </b-jumbotron>
  </b-container>
</template>

<script>

import ArrowRightCircle from '../components/icons/ArrowRightCircle'

export default {
  name: 'PropertyType',
  components: {
    ArrowRightCircle
  },
  data () {
    return {
      isAttachedSelected: false,
      isDetachedSelected: false
    }
  },
  methods: {
    selectAttached () {
      this.isAttachedSelected = true
      this.isDetachedSelected = false
    },
    selectDetached () {
      this.isDetachedSelected = true
      this.isAttachedSelected = false
    },
    getStarted () {
      if (this.isAttachedSelected) {
        localStorage.propertyType = 'attached'
      }
      if (this.isDetachedSelected) {
        localStorage.propertyType = 'detached'
      }
      if (this.isAttachedSelected || this.isDetachedSelected) {
        this.$router.push({name: 'Search'})
      }
    }
  }
}
</script>

<style scoped>

</style>
