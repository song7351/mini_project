<template>
  <div>
    <!-- 영화상세정보 폼 -->
    <div class="detailwrap">
      <img v-bind:src="movieImgURL" alt="movieImg" />
      <div class="card-container">
        <h2 class="text-pad"> {{ movie?.title }} </h2>
        <ul class="inforwrap">
          <li class="text-pad">개봉일자: {{ movie?.release_date }}</li>
          <li class="text-pad">평점: {{ movie?.vote_average }}</li>
          <li class="text-pad">유저평점: {{ total_vote }}</li>
          <li v-if="movieLikeFlag && isLoggedIn" class="text-pad-color">
            <div
              v-on:click="likeMovie(movie?.id)"
            >💖</div>
          </li>
          <li v-if="!movieLikeFlag && isLoggedIn" class="text-pad">
            <div v-on:click="likeMovie(movie?.id)">🤍</div>
          </li>
          <li v-if="!isLoggedIn" class="text-pad">
            <div v-on:click="needLogin()">🤍</div>
          </li>
          <li><b-button pill v-on:click="goYoutube" size="sm">예고편</b-button></li>
        </ul>
        <p class="overview">{{ movie?.overview }}</p>
      </div>
    </div>

    <!-- 댓글입력 폼 -->
    <div class="reviewSet" v-if="isLoggedIn">
      <b-form-spinbutton id="sb-inline" v-model="user_vote_average" min="0" max="5" step="1" inline></b-form-spinbutton>

      <b-col sm="10">
        <b-form-input
          v-model="content"
          placeholder="평점과 댓글을 입력해주세요."
          class="review-form"
        ></b-form-input>
      </b-col>
      <b-button variant="outline-secondary" v-on:click="createReview"
        >등록</b-button>
    </div>
    <div class="reviewSet" v-if="!isLoggedIn">
      <a><b-form-spinbutton id="sb-inline" v-model="user_vote_average" v-on:click="needLogin()" inline readonly></b-form-spinbutton></a>

      <b-col sm="10">
        <b-form-input
          readonly
          v-model="content"
          placeholder="로그인이 필요한 기능입니다."
          class="review-form"
        ></b-form-input>

      </b-col>
      <b-button variant="outline-secondary" v-on:click="needLogin()"
        >등록</b-button
      >
    </div>

    <!-- 댓글 리뷰리스트 폼 -->
    <b-list-group class="reviewList">
      <ReviewItem
        class="review"
        v-for="(review, index) in reviews"
        v-bind:key="index"
        v-bind:review="review"
      />
    </b-list-group>
  </div>
</template>

<script>
import axios from "axios";
import Swal from "sweetalert2";
import ReviewItem from "@/components/ReviewItem.vue";

const API_URL = "http://127.0.0.1:8000";

