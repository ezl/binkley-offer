<template>
  <label>
    <b-input-group>
      <b-form-datepicker
        v-model="valueAsData"
        @input="handleInput"
        locale="en-US"
        :date-format-options="{ year: 'numeric', month: 'short', day: '2-digit', weekday: 'short' }"
        :placeholder="textLabelAsData"></b-form-datepicker>
    </b-input-group>
  </label>
</template>

<script>
export default {
  name: 'TextInputDate',
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
