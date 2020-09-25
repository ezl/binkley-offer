import Vue from 'vue'
import Router from 'vue-router'
import Home from '../components/Home'
import FixturesAndPersonalProperty from '../components/FixturesAndPersonalProperty'
import OfferDetails from '../components/OfferDetails'
import LegalMumboJumbo from '../components/LegalMumboJumbo'
import ContactInfo from '../components/ContactInfo'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/first-step',
      name: 'FixturesAndPersonalProperty',
      component: FixturesAndPersonalProperty
    },
    {
      path: '/second-step',
      name: 'OfferDetails',
      component: OfferDetails
    },
    {
      path: '/third-step',
      name: 'LegalMumboJumbo',
      component: LegalMumboJumbo
    },
    {
      path: '/fourth-step',
      name: 'ContactInfo',
      component: ContactInfo
    }
  ]
})
