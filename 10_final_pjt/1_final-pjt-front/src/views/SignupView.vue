<template>
  <div id="big_cont">
    <div id="container">
      <h1>💜 회원가입 💜</h1>
      <form @submit.prevent="signUp">
        <label for="username">아이디</label><br>
        <b-form-input
          id="username"
          v-model="username"
          :state="nameState"
          aria-describedby="input-live-help input-live-feedback"
          placeholder="Enter your ID"
          trim
      ></b-form-input><br>

    <b-form-invalid-feedback id="input-live-feedback">
      Enter at least 5 letters
    </b-form-invalid-feedback>


        <label for="password1">비밀번호</label><br />
        <b-form-input placeholder="Enter your password" type="password" id="password1" v-model="password1"></b-form-input><br>

        <label for="password2">비밀번호 확인</label><br />
        <b-form-input placeholder="Password again" type="password" id="password2" v-model="password2"></b-form-input><br>

        <b-button variant="light" type="submit">회원가입</b-button>
      </form>
    </div>
  </div>

</template>

<script>
import Swal from "sweetalert2";

export default {
  name: "SignUpView",
  computed: {
      nameState() {
        return this.username.length > 4 ? true : false
      }
    },
  data() {
    return {
      username: '',
      password1: null,
      password2: null,
    };
  },
  methods: {
    signUp() {
      const username = this.username;
      const password1 = this.password1;
      const password2 = this.password2;

      const payload = {
        username: username,
        password1: password1,
        password2: password2,
      };
      if (password1 !== password2) {
        Swal.fire("비밀번호가 일치하지 않습니다.")
      } else {
        this.$store.dispatch("signUp", payload);
      }
      if (password1.length && password2.length <= 6) {
        Swal.fire("비밀번호가 너무 짧습니다.")
      } else {
        this.$store.dispatch("signUp", payload);
      }
    },
  },
};
</script>

<style scoped>
#big_cont {
  display: flex;
  justify-content: center;
  margin-top:20px;
}

#container {
  margin-top: 50px;
  align-items: center;
  border: 2px solid rgb(196, 186, 204);
  background-color: #fff;
  border-radius: 30px;
  width: 400px;
  padding-top:30px;
  padding-bottom: 60px;
}

h1 {
  margin-top: 30px;
  margin-bottom: 40px;
  background-color: #fff;
}

label {
  font-weight: 500;
  margin-bottom: 8px;
  background-color: #fff;
}

#username {
  border-radius: 5px;
  background-color: #fff;
}
#password1 {
  margin-bottom: 40px;
  border-radius: 5px;
  background-color: #fff;
  display: inline-block;
  width:200px;
}
#password2 {
  margin-bottom: 40px;
  border-radius: 5px;
  background-color: #fff;
  display: inline-block;
  width:200px;
}

form{
  background-color: #fff;
}
</style>

<style>
#swal2-title {
  color:rgb(75, 82, 92);
  background-color:rgb(180, 212, 240);
  margin: 20px;
  padding: 20px;
}

#input-live-feedback{
  background-color: #fff;
  margin-bottom:30px;
}

.form-control.is-invalid{
  display: inline-block;
  width:200px;
}

.form-control.is-valid{
  display: inline-block;
  width:200px;
  margin-bottom:40px;
}

.form-control{
  display: inline-block;
  width:200px;
  background-color: #fff;
}
</style>