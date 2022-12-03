<template>
  <div>
    <ul class="article-wrap">
        <li class="article-id">{{ article.id }}</li>
        <li class="article-title" v-on:click="goArticleDetail(article.id)">{{ article.title }}</li>
        <li class="article-who">{{ article.user.username }}</li>
        <li class="article-date">{{ article.created_at | moment('YYYY-MM-DD') }}</li>
    </ul>
    <hr>
  </div>
    
</template>

<script>
export default {
  props: ["article"],
  methods:{
    goArticleDetail(article_id){
      this.$router.push({ name: 'articledetail', params: { id: article_id } })
    },
  }
}
</script>

<style>
hr{
  display: inline-block;
  width: 90%;
}

.article-wrap{
  display: flex;
  padding: 10px 0 5px 0;
}

.article-id{
  width:27%;
}
.article-title{
  width:19%;
  cursor: pointer;
}
.article-title:hover{
  text-decoration: underline;
}

.article-who{
  width:27%;
}

.article-date{
  width:27%;
}

</style>