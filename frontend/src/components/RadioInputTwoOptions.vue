<template>
  <b-form-group>
    <b-row>
      <b-col>
        {{itemOneLabelAsData}}
        <b-form-radio v-model="itemAsData.first" value=true @change="handleInputOne">
        </b-form-radio>
      </b-col>
      <b-col>
        {{itemTwoLabelAsData}}
        <b-form-radio v-model="itemAsData.second" value=true @change="handleInputTwo">
        </b-form-radio>
      </b-col>
    </b-row>
  </b-form-group>
</template>

<script>
export default {
  name: 'RadioInputTwoOptions',
  props: {
    itemOneLabel: String,
    itemTwoLabel: String,
    item: {
      first: false,
      second: false
    }
  },
  data () {
    return {
      itemOneLabelAsData: this.itemOneLabel,
      itemTwoLabelAsData: this.itemTwoLabel,
      itemAsData: this.item
    }
  },
  methods: {
    handleInputOne () {
      this.itemAsData.first = true
      this.itemAsData.second = false
      this.$emit('input', this.itemAsData)
    },
    handleInputTwo () {
      this.itemAsData.first = false
      this.itemAsData.second = true
      this.$emit('input', this.itemAsData)
    }
  }
}
</script>

<style scoped>

</style>
