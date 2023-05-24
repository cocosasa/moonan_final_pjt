<template>
  <div id="app">
    <nav>
      <HeaderComponent/>
    </nav>
    <div class="center">
      <router-view/>
    </div>
  </div>
</template>

<script>
import HeaderComponent from '@/components/basis/HeaderComponent'
export default {
  name: 'App',
  components: {
    HeaderComponent
  }
}
</script>

<style>
#app {
  font-family: 'NanumSquare', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  color: white;
  color: black;
  min-width: 1200px;
  /* background-color: #070707; */
}

nav a {
  text-decoration: none;
  font-weight: bold;
  color: white;
}

nav a.router-link-exact-active {
  color: #ff0000;
}

.border {
  border: 1px solid darkcyan;
}
.bg-gray {
  background-color: lightgrey;
}
.center {
  max-width: 1200px;
  margin: 0 auto;
}
</style>