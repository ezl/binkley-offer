import Vue from 'vue'
import Router from 'vue-router'
import Home from '../pages/Home'
import FixturesAndPersonalProperty from '../pages/FixturesAndPersonalProperty'
import OfferDetails from '../pages/OfferDetails'
import LegalMumboJumbo from '../pages/LegalMumboJumbo'
import ContactInfo from '../pages/ContactInfo'
import ConfirmPropertyDetails from '../pages/ConfirmPropertyDetails'
import Settings from '../pages/Settings'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/confirm-details',
      name: 'ConfirmPropertyDetails',
      component: ConfirmPropertyDetails
    },
    {
      path: '/settings',
      name: 'Settings',
      component: Settings
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
