<template>
  <label>
    <b-form-checkbox
      type="checkbox"
      v-model="valueAsData"
      @input="handleInput"
    />
  </label>
</template>

<script>

export default {
  name: 'CheckboxInput',
  props: {
    value: Boolean
  },
  data () {
    return {
      valueAsData: this.value
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
