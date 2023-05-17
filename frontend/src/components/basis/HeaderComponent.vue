<template>
  <div class="border bg-gray">
    <h1>it's header</h1>
    <login>
      <router-link :to="{ name: 'main' }">Main</router-link> | 
      <router-link :to="{ name: 'LogOutView' }">LogOut</router-link>
    </login>
    <login> | 
      <router-link :to="{ name: 'SignUpView' }">SignUpPage</router-link> | 
      <router-link :to="{ name: 'LogInView' }">LogInPage</router-link>
    </login> | 

    <input type="text">
    <button>search</button>
  </div>
</template>

<script>
export default {
  name: 'HeaderComponent',
  components: {

  },
  data() {
    return {

    }
  },
  computed: {

  },
  methods: {

  },

}
</script>

<style>

</style>