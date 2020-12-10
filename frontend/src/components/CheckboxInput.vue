<template>
  <b-form-group v-if="specialFieldAsData"
                label-cols-sm="3"
                :label="titleAsData"
                label-align-sm="right">
    <b-form-checkbox
      type="checkbox"
      v-model="valueAsData"
      @input="handleInput"
    >
      {{ textLabelAsData }}
    </b-form-checkbox>
  </b-form-group>
  <b-form-group v-else>
    <b-form-checkbox
      type="checkbox"
      v-model="valueAsData"
      @input="handleInput"
    >
      {{ textLabelAsData }}
    </b-form-checkbox>
  </b-form-group>
</template>

<script>

export default {
  name: 'CheckboxInput',
  props: {
    value: Boolean,
    textLabel: String,
    specialField: Boolean,
    title: String
  },
  data () {
    return {
      valueAsData: this.value,
      textLabelAsData: this.textLabel,
      specialFieldAsData: this.specialField,
      titleAsData: this.title
    }
  },
  beforeDestroy () {
    this.$emit('input', false)
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
