<template>
  <div>
    <form @submit.prevent="logOut">
      <button>LogOut</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'LogOutView',
  methods: {
    logOut() {
      this.$store.dispatch('logOut')
    }
  }
}
</script>

<style></style>