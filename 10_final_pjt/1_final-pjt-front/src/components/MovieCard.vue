<template>
  <div>
    <img v-bind:src="movieImgURL" alt="movieImg" height="300" />
    <div class="title">{{title}}</div>
    <div class="overview">{{overview}}</div>
    <div class="releasedate">{{releaseDate}}</div>
  </div>
</template>

<script>
export default {
  props: ["title", "posterPath", "overview", "releaseDate"],

  computed: {
    movieImgURL() {
      return `https://themoviedb.org/t/p/w600_and_h900_bestv2${this.posterPath}`;
    }
  }
}
</script>

<style>
.title{
  margin-top:10px;
}

</style>