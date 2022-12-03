<template>
  <div class="form-box">
  <div class="form">
    <div class="mb-3">
      <label for="exampleFormContrlInput1" class="form-label" >제목</label>
      <input v-model="title" type="email" class="form-control" id="exampleFormControlInput1">
    </div>
    <div class="mb-3">
      <label for="exampleFormControlTextarea1" class="form-label">내용</label>
      <textarea v-model="content" class="form-control" id="exampleFormControlTextarea1" placeholder="내용을 입력하세요." rows="3"></textarea>
    </div>
    <div class="create-btn-form">
      <b-button variant="outline-secondary" v-on:click="createArticle">등록</b-button>
      <b-button variant="outline-secondary" v-on:click="goArticleList">취소</b-button>
    </div>
  </div>
</div>
</template>

<script>
import axios from "axios";
import Swal from "sweetalert2";
const API_URL = "http://127.0.0.1:8000";

export default {

  data(){
    return{
      title: '',
      content: '',
    }
  },
  methods:{
    goArticleList(){
      this.$router.push({ name: 'community' })
    },
    async createArticle() {
      if (this.content === "") {
        Swal.fire("내용을 입력해주세요.");
        return;
      } else if (this.title === "") {
        Swal.fire("제목을 입력해주세요.");
        return;
      }
      axios({
        method: "post",
        url: `${API_URL}/api/v1/community/articles/`,
        data: {
          title: this.title,
          content: this.content,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          this.$router.push({ name: 'community'})
        })
        .catch((err) => {
          console.log(err);
        });
    },
  }
}
</script>

<style scoped>
.create-btn-form {
  display: flex;
  justify-content: center;
  background-color: #ECEEFF;
}
.form {
  padding-left: 5%;
  padding-right: 5%;
  padding-top: 20px;
  padding-bottom: 20px;
  margin-top: 20px;
  margin-bottom: 30px;
}
.form-box {
  margin: 30px;
  margin-right: 400px;
  margin-left: 400px;
  margin-top: 60px;
  border: solid rgb(179, 175, 175);
  border-width: 1px;
  border-top-left-radius: 0.25rem;
  border-top-right-radius: 0.25rem;
}
</style>