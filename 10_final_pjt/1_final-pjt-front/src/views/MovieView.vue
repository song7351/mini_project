<template>
  <div class="big_box">
    <h3>💜 112 Film의 전체영화 💜</h3>
  <div>
    <!-- 영화 검색창 -->
    <b-form-input placeholder="보고싶은 영화를 검색해보세요" size="md" v-model="searchWord" class="search-movie"></b-form-input>
    <!-- 영화 검색 버튼 -->
    <button v-on:click="searching(true)" class="search">&#128269;</button>
    <!-- 영화 검색 초기화 버튼 -->
    <button v-on:click="searching(false)" class="clear">&#128260;</button>
    
    <div class="overflow-auto">
      <ul class="box">
        <li v-for="perPageMovie in perPageMovies" v-bind:key="perPageMovie.id">
          <AllMovieCard class="card" v-bind:posterPath="perPageMovie.poster_path" 
            v-bind:movieId="perPageMovie.id"
          />
        </li>
      </ul>
        <b-pagination class="pagination"
        v-model="currentPage"
        :total-rows="rows"
        :per-page="perPage"
      ></b-pagination>
    </div>
  </div>
  </div>
</template>

<script>
import Swal from "sweetalert2";
import AllMovieCard from '@/components/AllMovieCard';

export default {
  name: "MovieView",
  components: { 
    AllMovieCard,
  },

  data() {
    return {
      searchWord:'',
      perPage:14,
      currentPage:1,
      movies: [],
    }
  },

  computed: {
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

  created() {
    this.$store.dispatch("getMovies")
    this.getMovies()
  },
  methods: {
      getMovies() {
        this.movies = this.$store.state.movies;
      },
      searching(flag){
        if(!flag){
          this.searchWord = ''
        }
        var tmp = this.$store.state.movies.filter(movie => movie.title.includes(this.searchWord))
        if(tmp.length === 0){
          this.movies = this.$store.state.movies;
          Swal.fire("검색 결과가 없습니다.")
        }else{
          this.movies = tmp
        }
      }
    }
}
</script>


<style scoped>
h3{margin-top:50px; margin-bottom:30px;}

.big_box{
  background-color: #ECEEFF;
  text-align: center;
}

.search-movie{
  display: inline-block;
  width:400px;
  margin-bottom: 10px;
  margin-right: 5px;
  margin-left: 60px;
}

button{
  font-size: 20px;
}

.search{
  border:none;
}

.clear{
  border:none;
}

.card {
  margin-bottom: 50px;
  padding:20px;
  background-color: #ECEEFF;
  font-size: 0;
  border:0;
}

.card a {
  width:auto;
  padding:0px;
  margin:0px;
  background-color: #fff;

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

#swal2-title {
  color:rgb(75, 82, 92);
  background-color:rgb(180, 212, 240);
  margin: 20px;
  padding: 20px;
}
</style>