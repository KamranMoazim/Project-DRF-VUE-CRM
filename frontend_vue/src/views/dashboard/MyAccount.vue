<template>
    <div class="container">
        <div class="column is-multiline">
            <div class="column is-12">
                <h1 class="title">
                    My Account
                </h1>
            </div>
            <div class="column is-12">
                <button class="button is-danger" @click="logout()">
                    Log Out
                </button>
            </div>
        </div>
    </div>
</template>


<script>
    import axios from "axios"
    import {toast} from "bulma-toast"

    export default {
        name:"MyAccount",
        methods: {
            async logout() {
                this.$store.commit("setIsLoading", true);
                // console.log("Logout clicked")
                // await axios
                //     .post("/api/v1/token/logout/")
                //     .then((res)=>{
                //         toast({
                //             message:"Logout Successfully!",
                //             type:"is-success",
                //             dismissible:true,
                //             pauseOnHover:true,
                //             duration:2000,
                //             position:"bottom-right"
                //         })
                //     })
                toast({
                    message:"Logout Successfully!",
                    type:"is-success",
                    dismissible:true,
                    pauseOnHover:true,
                    duration:2000,
                    position:"bottom-right"
                })
                axios.defaults.headers.common["Authorization"] = "";
                localStorage.removeItem("token")
                this.$store.commit("removeToken")
                this.$router.push("/")
                this.$store.commit("setIsLoading", false);
            }
        }
    }
</script>