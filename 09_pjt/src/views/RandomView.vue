<template>
  <div class="randomView">
    <h1>Random View</h1>
    <b-button variant="success" v-on:click="getRandom">PICK</b-button>
    <div class=container>
      <div>
          <b-card
    :img-src="imgsrc"
    img-alt="Image"
    img-top
    style="width: 20rem; height: 650px;"
    class="mb-2"
  >
  <b-card-title style="overflow: hidden; text-overflow: ellipsis;  display: block;   display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;">
    {{ movie.title }}
  </b-card-title>
    <b-card-text style="overflow: hidden; text-overflow: ellipsis;  display: block;   display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;">
      {{ movie.overview }}
    </b-card-text>
  </b-card>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import _ from "lodash";

export default {
  data(){
    return{
      movie:[
      ],
      imgsrc:'',
    }
  },
 created(){
    this.getRandom()
  },
  methods: {
    // posterImg(poster_path){
    //   const url = "https://image.tmdb.org/t/p/original"+poster_path
    //   return url
    // },
    async getRandom() {
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
        this.movie = _.sample(response.data.results)
        this.imgsrc = "https://image.tmdb.org/t/p/original" + this.movie.poster_path
        if(this.movie.overview === ""){
          this.movie.overview = "줄거리가 없습니다."
        }
        // console.log(this.movie)

      } catch (error) {
        console.log(error);
      }
    },
  },

}
</script>

<style scoped>
.randomView{
  text-align: center;
}
.randomView button{
  margin: 20px 0px;
  width: 318px;
}
.container{
  display: flex;
  justify-content: center;
}
.card-img-top{
  height: 477px;
}
</style>