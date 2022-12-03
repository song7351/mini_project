<template>
<li v-on:click="deltitle(index)">{{title}}</li>
</template>

<script>
export default {
  name: "WatchListItem",
  props:["title", "index"],
  methods:{
    deltitle(index){
      this.$emit('deltitle', index)
    }
  }
}
</script>