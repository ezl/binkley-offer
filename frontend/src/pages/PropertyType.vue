<template>
  <div>
    <H1 class="title">Select Property Type</H1>
    <p class="text-center">
      Before we start, what type of property are you writing a contract for?
    </p>
    <section id="propertyTypeChoices">
      <b-row class="text-center">
        <b-col cols=12 md=6 offset-md=3>
          <b-card-group deck class="justify-content-center">

            <b-card
                @click="selectAttached"
                :class="{selectedCard: isAttachedSelected}"
            >
              <b-card-text class="mb-2">
                <b-icon-building font-scale="2.5"/>
              </b-card-text>
              <b-card-text>Attached Single</b-card-text>
            </b-card>

            <b-card
                @click="selectDetached"
                :class="{selectedCard: isDetachedSelected}"
            >
              <b-card-text class="mb-2">
                <b-icon-house-door font-scale="2.5"/>
              </b-card-text>
              <b-card-text>Detached Single</b-card-text>
            </b-card>
          </b-card-group>
        </b-col>
      </b-row>

      <b-row class="text-center mt-3 helpText">
        <b-col>
          <p v-if="isDetachedSelected">For use with single family homes, fee simple townhomes, or shared community
            associations</p>
          <p v-if="isAttachedSelected">For use with condos, including condo townhomes and commercial condos</p>
          <p v-if="!(isAttachedSelected || isDetachedSelected)"
             class="Super Hacky Way To Maintain Same Whitespace When Neither Option Is Selected BAD BAD BAD Eric">
            &nbsp;</p>
        </b-col>
      </b-row>

      <b-row class="text-center mt-3">
        <b-col>
          <b-button variant="primary" :disabled="!(isAttachedSelected || isDetachedSelected)" class="btn"
                    @click="getStarted()"> Get Started
          </b-button>
        </b-col>
      </b-row>
      <br>
      <b-row class="text-center mt-3">
        <b-col>
          <b-button variant="primary" class="btn" @click="createAccount()">Create an Account</b-button>
        </b-col>
        <b-col>
          <b-button variant="primary" class="btn" @click="loginAccount()">Login</b-button>
        </b-col>
      </b-row>
    </section>
  </div>
</template>

<script>

import ArrowRightCircle from '../components/icons/ArrowRightCircle'
import LoggedUser from '../models/LoggedUser'

export default {
  name: 'PropertyType',
  metaInfo: {
    meta: [
      {charset: 'utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1'}
    ]
  },
  components: {
    ArrowRightCircle
  },
  data () {
    return {
      isAttachedSelected: false,
      isDetachedSelected: false,
      loggedUserDetails: new LoggedUser()
    }
  },
  mounted () {
    this.loggedUserDetails = Object.assign(new LoggedUser(), JSON.parse(localStorage.loggedUserDetails))
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
    },
    createAccount () {
      this.$router.push({name: 'Register'})
    },
    loginAccount () {
      this.$router.push({name: 'Login'})
    }
  }
}
</script>

<style scoped>

.card-deck {
  /* overwrite the responsive thing that makes cards tile vertically on small viewports */
  display: flex;
  flex-wrap: wrap;
}

.card {
  margin: 5px;
  cursor: pointer;
  color: rgba(0, 0, 0, .4);
  border-color: 1px solid rgba(0, 0, 0, .4);
}

@media (min-width: 576px) {
  .card {
    margin: 15px;
  }
}

.card.selectedCard {
  color: #007BFF;
  background-color: rgba(233, 243, 255, 0.5);
  border-color: #007bff;
}

.helpText {
  color: rgba(0, 0, 0, .4);
  font-size: 0.8em;
  font-style: italic;
}
</style>
