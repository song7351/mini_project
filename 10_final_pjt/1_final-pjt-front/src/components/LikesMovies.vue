<template>
  <div>
    <h3>좋아요 많은 영화</h3>
    <p>많은 사람들이 좋아하는 영화를 알아보세요!</p>
    <VueSlickCarousel v-bind="settings" v-if="movies.length">
      <div v-for="movie in movies" v-bind:key="movie.id" class="movie-list">
        <SeasonMovieCard
          v-bind:title="movie.title"
          v-bind:posterPath="movie.poster_path"
          v-bind:releaseDate="movie.release_date"
          v-bind:movieId="movie.id"
        />
      </div>
    </VueSlickCarousel>
  
  </div>
</template>

<script>
import axios from "axios";
import SeasonMovieCard from "@/components/SeasonMovieCard.vue";
import VueSlickCarousel from "vue-slick-carousel";
import "vue-slick-carousel/dist/vue-slick-carousel.css";
import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";

export default {
  components: {
    SeasonMovieCard,
    VueSlickCarousel,
  },
  data(){
    return{
      movies:[],
      settings: {
        dots: true,
        infinite: true,
        slidesToShow: 9,
        slidesToScroll: 9,
        autoplay: true,
        autoplaySpeed: 2000,
        pauseOnDotsHover: true,
        pauseOnFocus: true,
        pauseOnHover: true,
      },
    }
  },
  created() {
    this.getManyLikeMovies();
  },
  computed: {},
  methods: {
    getManyLikeMovies() {
      const URL = "http://127.0.0.1:8000";
      axios({
        method: "get",
        url: `${URL}/api/v1/movies/`,
      })
        .then((res) => {
          this.movies = res.data.sort((a,b) => (b.like_users.length - a.like_users.length));
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
}
</script>

<style scoped>
.movie-list {
  margin-top: 20px;
  margin-bottom: 30px;
}


</style>