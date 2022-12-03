<template>
  <div>
    <router-link :to="{ name: 'moviedetail', params: { id: movieId } }">
      <img v-bind:src="movieImgURL" alt="movieImg" height="300" />
      <div class="title">{{title}}</div>
    </router-link>
  </div>
</template>

<script>
export default {
  props: ["posterPath", "movieId", "title"],
  computed: {
    movieImgURL() {
      return `https://themoviedb.org/t/p/w600_and_h900_bestv2${this.posterPath}`;
    }
  }
}
</script>

<style scoped>
.movie-list div a{
  text-decoration: none;
  color: black;
}

.movie-list div a img {
  transition: all 0.2s linear;
}

.movie-list div a:hover img{
  transform: scale(1.2);
}


</style>