<template>
  <div>
    <h1>WatchListView</h1>
    <WatchListForm v-on:searching="searching"/>
    <ul>
      <!-- <li v-for="(title, index) in titles" :key="index">{{ title }}</li> -->
      <WatchListItem v-for="(title, index) in titles" :key="index" v-bind:title="title" v-bind:index="index" v-on:deltitle="deltitle"/>
    </ul>
  </div>
</template>

<script>
import WatchListForm from "../components/watchListView/WatchListFormView.vue";
import WatchListItem from "../components/watchListView/WatchListItemView.vue";

export default {
  
  components:{
    WatchListForm,
    WatchListItem
  },
  data(){
    return{
      titles:[],
    }
  },
  methods:{
   searching(title) {
      this.titles.push(title)
    },
    deltitle(index){
      this.titles.splice(index,1);
    }
  }
}
</script>
