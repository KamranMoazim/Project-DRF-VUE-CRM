<template>
    <div class="container">
        <div class="column">
            <div class="column is-4 is-offset-4">
                <h1 class="title">
                    Sign Up
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
                        <label>Repeat Password</label>
                        <div class="control">
                            <input class="input" type="password" name="password2" v-model="password2" />
                        </div>
                    </div>
                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">
                            {{error}}
                        </p>
                    </div>
                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Sign Up</button>
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
        name:"SignUp",
        data() {
            return {
                username:"",
                password1:"",
                password2:"",
                errors:[],
            }
        },
        methods: {
            async submitForm(){
                // console.log("Signup form")
                // console.log(this.username)
                // console.log(this.password1)
                // console.log(this.password2)

                this.$store.commit("setIsLoading", true);

                this.errors = []

                if (this.username === "") {
                    this.errors.push("The username is missing!")
                }
                if (this.password1 === "") {
                    this.errors.push("The password is too short!")
                }
                if (this.password1 != this.password2) {
                    this.errors.push("Confirm Password is not matching!")
                }


                if (!this.errors.length) {
                    const formData = {
                        username:this.username,
                        password:this.password1,
                    }
                    await axios
                        .post("/api/v1/users/", formData)
                        .then((res)=>{
                            toast({
                                message:"Account created Successfully! Please Login.",
                                type:"is-success",
                                dismissible:true,
                                pauseOnHover:true,
                                duration:2000,
                                position:"bottom-right"
                            })
                            this.$router.push("/log-in")
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

                this.$store.commit("setIsLoading", false);
            }
        }
    }
</script>