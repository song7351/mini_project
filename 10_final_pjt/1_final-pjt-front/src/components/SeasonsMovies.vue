<template>
  <div>
    <h3>지금 봐야하는 영화</h3>
    <p>겨울에 온 가족과 볼 영화는?! ❄</p>
    <VueSlickCarousel v-bind="settings" v-if="seasonsmovies.length">
      <div
        v-for="movie in seasonsmovies"
        v-bind:key="movie.id"
        class="movie-list"
      >
        <SeasonMovieCard
          v-bind:posterPath="movie.poster_path"
          v-bind:movieId="movie.id"
          v-bind:title="movie.title"
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
  data() {
    return {
      seasonsmovies: [],
      settings: {
        dots: true,
        infinite: true,
        slidesToShow: 9,
        slidesToScroll: 3,
        autoplay: true,
        autoplaySpeed: 2000,
        pauseOnDotsHover: true,
        pauseOnFocus: true,
        pauseOnHover: true,
      },
    };
  },
  created() {
    this.getSeasonMovies();
  },
  computed: {},
  methods: {
    getSeasonMovies() {
      const URL = "http://127.0.0.1:8000";
      axios({
        method: "get",
        url: `${URL}/api/v1/movies/`,
      })
        .then((res) => {
          this.seasonsmovies = res.data.filter(
            (movie) => movie.season === "겨울" || movie.genres[0] === 10751
          );
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style scoped>
* {
  box-sizing: border-box;
}

h3 {
  margin-top: 30px;
}
.slider {
  width: 100vw;
  text-align: center;
  border-radius: 10px;
  overflow: hidden;
}

.slides {
  display: flex;
  overflow: auto;
}
.slides::-webkit-scrollbar {
  height: 10px;
}
.slides::-webkit-scrollbar-thumb {
  background: #02010150;
  border-radius: 10px;
}
.slides::-webkit-scrollbar-track {
  background-color: white;
}
.slides > div {
  scroll-snap-align: start;
  flex-shrink: 0;
  margin-right: 30px;
  scroll-padding-right: 20px;
  border-radius: 10px;
  overflow: hidden;
}

.movie-list {
  margin-top: 20px;
  margin-bottom: 30px;
}
</style>
