<template>
  <div id="app">
    <b-container>
      <router-view/>
    </b-container>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>

.title{
  font-size: 1.5rem;
  text-align: center;
  padding: 1rem;
}

.hyperlink-text{
  color: #86AEDB;
  cursor: pointer;
}
#app {
}
</style>
