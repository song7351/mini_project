<template>
  <b-card
    :img-src="posterImg(movie.poster_path)"
    img-alt="Image"
    img-top
    style="width: 20rem; height: 650px;"
    class="mb-2"
  >
  <b-card-title style="overflow: hidden; text-overflow: ellipsis;  display: block;   display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;">
    {{movie.title}}
  </b-card-title>
    <b-card-text style="overflow: hidden; text-overflow: ellipsis;  display: block;   display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;">
      {{movie.overview}}
    </b-card-text>
  </b-card>
</template>

<script>

export default {
  name: "MovieCard",
  props:['movie'],
  methods: {
    posterImg(poster_path){
      const url = "https://image.tmdb.org/t/p/original"+poster_path
      return url
    },
  }
}
</script>

<style scoped>
.card-img-top{
  height: 477px;
}
</style>
