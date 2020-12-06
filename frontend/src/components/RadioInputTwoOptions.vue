<template>
  <b-form-group v-if="specialFieldAsData"
                label-cols-sm="3"
                label-align-sm="right"
                :label="textLabelAsData">
    <b-row class="mt-2" align-v="baseline">
      <b-col>
        <b-form-radio v-model="itemAsData.first" value=true @change="handleInputOne">
          {{ itemOneLabelAsData }}
        </b-form-radio>
      </b-col>
      <b-col>
      <b-form-radio v-model="itemAsData.second" value=true @change="handleInputTwo">
        {{ itemTwoLabelAsData }}
      </b-form-radio>
      </b-col>
      <b-col/>
      <b-col/>
    </b-row>
  </b-form-group>
  <b-form-group v-else>
    <b-row>
      <b-col>
        <b-form-radio v-model="itemAsData.first" value=true @change="handleInputOne">
          {{ itemOneLabelAsData }}
        </b-form-radio>
      </b-col>
      <b-col>
        <b-form-radio v-model="itemAsData.second" value=true @change="handleInputTwo">
          {{ itemTwoLabelAsData }}
        </b-form-radio>
      </b-col>
    </b-row>
  </b-form-group>
</template>

<script>
export default {
  name: 'RadioInputTwoOptions',
  props: {
    itemOneLabel: String,
    itemTwoLabel: String,
    specialField: Boolean,
    textLabel: String,
    item: {
      first: false,
      second: false
    }
  },
  data () {
    return {
      itemOneLabelAsData: this.itemOneLabel,
      itemTwoLabelAsData: this.itemTwoLabel,
      itemAsData: this.item,
      specialFieldAsData: this.specialField,
      textLabelAsData: this.textLabel
    }
  },
  beforeDestroy () {
    this.itemAsData.first = false
    this.itemAsData.second = false
    this.$emit('input', this.itemAsData)
  },
  methods: {
    handleInputOne () {
      this.itemAsData.first = true
      this.itemAsData.second = false
      this.$emit('input', this.itemAsData)
    },
    handleInputTwo () {
      this.itemAsData.first = false
      this.itemAsData.second = true
      this.$emit('input', this.itemAsData)
    }
  }
}
</script>

<style scoped>

</style>
