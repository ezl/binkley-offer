<template>
  <b-container>
    <b-jumbotron bg-variant="white" class="text-center">
      <template #header class="text">Select Property Type</template>

      <template #lead>
        Before we start, what type of property are you writing a contract for ?
      </template>
      <br>
      <br>
      <b-card-group deck class="justify-content-center">
        <b-row no-gutters>
          <b-col class="px-2" v-if="isAttachedSelected" cols="6" sm="6" md="6">
            <b-card border-variant="primary"
                    style="color: #007BFF"
                    footer-html="<p>Attached <br> Property</p>"
                    footer-bg-variant="white"
                    footer-border-variant="white">
              <b-icon-building font-scale="4.5"/>
            </b-card>
          </b-col>
          <b-col class="px-2" v-else cols="6" sm="6" md="6">
            <b-card @click="selectAttached"
                    footer-html="<p>Attached <br> Property</p>"
                    style="color: gray"
                    footer-bg-variant="white"
                    footer-border-variant="white">
              <b-icon-building font-scale="4.5"/>
            </b-card>
          </b-col>
          <b-col class="px-2" style="height: 100%" v-if="isDetachedSelected" cols="6" sm="6" md="6">
            <b-card border-variant="primary"
                    style="color: #007BFF"
                    footer-html="<p>Detached Property</p>"
                    footer-bg-variant="white"
                    footer-border-variant="white">
              <b-icon-house-door font-scale="4.5"/>
            </b-card>
          </b-col>
          <b-col class="px-2" v-else cols="6" sm="6" md="6">
            <b-card @click="selectDetached"
                    style="color: gray"
                    footer-bg-variant="white"
                    footer-html="<p>Detached Property</p>"
                    footer-border-variant="white">
              <b-icon-house-door font-scale="4.5"/>
            </b-card>
          </b-col>
        </b-row>
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
