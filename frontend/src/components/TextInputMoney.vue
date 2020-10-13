<template>
  <b-form-group
    label-cols-sm="3"
    :label="titleAsData"
    label-align-sm="right">
    <b-input-group :prepend="prependAsData" size="md">
      <b-form-input
        v-model="valueAsData"
        @input="handleInput"
        :placeholder="textLabelAsData"></b-form-input>
    </b-input-group>
  </b-form-group>
</template>

<script>
export default {
  name: 'TextInputMoney',
  props: {
    value: String,
    textLabel: String,
    prepend: String,
    title: String
  },
  data () {
    return {
      valueAsData: this.value,
      textLabelAsData: this.textLabel || 'Details',
      prependAsData: this.prepend,
      titleAsData: this.title
    }
  },
  methods: {
    handleInput (event) {
      this.$emit('input', event)
    }
  }
}
</script>

<style scoped>

</style>
