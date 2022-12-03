<template>
  <div>
    <ul class="form-box">
        <li class="name">작성자: {{article.user.username}}</li>
        <li>작성일: {{article.created_at | moment('YYYY-MM-DD')}}</li>
        <br>
        <li>제목: {{article.title}}</li>
        <li><p>{{ article.content }}</p></li>

    </ul>
    <br>
    <b-button variant="outline-secondary" class="deletebtn" v-on:click="delArticle(article.id)" v-show="checkUser(article.user.username)" v-if="flag">삭제</b-button>

  </div>
</template>

<script>
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default {
    data(){
        return{
            article: null,
            reviews: null,
            flag: true,
        }
    },
    created() {
        this.getArticleDetail();
        // 미구현기능
        // this.getArticleReviews(); 
    },
    computed:{
        isLoggedIn() {
        return this.$store.getters.isLogin;
        }
    },
    methods:{
        checkUser(username){
            if(username === this.$store.state.username){
                return true
            }
            return false
        },
        getArticleDetail() {
        axios({
            method: "get",
            url: `${API_URL}/api/v1/community/articles/${this.$route.params.id}/`,
        })
            .then((res) => {
            console.log(res.data);
            this.article = res.data;
            })
            .catch((err) => {
            console.log(err);
            });
        },
        // 미구현기능
        // getArticleReviews() {
        // axios({
        //     method: "get",
        //     url: `${API_URL}/api/v1/community/comments/`,
        // })
        //     .then((res) => {
        //     console.log(res.data)
        //     const tmp = res.data.filter(
        //         (review) => review.article == this.$route.params.id
        //     );
        //     this.reviews = tmp;
        //     // console.log(this.reviews)
        //     })
        //     .catch((err) => {
        //     console.log(err);
        //     });
        // },
    }
}
</script>

<style scoped>
.form-box {
  margin: 30px;
  margin-right: 400px;
  margin-left: 400px;
  border: solid rgb(179, 175, 175);
  border-width: 1px;
  border-top-left-radius: 0.25rem;
  border-top-right-radius: 0.25rem;
}
.name {
  padding-top: 30px;
}
/* =======
.article-dt{
    margin-top: 50px;
    margin-bottom: 100px;
}

ul{
    border: 1px solid #000;
    border-radius: 20px;
    display: inline-block;
    background-color: #fff;
    width: 400px;
    padding: 30px 0 20px 0;
}
.title{
    margin-bottom: 10px;
}

.user{
    font-size: 13px;
}
.date{
    font-size: 12px;
    margin-bottom: 30px;
}

>>>>>>> Stashed changes */
</style>