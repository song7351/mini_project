import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

Vue.use(Vuex)


const API_URL = 'http://127.0.0.1:8000'


export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    token: null,
    username: null,
    user_pk: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    CHANGE_MOVIES(state, movies) {
      state.movies = movies;
    },
    // 회원가입 && 로그인
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'home' })
    },
    DELETE_TOKEN(state) {
      state.token = null
      state.user_pk = null
      state.username = null
      router.push({ name: 'home' }).catch(()=>{});
    },
    SAVE_USRE_INFO(state, info){
      state.username = info.username
      state.user_pk = info.pk
    }
  },
  actions: {
    async getMovies(context) {
      try {
        const response = await axios.get("http://localhost:8000/api/v1/movies");
        if (response.data) {
          console.log(response.data);
          context.commit("CHANGE_MOVIES", response.data);
        }
      } catch (error) {
        console.log(error);
      }
    },
    async signUp(context, payload) {
        try {
           await axios({
            method: 'post',
            url: `${API_URL}/accounts/signup/`,
            data: {
              username: payload.username,
              password1: payload.password1,
              password2: payload.password2,
            }
          })
          .then((res) => {
            // console.log(res)
            context.commit('SAVE_TOKEN', res.data.key)
          })
        } catch (error) {
          console.log(error);
        }
    },
    logIn(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
        })
    },
    logOut(context) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
      })
        .then((res) => {
          if(res){
            console.log(res)
            context.commit('DELETE_TOKEN')
          }
        })
    },
    saveUserInfo(context, payload) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Token ${payload}`
        }
      })
        .then((res) => {
          console.log(res.data)
          context.commit('SAVE_USRE_INFO', res.data)
        })
    },
  },
  modules: {
  }
})