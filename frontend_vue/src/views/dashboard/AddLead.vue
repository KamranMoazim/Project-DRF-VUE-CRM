<template>
    <div class="container">
        <div class="column is-multiline">
            <div class="column is-12">
                <h1 class="title">
                    Add Lead
                </h1>
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Company</label>
                        <div class="control">
                            <input class="input" type="text" name="company" v-model="company" />
                        </div>
                    </div>
                    <div class="field">
                        <label>Contact Person</label>
                        <div class="control">
                            <input class="input" type="text" name="contact_person" v-model="contact_person" />
                        </div>
                    </div>
                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input class="input" type="email" name="email" v-model="email" />
                        </div>
                    </div>
                    <div class="field">
                        <label>Phone</label>
                        <div class="control">
                            <input class="input" type="text" name="phone" v-model="phone" />
                        </div>
                    </div>
                    <div class="field">
                        <label>Wetsite</label>
                        <div class="control">
                            <input class="input" type="text" name="website" v-model="website" />
                        </div>
                    </div>
                    <div class="field">
                        <label>Confidence</label>
                        <div class="control">
                            <input class="input" type="number" name="confidence" v-model="confidence" />
                        </div>
                    </div>
                    <div class="field">
                        <label>Estimated Value</label>
                        <div class="control">
                            <input class="input" type="number" name="estimated_value" v-model="estimated_value" />
                        </div>
                    </div>
                    <div class="field">
                        <label>Status</label>
                        <div class="control">
                            <div class="select">
                                <select v-model="status">
                                    <option value="new"> New </option>
                                    <option value="contacted"> Contacted </option>
                                    <option value="inprogess"> In Progress </option>
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
                                <select v-model="priority">
                                    <option value="low"> Low </option>
                                    <option value="medium"> Medium </option>
                                    <option value="high"> High </option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Add Lead</button>
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
        name:"AddLead",
        data(){
            return {
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
        },
        methods: {
            async submitForm(){
                // console.log("form")
                this.$store.commit("setIsLoading", true);
                const lead = {
                    company:this.company,
                    contact_person:this.contact_person,
                    email:this.email,
                    phone:this.phone,
                    website:this.website,
                    confidence:this.confidence,
                    estimated_value:this.estimated_value,
                    status:this.status,
                    priority:this.priority
                }
                // console.log(lead)

                await axios
                        .post("/api/v1/leads/", lead)
                        .then((res)=>{
                            // console.log(res.data)
                            toast({
                                message:"Lead Added Successfully!",
                                type:"is-success",
                                dismissible:true,
                                pauseOnHover:true,
                                duration:2000,
                                position:"bottom-right"
                            })
                            this.$router.push("/dashboard/leads")
                        })
                        .catch((err)=>{
                            toast({
                                message:"Lead could not Added!",
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