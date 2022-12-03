<template>
  <div>
    <h3 v-if="isLoggedIn">💜 {{ this.$store.state.username }}님의 Home 💜</h3>
    <h3 v-else>💜 Welcome To 112 Film 💜</h3>
    <a v-if="isLoggedIn" href="http://localhost:8080/wishlist"><img src="..\src\assets\112.png" height="150" class="logo_img"></a>
    <a v-else href="http://localhost:8080/login"><img src="..\src\assets\112.png" height="150" class="logo_img"></a>
    <br>
    <hr>
    <RecentMoviesVue />
    <br>
    <hr>
    <YourMoviesVue v-if="isLoggedIn && flag"/>
    <br v-if="isLoggedIn && flag">
    <hr v-if="isLoggedIn && flag">
    <LikesMoviesVue />
    <hr>
    <SeasonsMoviesVue />
    <br><br>
    <hr>
  </div>
</template>

<script>
import axios from "axios";
import YourMoviesVue from '@/components/YourMovies.vue';
import RecentMoviesVue from '@/components/RecentMovies.vue';
import LikesMoviesVue from '@/components/LikesMovies.vue';
import SeasonsMoviesVue from '@/components/SeasonsMovies.vue';

export default {
  components: { YourMoviesVue, RecentMoviesVue, LikesMoviesVue, SeasonsMoviesVue },
  data(){
    return{
      flag: false
    }
  },
  computed:{
    isLoggedIn() {
      return this.$store.getters.isLogin
    },
  },
  created() {
    this.$store.dispatch('saveUserInfo', this.$store.state.token)
    this.isFlag()
  },
  methods: {
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
};
</script>

<style scoped>

hr{
  margin-top: 40px;
  margin-bottom: 40px;
}


h3{
  margin-top: 50px;
  margin-bottom: 30px;
}

@keyframes logo112 {
	from {
		transform: translate(-200px, 0px);
	}
	to {
		transform: translate(0px,0px);
	}
}

.logo_img{
  animation: logo112 2s linear forwards;
  margin-bottom : 30px;
}
</style>