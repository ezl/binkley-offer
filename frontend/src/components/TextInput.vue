<template>
  <label>
    <b-form-group>
      <span v-if="titleAsData"> {{ titleAsData }}</span>
      <b-form-input
        type="text"
        v-model="valueAsData"
        @input="handleInput"
        :placeholder="textLabelAsData"
      />
    </b-form-group>
  </label>
</template>

<script>
export default {
  name: 'TextInput',
  props: {
    value: String,
    textLabel: String,
    title: String
  },
  data () {
    return {
      valueAsData: this.value,
      titleAsData: this.title,
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
