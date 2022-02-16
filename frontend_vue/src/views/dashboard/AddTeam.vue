<template>
    <div class="container">
        <div class="column is-multiline">
            <div class="column is-12">
                <h1 class="title">
                    Add Team
                </h1>
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Team Name</label>
                        <div class="control">
                            <input class="input" type="text" name="name" v-model="name" />
                        </div>
                    </div>
                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Add Team</button>
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
        name:"AddTeam",
        data(){
            return {
                name:""
            }
        },
        methods: {
            async submitForm(){
                this.$store.commit("setIsLoading", true);

                const team = {
                    name:this.name
                }

                await axios
                        .post("/api/v1/teams/", team)
                        .then((res)=>{
                            // console.log(res.data)
                            toast({
                                message:"Team Created Successfully!",
                                type:"is-success",
                                dismissible:true,
                                pauseOnHover:true,
                                duration:2000,
                                position:"bottom-right"
                            })
                            this.$store.commit("setTeam", {"id":res.data.id, "name":this.name})
                            this.$router.push("/dashboard")
                        })
                        .catch((err)=>{
                            toast({
                                message:"Team could not Created!",
                                type:"is-danger",
                                dismissible:true,
                                pauseOnHover:true,
                                duration:2000,
                                position:"bottom-right"
                            })
                            console.log(err)
                        })

                this.$store.commit("setIsLoading", false);
            }
        }
    }
</script>