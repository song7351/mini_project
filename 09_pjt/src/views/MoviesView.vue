<template>
  <div>
    <!-- Moviecard -->
    <div class="container">
      <div class="movieCard" v-for="(movie, index) in movies" :key="index" >
          <MovieCard :movie="movie"/>
        <!-- <div>
          <img :src="posterImg(movie.poster_path)" alt="">
          <h5>{{movie.title}}</h5>
          <p>{{movie.overview}}</p>
        </div> -->
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import MovieCard from "../components/movieView/MovieCardView.vue"

export default {
  data(){
    return{
      movies:[
      ]
    }
  },
 created(){
    this.getTopRate()
  },
  methods: {
    // posterImg(poster_path){
    //   const url = "https://image.tmdb.org/t/p/original"+poster_path
    //   return url
    // },
    async getTopRate() {
      const API_KEY = process.env.VUE_APP_TMDB_API_KEY;
      const API_URL = process.env.VUE_APP_TOPRATE_API_URL;
      try {
        const response = await axios.get(API_URL, {
          params: {
            api_key: API_KEY,
            language: "ko-KR",
            // page: 1,
          },
        });
        // console.log(response.data.items[0].id.videoId);
        // console.log(response.data.results[0].title);
        this.movies = response.data.results
      } catch (error) {
        console.log(error);
      }
    },
  },
  components:{
    MovieCard
  }
}
</script>

<style>
.container{
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  row-gap: 50px;
}
</style>
