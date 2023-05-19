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
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  color: #2c3e50;
  min-width: 1200px;
}

nav a {
  text-decoration: none;
  font-weight: bold;
  color: #2c3e50;
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