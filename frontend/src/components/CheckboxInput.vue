<template>
  <b-form-group v-if="specialFieldAsData"
                label-cols-sm="3"
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
    specialField: Boolean
  },
  data () {
    return {
      valueAsData: this.value,
      textLabelAsData: this.textLabel,
      specialFieldAsData: this.specialField
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
