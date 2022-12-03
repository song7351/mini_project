<template>
    <b-list-group-item>
    <div class="big-box">
      <div class="block1">
        <div>
        <span v-if="reviewLikeFlag && isLoggedIn"><div class="heart" v-on:click="likeReview(review.id)">💖</div></span>
        <span v-if="!reviewLikeFlag && isLoggedIn"><div class="heart" v-on:click="likeReview(review.id)">🤍</div></span>
        <span v-if="!isLoggedIn"><div class="heart" v-on:click="needLogin()">🤍</div></span>
        <span class="review-cnt">{{ reviewLikeCnt }}</span>
      </div>
      </div>

      <div class="block2">
      <ul class="review-list">
        <li class="username">
            {{ review.user.username }}&nbsp;&nbsp;[ {{ review.user_vote_average}}점 ]
        </li>
        <li class="review-data">{{ review.created_at | moment('YYYY-MM-DD HH:mm:ss')  }} 작성</li>
        <li class="review-content" v-if="flag">{{ review.content }}</li>
      </ul>
      </div>
      
      <div class="heart-wrap">
        <span v-if="reviewLikeFlag && isLoggedIn"><div class="heart" v-on:click="likeReview(review.id)">💖</div></span>
        <span v-if="!reviewLikeFlag && isLoggedIn"><div class="heart" v-on:click="likeReview(review.id)">🤍</div></span>
        <span v-if="!isLoggedIn"><div class="heart" v-on:click="needLogin()">🤍</div></span>
        <span class="review-cnt">{{ reviewLikeCnt }}</span>
      </div>
    </div>


    <div>
        <div class="change-form">
        <div class="change-form" v-if="!flag">
          <input type="number" min="0" max="5" step="1" v-model="review_vote" class="vote-average">
          <input type="text" v-model="review_content" class="form-control">
        </div>
        <b-button variant="outline-secondary" class="deletebtn" v-on:click="chgUpdate(review.content, review.user_vote_average)" v-show="checkUser(review.user.username)" v-if="flag">수정</b-button>
        <b-button variant="outline-secondary" class="deletebtn" v-on:click="delReview(review.id)" v-show="checkUser(review.user.username)" v-if="flag">삭제</b-button>
        <b-button variant="outline-secondary" class="deletebtn" v-on:click="putReview(review.id)" v-if="!flag">수정 등록</b-button>
        <b-button variant="outline-secondary" class="deletebtn" v-on:click="chgUpdate(null ,0)" v-if="!flag">취소</b-button>
      </div>
    </div>
  </b-list-group-item>

</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  props: ["review"],
  data(){
    return{
        flag: true,
        review_content: '',
        review_vote: 0,
        reviewLikeFlag: false,
        reviewLikeCnt: 0,
    }
  },
  computed:{
    isLoggedIn() {
      return this.$store.getters.isLogin;
    }
  },
  created(){
    this.chkReviewLike(this.review.id)
  },
  methods:{
    chkReviewLike(review_pk){
        axios({
        method: "get",
        url: `${API_URL}/api/v1/reviews/${review_pk}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          if(res.data.like_users.includes(this.$store.state.user_pk)){
            this.reviewLikeFlag = true
          }
          this.reviewLikeCnt = res.data.like_users.length

        })
        .catch((err) => {
          console.log(err);
        });
    },
    needLogin() {
      alert("로그인이 필요한 기능입니다.");
    },
    likeReview(review_pk) {
      axios({
        method: "post",
        url: `${API_URL}/api/v1/reviews/${review_pk}/likes/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          this.reviewLikeFlag = !this.reviewLikeFlag;
          this.chkReviewLike(review_pk)
        })
        .catch((err) => {
          console.log(err);
        });
    },
    chgUpdate(content, vote){
      this.flag = !this.flag
      this.review_content = content
      this.review_vote = vote
    },
    checkUser(username){
      if(username === this.$store.state.username){
        return true
      }
      return false
    },
    delReview(review_pk) {
      axios({
        method: 'DELETE',
        url: `${API_URL}/api/v1/reviews/${review_pk}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          this.$router.go()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    async putReview(review_pk){
      if(this.content === ''){
        alert("내용을 입력해주세요.")
        return
      }else if(this.user_vote_average <0 || this.user_vote_average > 5){
        alert("평점 범위가 벗어났습니다.")
        return
      }
      axios({
        method: 'PUT',
        url: `${API_URL}/api/v1/reviews/${review_pk}/`,
        data: {
          user_vote_average: this.review_vote,
          content: this.review_content,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          this.$router.go()
        })
        .catch((err) => {
          console.log(err)
        })
    },
  }
}
</script>

<style scoped>
.change-form {
  display: flex;
  justify-content: center;
  background-color: white;
}
.heart{
  background-color: white;
}

.heartfill{
  color: red;
}

.heart-wrap{
  width: 55px;
  background-color: #fff;
}

.heart-wrap span {
  background-color: #fff;
}

.review-cnt{
  margin-left: 5px;
}

.big-box{
  display: flex;
  justify-content: space-between;
  background-color: white;
}

.block1{
  visibility: hidden;
  width: 55px;
}

.block2{
  background-color: white;
}
</style>