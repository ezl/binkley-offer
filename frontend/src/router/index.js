import Vue from 'vue'
import Router from 'vue-router'
import Home from '../pages/Home'
import FixturesAndPersonalProperty from '../pages/FixturesAndPersonalProperty'
import OfferDetails from '../pages/OfferDetails'
import LegalMumboJumbo from '../pages/LegalMumboJumbo'
import ContactInfo from '../pages/ContactInfo'

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
