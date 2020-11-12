import Vue from 'vue'
import Router from 'vue-router'
import FixturesAndPersonalProperty from '../pages/FixturesAndPersonalProperty'
import OfferDetails from '../pages/OfferDetails'
import LegalMumboJumbo from '../pages/LegalMumboJumbo'
import ContactInfo from '../pages/ContactInfo'
import ConfirmPropertyDetails from '../pages/ConfirmPropertyDetails'
import Settings from '../pages/Settings'
import Done from '../pages/Done'
import PropertyType from '../pages/PropertyType'
import Search from '../pages/Search'
import BuyerAndSeller from '../pages/BuyerAndSeller'
import Register from '../pages/Register'
import Home from '../pages/Home'
import Login from '../pages/Login'
import ParkingAndStorage from '../pages/ParkingAndStorage'

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
      path: '/property-type',
      name: 'PropertyType',
      component: PropertyType
    },
    {
      path: '/search',
      name: 'Search',
      component: Search
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
      path: '/buyer-and-seller',
      name: 'BuyerAndSeller',
      component: BuyerAndSeller
    },
    {
      path: '/first-step',
      name: 'FixturesAndPersonalProperty',
      component: FixturesAndPersonalProperty
    },
    {
      path: '/second-step',
      name: 'ParkingAndStorage',
      component: ParkingAndStorage
    },
    {
      path: '/third-step',
      name: 'OfferDetails',
      component: OfferDetails
    },
    {
      path: '/fourth-step',
      name: 'LegalMumboJumbo',
      component: LegalMumboJumbo
    },
    {
      path: '/fifth-step',
      name: 'ContactInfo',
      component: ContactInfo
    },
    {
      path: '/done',
      name: 'Done',
      component: Done
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    }
  ],
  scrollBehavior (to, from, savedPosition) {
    return {x: 0, y: 0}
  }
})
