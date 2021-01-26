<template>
  <b-form-textarea
      v-model="valueAsData"
      placeholder="Enter something..."
      @input="handleInput"
      rows="3"
      max-rows="6"
  ></b-form-textarea>
</template>

<script>
export default {
  name: 'TextAreaInput',
  props: {
    value: String
  },
  beforeDestroy () {
    this.$emit('input', null)
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
