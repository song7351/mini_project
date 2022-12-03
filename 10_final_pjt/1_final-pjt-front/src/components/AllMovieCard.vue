<template>
  <div>
    <router-link :to="{ name: 'moviedetail', params: { id: movieId } }">
        <img v-bind:src="movieImgURL" alt="movieImg" height="300" />
    </router-link>
  </div>
</template>

<script>
export default {
  props: ["posterPath", "movieId"],
  computed: {
    movieImgURL() {
      return `https://themoviedb.org/t/p/w600_and_h900_bestv2${this.posterPath}`;
    }
  }
}
</script>

<style scoped>
a img{
  width:100%;
  height:auto;
  transition: all 0.1s linear;
}

a:hover img{
  transform: scale(1.1);
  border-radius: 10px;
  border: 4px solid #818ac0;
}
</style>