export default {
  components: {
    ReviewItem,
  },
  data() {
    return {
      value: 0,
      movie: null,
      user_vote_average: 0,
      content: "",
      reviews: null,
      movieLikeFlag: false,
    };
  },
  created() {
    this.getMovieDetail();
    this.getMovieReviews();
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLogin;
    },
    movieImgURL() {
      const url =
        "https://themoviedb.org/t/p/w600_and_h900_bestv2" +
        this.movie?.poster_path;
      return url;
    },
    total_vote() {
      const n = this.reviews?.length;
      let sum_vote = 0;
      if (n === 0) {
        return 0;
      }
      this.reviews?.forEach((review) => {
        sum_vote = sum_vote + review.user_vote_average;
      });
      const result = (sum_vote / n).toFixed(1);
      return result;
    },
  },
  methods: {
    needLogin() {
      Swal.fire("로그인이 필요한 기능입니다.");
    },
    chgUpdate() {
      this.flag = !this.flag;
    },
    likeMovie(movie_pk) {
      axios({
        method: "post",
        url: `${API_URL}/api/v1/movies/${movie_pk}/likes/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          this.movieLikeFlag = !this.movieLikeFlag;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    checkUser(username) {
      if (username === this.$store.state.username) {
        return true;
      }
      return false;
    },
    getMovieReviews() {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/reviews/`,
      })
        .then((res) => {
          const tmp = res.data.filter(
            (review) => review.movie.id == this.$route.params.id
          );
          this.reviews = tmp;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getMovieDetail() {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/${this.$route.params.id}/`,
      })
        .then((res) => {
          this.movie = res.data;
          if (this.movie.like_users.includes(this.$store.state.user_pk)) {
            this.movieLikeFlag = true;
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    async goYoutube() {
      // const API_KEY = process.env.VUE_APP_TMDB_API_KEY;
      const API_KEY = "d77a958e646191ffe9107d07477129e7";
      const API_URL =
        "https://api.themoviedb.org/3/movie/" +
        this.movie?.movie_id +
        "/videos";
      let key = "";
      try {
        const response = await axios.get(API_URL, {
          params: {
            api_key: API_KEY,
            language: "ko-KR",
          },
        });
        key = response.data.results[0].key;
        // console.log(key)
      } catch (error) {
        console.log(error);
      }
      if (key) {
        const link = "https://youtube.com/embed/" + key;
        window.open(link);
      } else {
        Swal.fire("예고편 동영상이 없습니다.");
      }
    },
    async createReview() {
      if (this.content === "") {
        Swal.fire("내용을 입력해주세요.");
        return;
      } else if (this.user_vote_average < 0 || this.user_vote_average > 5) {
        Swal.fire("평점 범위가 벗어났습니다.");
        return;
      }
      axios({
        method: "post",
        url: `${API_URL}/api/v1/movies/${this.$route.params.id}/comments/`,
        data: {
          user_vote_average: this.user_vote_average,
          content: this.content,
          movie: this.$route.params.id,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          this.user_vote_average = 0;
          this.content = "";
          this.$router.go();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    delReview(review_pk) {
      axios({
        method: "DELETE",
        url: `${API_URL}/api/v1/reviews/${review_pk}/`,
      })
        .then(() => {
          this.$router.go();
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style>
.detailwrap {
  margin-top: 30px;
  display: flex;
  justify-content: center;
  background-color: #eceeff;
}
.detailwrap img {
  height: 500px;
  padding: 20px;
  margin-left: 100px;
}
.inforwrap {
  display: flex;
  padding: 10px;
}
.text-pad {
  text-align: left;
  padding-right: 20px;
  font-weight: bold;
  margin-top:4px;
}

.text-pad-color {
  text-align: left;
  padding-right: 20px;
  font-weight: bold;
  color: red;
  margin-top:4px;
}

.overview {
  text-align: left;
  margin-right: 110px;
}

.form-btn {
  width: 40px;
}
.reviewSet {
  display: flex;
  justify-content: center;
  background-color: white;
}

.card-container {
  margin-top: 30px;
  width: 80vw;
  padding: 30px;
  align-items: center;
}
.reviewList {
  margin-top: 30px;
  margin-left: 10%;
  margin-right: 10%;
}

.review {
  display: flex;
}
.content-form {
  border: 1px solid;
  border-radius: 10px;
  border-color: grey;
  align-items: center;
}

.review-list {
  background-color: #fff;
  padding: 0px;
}

.review-list li {
  background-color: #fff;
}

.username {
  font-weight: bold;
}

.review-data {
  font-size: small;
  margin-bottom: 15px;
}

.reviewSet {
  background-color: #eceeff;
  padding: 0 100px 0 100px;
}


.form-control{
  display: inline-block;
  width:500px;
}

bdi{
  background-color: #fff;
}

.vote-average {
  font-weight: bold;
  font-size: 20px;
  border-radius: 8px;
  color: #727272;
  border: solid 1px #afafaf;
  background-color: #fff;
}

.deletebtn {
  margin-left: 3px;
}

#swal2-title {
  color: rgb(75, 82, 92);
  background-color: rgb(180, 212, 240);
  margin: 10px;
  padding: 20px;
}

.back{
  margin-bottom: 30px;
  width: 50px;
  border-radius: 10px;
  text-align: center;
}

.list-group-item{
  margin-bottom: 10px;
}

button svg{
  background-color: #fff;
}


</style>
