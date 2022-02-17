<template>
    <div class="container">
        <div class="is-multiline">
            <div class="column is-12">
                <h1 class="title"> {{team.name}} </h1>
                <router-link :to="{name:'AddMember'}" class="button is-primary">Add Member</router-link>
            </div>
            <div class="column is-12">
                <h2 class="subtitle"> Team Members </h2>
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>
                                Name
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-bind:key="member.id" v-for="member in team.members">
                            <td>
                                {{member.username}}
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from "axios"
    import {toast} from "bulma-toast"

export default {
    name:"Team",
    data(){
        return {
            team: {
                members:[],
                name:""
            }
        }
    },
    mounted(){
        this.getTeam()
    },
    methods: {
        async getTeam(){
            this.$store.commit("setIsLoading", true);
            await axios
                    .get("/api/v1/teams/get-my-teams/")
                    .then((res)=>{
                        // console.log("/api/v1/teams/get-my-teams/ =======> ", res)
                        this.team = res.data
                        // this.$store.commit("setTeam", {"id":res.data.id, "name":res.data.name})
                        // this.$router.push("/dashboard/my-account")
                    })
                    .catch((err)=>{
                        console.log(err)
                    })
            this.$store.commit("setIsLoading", false);
        }
    }
}
</script>