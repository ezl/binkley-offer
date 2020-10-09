<template>
  <b-form-group
      label-cols-sm="3"
      :label="titleAsData"
      label-align-sm="right">
    <b-input-group>
      <b-form-datepicker
          v-model="valueAsData"
          @input="handleInput"
          locale="en-US"
          :date-format-options="{ year: 'numeric', month: 'short', day: '2-digit', weekday: 'short' }"
          :placeholder="textLabelAsData"></b-form-datepicker>
    </b-input-group>
  </b-form-group>
</template>

<script>
export default {
  name: 'TextInputDate',
  props: {
    value: String,
    textLabel: String,
    title: String
  },
  data () {
    return {
      valueAsData: this.value,
      textLabelAsData: this.textLabel || 'Details',
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
