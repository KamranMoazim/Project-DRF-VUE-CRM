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
                <router-link to="/dashboard/leads" class="navbar-item">Leads</router-link>
                <router-link to="/dashboard/team" class="navbar-item">Team</router-link>
                <div class="navbar-item">
                    <div class="buttons">
                        <template v-if="!$store.state.isAuthenticated">
                            <router-link to="/sign-up"  class="button is-success"><strong>SignUp</strong></router-link>
                            <router-link to="/log-in"  class="button is-light">Log In</router-link>
                        </template>
                        <template v-else>
                            <router-link to="/dashboard"  class="button is-info"><strong>Dashboard</strong></router-link>
                            <router-link to="/dashboard/my-account"  class="button is-light">My Account</router-link>
                        </template>
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