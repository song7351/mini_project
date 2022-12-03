<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/movies">Movies</router-link> |
      <router-link to="/random">Random</router-link> |
      <router-link to="/watch-list">WatchList</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<style>
nav{
  text-align: center;
  height: 100px;
  line-height: 100px;
  font-size: 50px;
  background-color: darksalmon;
}
</style>