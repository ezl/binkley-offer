<template>
  <b-form-group v-if="specialFieldAsData"
                label-cols-sm="3"
                :label="titleAsData"
                label-align-sm="right">
    <b-form-input
      type="text"
      v-model="valueAsData"
      @input="handleInput"
      :placeholder="textLabelAsData"
    />
  </b-form-group>
  <b-form-input v-else
                type="text"
                v-model="valueAsData"
                @input="handleInput"
                :placeholder="textLabelAsData"
  />
</template>

<script>
export default {
  name: 'TextInput',
  props: {
    value: String,
    textLabel: String,
    title: String,
    specialField: Boolean
  },
  data () {
    return {
      valueAsData: this.value,
      titleAsData: this.title,
      textLabelAsData: this.textLabel || 'Details',
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
