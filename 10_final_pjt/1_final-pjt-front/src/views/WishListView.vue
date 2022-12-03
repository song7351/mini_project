<template>
  <div class="big_box">
    <h3>💜 {{ this.$store.state.username }}님이 찜한 영화 💜</h3>
  <div>
    <div class="overflow-auto">
      <!-- 찜한 영화가 있을때, 화면 -->
      <ul class="box" v-if="flag">
        <li v-for="perPageMovie in perPageMovies" v-bind:key="perPageMovie.id">
          <AllMovieCard class="card" v-bind:posterPath="perPageMovie.poster_path" 
            v-bind:movieId="perPageMovie.id"
          />
        </li>
      </ul>
      <!-- 찜한 영화가 없을때, 화면 -->
      <p v-else>찜한 영화가 없습니다.<br> 관심있는 영화에 좋아요를 눌러주세요 😊</p>

      <!-- 찜한 영화가 있을때, 화면-페이지네이션 -->
        <b-pagination v-if="flag" class="pagination"
        v-model="currentPage"
        :total-rows="rows"
        :per-page="perPage"
      ></b-pagination>
    </div>
  </div>
  </div>
</template>

<script>
import axios from "axios";
import AllMovieCard from '@/components/AllMovieCard';

export default {
  name: "WishList",
  components: { 
    AllMovieCard,
  },
     data(){
    return{
      flag: false,
      perPage:14,
      currentPage:1,
      movies: [],
    };
  },
  created(){
    this.getWishList()
    this.$store.dispatch('saveUserInfo', this.$store.state.token)
    this.isFlag()
  },
  computed:{
    perPageMovies() {
      const newMovies = this.movies.slice(
        this.perPage * this.currentPage - this.perPage,
        this.perPage * this.currentPage
      );
      return newMovies;
    },
    rows() {
      return this.movies.length;
    },
  },
  methods:{
    getWishList() {
      const URL = 'http://127.0.0.1:8000'
      axios({
        method: 'get',
        url: `${URL}/api/v1/movies/`,
      })
        .then((res) => {
          // 유저가 좋아요한 영화를 파악한다.
          const mymovies = res.data.filter(movie => movie.like_users.includes(this.$store.state.user_pk));
          this.movies = mymovies
        })
        .catch((err) => {
          console.log(err)
        })
    },
    isFlag() {
      const URL = 'http://127.0.0.1:8000'
      axios({
        method: 'get',
        url: `${URL}/api/v1/movies/`,
      })
        .then((res) => {
          // 유저가 좋아요한 영화를 파악한다.
          const mymovies = res.data.filter(movie => movie.like_users.includes(this.$store.state.user_pk));
          if(mymovies.length !== 0){
            this.flag = true
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
  }
}
</script>

<style scoped>
h3{margin-top:50px;}

.big_box{
  background-color: #ECEEFF;
  text-align: center;
}
p{
  margin-top:50px;
  margin-bottom: 70px;
}
.card {
  margin-bottom: 50px;
  padding:20px;
  border:0;
  background-color: #ECEEFF;
}
.box {
  display: grid;
  margin-top: 50px;
  width:100%;
  grid-template-columns: repeat(7, 1fr);
}
.pagination{
  display: flex;
  justify-content: center;
}
::v-deep .pagination  .page-link {
      background: rgb(221, 224, 255) ;
      color: black;
    }
::v-deep .pagination .active button{
      background: #a89be2;
      color: white;
      border: white;
    }

</style>