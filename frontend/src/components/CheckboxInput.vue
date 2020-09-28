<template>
  <label>
    <b-form-group>
      <template slot="label">{{textLabelAsData}}</template>
      <b-form-checkbox
        type="checkbox"
        v-model="valueAsData"
        @input="handleInput"
      />
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
