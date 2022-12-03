<template>
    <div>
      <h2>보고싶은 영화</h2>
      <div>
        <input type="text" v-model="searchWords">
        <button v-on:click="searching">Add</button>
      </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
  name: "WatchListForm",
  data(){
    return{
      searchWords:'',
    }
  },
  methods:{
    async searching(){
      if(this.searchWords === ""){
        alert("검색어를 입력해주세요.")
      }else{
      const API_KEY = process.env.VUE_APP_TMDB_API_KEY;
      const API_URL = process.env.VUE_APP_SEARCH_API_URL;
      try {
        const response = await axios.get(API_URL, {
          params: {
            api_key: API_KEY,
            language: "ko-KR",
            query: this.searchWords,
            // page: 1,
          },
        });
        // console.log(response.data.items[0].id.videoId);
        console.log(response.data.results);
        if(response.data.results.length === 0){
          alert("검색결과가 없습니다.")
          this.searchWords = ''
        }else{
          let title = response.data.results[0].title
          this.$emit('searching', title)
          this.searchWords = ''
        }
      } catch (error) {
        console.log(error);
      }
      }
    }
  }
}
</script>
