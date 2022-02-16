<template>
    <div class="container">
        <div class="is-multiline">
            <div class="column is-12">
                <h1 class="title">Edit {{lead.company}} </h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Company</label>
                        <div class="control">
                            <input class="input" type="text" name="company" v-model="lead.company" />
                        </div>
                    </div>
                    <div class="field">
                        <label>Contact Person</label>
                        <div class="control">
                            <input class="input" type="text" name="contact_person" v-model="lead.contact_person" />
                        </div>
                    </div>
                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input class="input" type="email" name="email" v-model="lead.email" />
                        </div>
                    </div>
                    <div class="field">
                        <label>Phone</label>
                        <div class="control">
                            <input class="input" type="text" name="phone" v-model="lead.phone" />
                        </div>
                    </div>
                    <div class="field">
                        <label>Wetsite</label>
                        <div class="control">
                            <input class="input" type="text" name="website" v-model="lead.website" />
                        </div>
                    </div>
                    <div class="field">
                        <label>Confidence</label>
                        <div class="control">
                            <input class="input" type="number" name="confidence" v-model="lead.confidence" />
                        </div>
                    </div>
                    <div class="field">
                        <label>Estimated Value</label>
                        <div class="control">
                            <input class="input" type="number" name="estimated_value" v-model="lead.estimated_value" />
                        </div>
                    </div>
                    <div class="field">
                        <label>Status</label>
                        <div class="control">
                            <div class="select">
                                <select v-model="lead.status">
                                    <option value="new"> New </option>
                                    <option value="contacted"> Contacted </option>
                                    <option value="inprogress"> In Progress </option>
                                    <option value="lost"> Lost </option>
                                    <option value="won"> Won </option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <div class="field">
                        <label>Priority</label>
                        <div class="control">
                            <div class="select" >
                                <select v-model="lead.priority">
                                    <option value="low"> Low </option>
                                    <option value="medium"> Medium </option>
                                    <option value="high"> High </option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Update Lead</button>
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
    name:"EditLead",
    data(){
        return {
            lead: { 
                id:"",
                company:"",
                contact_person:"",
                email:"",
                phone:"",
                website:"",
                confidence:0,
                estimated_value:0,
                status:"new",
                priority:"low"
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
                    // console.log(res)
                    this.lead = res.data
                })
                .catch((err)=>{
                    console.log(err)
                })
            this.$store.commit("setIsLoading", false);
        },
        async submitForm(){
            // console.log("form")
            this.$store.commit("setIsLoading", true);
            // console.log(this.lead)

            await axios
                    .patch(`/api/v1/leads/${this.lead.id}/`, this.lead)
                    .then((res)=>{
                        // console.log(res.data)
                        toast({
                            message:"Lead Updated Successfully!",
                            type:"is-success",
                            dismissible:true,
                            pauseOnHover:true,
                            duration:2000,
                            position:"bottom-right"
                        })
                        this.$router.push(`/dashboard/lead/${this.lead.id}`)
                    })
                    .catch((err)=>{
                        toast({
                            message:"Lead could not Updated. Try Again!",
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