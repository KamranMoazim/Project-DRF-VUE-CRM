<template>
    <div class="container">
        <div class="column is-multiline">
            <div class="column is-12">
                <h1 class="title">
                    Leads
                </h1>
                <router-link to="/dasboard/leads/add"> Add Lead </router-link>
            </div>
            <div class="column is-12">
                <table class="table">
                    <thead>
                        <tr>
                            <th>Company</th>
                            <th>Contact Person</th>
                            <th>Status</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr
                            v-for="lead in leads"
                            v-bind:key="lead">
                            <td>{{lead.company}}</td>
                            <td>{{lead.contact_person}}</td>
                            <td>{{lead.status}}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>


<script>

    import axios from "axios"

    export default {
        name:"Leads",
        data(){
            return {
                leads:[]
            }
        },
        mounted(){
            this.getLeads()
        },
        methods: {
            async getLeads(){

                this.$store.commit("setIsLoading", true);

                await axios
                        .get("/api/v1/leads/")
                        .then((res)=>{
                            console.log(res)
                            this.leads = res.data
                        })
                        .catch((err)=>{
                            console.log(err)
                        })

                this.$store.commit("setIsLoading", false);
            }
        }
    }
</script>