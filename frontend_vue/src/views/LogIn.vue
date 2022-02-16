<template>
    <div class="container">
        <div class="column">
            <div class="column is-4 is-offset-4">
                <h1 class="title">
                    Log In
                </h1>
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input class="input" type="email" name="email" v-model="username" />
                        </div>
                    </div>
                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input class="input" type="password" name="password1" v-model="password1" />
                        </div>
                    </div>
                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Login</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>


<script>
    import axios from "axios"
    import {toast} from "bulma-toast"

    export default {
        name:"LogIn",
        data() {
            return {
                username:"",
                password1:"",
                errors:[],
            }
        },
        methods: {
            async submitForm(){
                // console.log("Login form")
                // console.log(this.username)
                // console.log(this.password1)

                axios.defaults.headers.common["Authorization"] = "";
                localStorage.removeItem("token")

                this.errors = []

                if (this.username === "") {
                    this.errors.push("The username is missing!")
                }
                if (this.password1 === "") {
                    this.errors.push("The password is too short!")
                }


                if (!this.errors.length) {
                    const formData = {
                        username:this.username,
                        password:this.password1,
                    }
                    await axios
                        .post("/api/v1/token/login/", formData)
                        .then((res)=>{
                            // console.log(res)
                            const token = res.data.auth_token;
                            this.$store.commit("setToken", token)
                            axios.defaults.headers.common["Authorization"] = "Token " + token
                            localStorage.setItem("token", token)

                            toast({
                                message:"Logged In Successfully!",
                                type:"is-success",
                                dismissible:true,
                                pauseOnHover:true,
                                duration:2000,
                                position:"bottom-right"
                            })
                            this.$router.push("/dashboard/my-account")
                        })
                        .catch((error)=>{
                            if (error.response) {
                                for (const property in error.response.data) {
                                    this.errors.push(`${property}: ${error.response.data[property]}`)
                                }
                            } else if (error.message) {
                                this.errors.push("Something went wrong! Please Try Again!")    
                            }
                        })
                }
            }
        }
    }
</script>