<template>
  <label>
    <b-form-group>
      <b-form-checkbox
        type="checkbox"
        v-model="valueAsData"
        @input="handleInput"
      >
      {{textLabelAsData}}
      </b-form-checkbox>
    </b-form-group>
  </label>
</template>

<script>

export default {
  name: 'CheckboxInput',
  props: {
    value: Boolean,
    textLabel: String
  },
  data () {
    return {
      valueAsData: this.value,
      textLabelAsData: this.textLabel
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
