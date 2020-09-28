<template>
    <b-form-group
      label-cols-sm="3"
      :label="textLabelAsData"
      label-align-sm="right"
    >
      <b-form-input
        v-model="valueAsData"
        @input="handleInput"></b-form-input>
    </b-form-group>
</template>

<script>
export default {
  name: 'FormGroupInput',
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
