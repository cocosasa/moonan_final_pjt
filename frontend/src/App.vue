<template>
  <div id="app">
    <nav>
      <HeaderComponent/>
    </nav>
    <router-view/>
  </div>
</template>

<script>
import HeaderComponent from './components/basis/HeaderComponent'
export default {
  name: 'App',
  components: {
    HeaderComponent
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.border {
  border: 1px solid darkcyan;
}

.bg-gray {
  background-color: lightgrey;
}
</style>