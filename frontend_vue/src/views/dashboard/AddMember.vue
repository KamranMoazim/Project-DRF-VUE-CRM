<template>
    <div class="container">
        <div class="is-multiline">
            <div class="column is-12">
                <h1 class="title"> Add Member </h1>
            </div>
            <div class="column is-12">
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
                            <button class="button is-success">Add</button>
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
    name:"AddMember",
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
                            message:"Member Added Successfully!",
                            type:"is-success",
                            dismissible:true,
                            pauseOnHover:true,
                            duration:2000,
                            position:"bottom-right"
                        })
                        // this.$router.push({name:"Team"})

                        const emailData = {"email":this.username}

                        axios
                            .post("/api/v1/teams/add-member-to-team/", emailData)
                            .then((res)=>{
                                this.$router.push({name:"Team"})
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
                    })
                    .catch((error)=>{
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                        } else if (error.message) {
                            this.errors.push("Something went wrong! Please Try Again!")  
                            toast({
                                message:"Could not Add Member to Your Team! Try Again.",
                                type:"is-danger",
                                dismissible:true,
                                pauseOnHover:true,
                                duration:2000,
                                position:"bottom-right"
                            })  
                        }
                    })
            }

            this.$store.commit("setIsLoading", false);
        }
    }
}
</script>