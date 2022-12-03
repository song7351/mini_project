<template>
  <div>
    <h3>💜 112 Film 자유게시판 💜</h3>
    <ul class="articleTitleWrap">
        <li class="articleId">번호</li>
        <li class="articleTitle">제목</li>
        <li class="articleUser">작성자</li>
        <li class="articleCreate">작성일</li>
    </ul>
    <hr>

    <ListArticle
        v-for="(article, index) in articles"
        v-bind:key="index"
        v-bind:article="article"
    />
    
    <b-button class="createbtn" variant="light" type="submit" v-on:click="goCreateArticle">글쓰기</b-button>
  </div>
</template>

<script>
import axios from "axios";
import ListArticle from '@/components/ListArticle';


export default {
    components: {
        ListArticle,
    },
    data(){
        return{
            articles: [],
        }
    },
    created(){
        this.getArticles();
    },
    methods:{
      getArticles() {
        const URL = "http://127.0.0.1:8000";
        axios({
            method: "get",
            url: `${URL}/api/v1/community/articles/`,
        })
            .then((res) => {
                console.log(res.data)
                this.articles = res.data
            })
            .catch((err) => {
            console.log(err);
            });
        },
        goCreateArticle(){
            this.$router.push({ name: 'createArticle' })
        }
    }
}
</script>

<style scoped>

h3{margin-top:50px; margin-bottom:60px;}

hr{
    display: inline-block;
    width: 90%;
}

.articleTitleWrap{
    display: flex;
    justify-content:space-around;
    /* border: 1px solid #000; */
    margin:0;
    padding: 10px 0 10px 0;
}

.articleTitleWrap li{
    font-weight:bold;
}
.articleId{
    width: 10%;
}
.articleTitle{
    width: 70;
}
.articleUser{
    width: 10%;
}
.articleCreate{
    width: 10%;
}

.createbtn{
    margin-top: 40px;
    margin-bottom: 40px;
}
</style>