<template>
  <b-form-group
    label-cols-sm="3"
    :label="titleAsData"
    label-align-sm="right">
    <b-input-group>
      <b-form-datepicker v-if="disableWeekendsAsData"
          v-model="valueAsData"
          @input="handleInput"
          locale="en-US"
          :date-disabled-fn="dateDisabled"
          :date-format-options="{ year: 'numeric', month: 'short', day: '2-digit', weekday: 'short' }"
          :placeholder="textLabelAsData"></b-form-datepicker>
      <b-form-datepicker v-else
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
    title: String,
    disableWeekends: Boolean
  },
  data () {
    return {
      valueAsData: this.value,
      textLabelAsData: this.textLabel || 'Details',
      titleAsData: this.title,
      disableWeekendsAsData: this.disableWeekends
    }
  },
  beforeDestroy () {
    this.$emit('input', null)
  },
  methods: {
    handleInput (event) {
      this.$emit('input', event)
    },
    dateDisabled (ymd, date) {
      const weekday = date.getDay()
      return weekday === 0 || weekday === 6
    }
  }
}
</script>

<style scoped>

</style>
