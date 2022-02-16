<template>
    <div class="container">
        <div class="column">
            <div class="column is-4 is-offset-4">
                <h1 class="title">
                    Log In
                </h1>
                <form>
                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input class="input" type="email" name="email" />
                        </div>
                    </div>
                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input class="input" type="password" name="password1" />
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
    export default {
        name:"LogIn"
    }
</script>