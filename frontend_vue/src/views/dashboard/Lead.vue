<template>
    <div class="container">
        <div class="is-multiline">
            <div class="column is-12">
                <h1 class="title"> {{lead.company}} </h1>
                <router-link :to="{name:'EditLead', params:{id:lead.id||1}}" class="button is-light">Edit</router-link>
                <!-- :to="{name:'Lead', params:{id:lead.id}}"  -->
                <!-- to="/dashboard/edit-lead/:id"  -->
                <!-- :to="{name:'EditLead', params:{id:lead.id}}" -->
            </div>
            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Details</h2>
                    <p><strong>Status: </strong> {{lead.status}} </p>
                    <p><strong>Priority: </strong> {{lead.priority}} </p>
                    <p><strong>Confidenc: </strong> {{lead.confidence}} </p>
                    <p><strong>Esimated Value: </strong> {{lead.estimated_value}} </p>
                    <p><strong>Created At: </strong> {{lead.created_at}} </p>
                    <p><strong>Modified At: </strong> {{lead.modified_at}} </p>
                </div>
            </div>
            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Contact Information</h2>
                    <p><strong>Contact Person: </strong> {{lead.contact_person}} </p>
                    <p><strong>Email: </strong> {{lead.email}} </p>
                    <p><strong>Phone: </strong> {{lead.phone}} </p>
                    <p><strong>Website: </strong> {{lead.website}} </p>
                </div>
            </div>
        </div>
    </div>
</template>


<script>

import axios from "axios"
import {toast} from "bulma-toast"

export default {
    name:"Lead",
    data(){
        return {
            lead: { 
                id:""
            }
        }
    },
    mounted(){
        this.getLead()
    },
    methods: {
        async getLead(){
            this.$store.commit("setIsLoading", true);

            const leadId = this.$route.params.id;

            axios
                .get(`/api/v1/leads/${leadId}/`)
                .then((res)=>{
                    // console.log(res.data)
                    this.lead = res.data
                    // console.log(this.lead)
                })
                .catch((err)=>{
                    console.log(err)
                    toast({
                        message:"Could not Get Lead from Database!",
                        type:"is-warning",
                        dismissible:true,
                        pauseOnHover:true,
                        duration:2000,
                        position:"bottom-right"
                    })
                })

            this.$store.commit("setIsLoading", false);
        }
    }
}
</script>