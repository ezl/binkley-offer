<template>
  <label>
    <b-input-group prepend="$" size="md">
      <b-form-input
        v-model="valueAsData"
        @input="handleInput"
        :placeholder="textLabelAsData"></b-form-input>
    </b-input-group>
  </label>
</template>

<script>
export default {
  name: 'TextInputMoney',
  props: {
    value: String,
    textLabel: String
  },
  data () {
    return {
      valueAsData: this.value,
      textLabelAsData: this.textLabel || 'Details'
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
