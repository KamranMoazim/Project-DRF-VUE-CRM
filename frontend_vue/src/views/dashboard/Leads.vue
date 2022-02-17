<template>
    <div class="container">
        <div class="column is-multiline">
            <div class="column is-12">
                <h1 class="title">
                    Leads
                </h1>
                <router-link :to="{name:'AddLead'}" class="button is-success"> Add Lead </router-link>
            </div>
            <div class="column is-12">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Company</th>
                            <th>Contact Person</th>
                            <th>Assigned To</th>
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
                            <td>
                                <template v-if="lead.assigned_to">
                                    {{lead.assigned_to.username}}
                                </template>
                            </td>
                            <td>{{lead.status}}</td>
                            <td>
                                <router-link :to="{name:'Lead', params:{id:lead.id}}">
                                    Details
                                </router-link>
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
                            // console.log(res)
                            this.leads = res.data
                        })
                        .catch((err)=>{
                            toast({
                                message:"Could not Get Leads from Database!",
                                type:"is-warning",
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