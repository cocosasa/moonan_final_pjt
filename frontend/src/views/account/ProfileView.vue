<template>
  <div>
    <div class="d-flex justify-content-between">
      <div class="profile-img-circle">
        <img class="profile-img" src="@/assets/moonanface.png">
      </div>
      <div>
        <p>아이디</p>
        <p>아이디</p>
      </div>
      <div class="d-flex">
        <div class="profile-info">
          <p>24</p>
          <p>SOLVE</p>
        </div>
        <div class="profile-info">
          <p>24</p>
          <p>SOLVE</p>
        </div>
        <div class="profile-info">
          <p>24</p>
          <p>SOLVE</p>
        </div>
        <div class="profile-info">
          <p>24</p>
          <p>SOLVE</p>
        </div>
      </div>
    </div>
    <hr>
    <div>
      <h3>WANT TO WATCH</h3>
      <div>영화</div>
    </div>
    <div>
      <h3>WANT TO WATCH</h3>
      <div>영화</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProfileView',
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
.profile-img-circle{
  width: 150px;
  height: 150px;
  overflow: hidden;
  border-radius: 100px;
}
.profile-img{
  width: 100%;
  height: 100%;
}
.profile-info{
  margin-top: 60px;
  margin-bottom: 40px;
  padding-left: 60px;
  padding-right: 60px;
  border-right: 1px solid;
  align-items: center;
}
.profile-info > p {
  text-align: center;
}
</style>