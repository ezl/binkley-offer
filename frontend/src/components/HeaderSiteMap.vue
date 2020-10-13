<template>
  <b-row>
    <div v-for="(item) in siteMapAsData"
         :key="item.pageUrl">
      <button class="btn" :style="{color: item.color}" @click="navigate(item.pageUrl)" :disabled="item.isDisabled">
        {{ item.displayName }}
      </button>
    </div>
  </b-row>
</template>

<script>
export default {
  name: 'HeaderSiteMap',
  props: {
    siteMap: Array
  },
  data () {
    return {
      siteMapAsData: this.siteMap
    }
  },
  methods: {
    navigate: function (goToPage) {
      this.$router.push({name: goToPage})
    }
  }
}
</script>

<style scoped>

</style>
