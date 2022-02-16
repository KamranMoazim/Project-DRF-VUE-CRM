<template>
    <nav class="navbar is-dark">
        <div class="navbar-brand">
            <router-link to="/" class="navbar-item">
                <strong>
                    DRF VUE CRM
                </strong>
            </router-link>
        </div>
        <div class="navbar-menu">
            <div class="navbar-end">
                <div class="navbar-item">
                    <div class="buttons">
                        <router-link to="/sign-up"  class="button is-success"><strong>SignUp</strong></router-link>
                        <router-link to="/log-in"  class="button is-light">Log In</router-link>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>


<script>
    export default {
        name:"Navbar"
    }
</script>

<style lang="scss">

</style>