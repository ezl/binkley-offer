<template>
  <label>
    <b-input
      type="text"
      v-model="valueAsData"
      @input="handleInput"
    />
  </label>
</template>

<script>
export default {
  name: 'TextInput',
  props: {
    value: String
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
