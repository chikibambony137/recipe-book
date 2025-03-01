<script>
    import axios from 'axios';

    export default {
        data() {
            return {
                API_URL: 'http://localhost:8000',
                login: '',
                password: ''
            };
        },
        methods: {
            async Login() {
                try {
                    await axios.post(`${this.API_URL}/login?login=${this.login}&password=${this.password}`)
                    this.$router.push('/home')
                }
                catch (error) {
                    alert('Ошибка: ' + (error.response?.data?.detail || ''));
                }
            },

            goToReg() {
                this.$router.push('/registration')
            },
        },
}
</script>

<template>
    <div class="loginForm">
        <div>
            <a class="toRegister" @click="goToReg"><u>Register ></u></a>
            <img src="..\assets\logo.png" class="logo"/>
        </div>
        <div>
            <form @submit.prevent="Login">
                <p><input type="login" class="login-input" v-model="login" placeholder="Login / Email" maxlength=50/></p>
                <p><input type="password" class="login-input" v-model="password" placeholder="Password" maxlength=50/></p>
                <p><button type="submit" class="login-button" @click="Login">Login</button></p>
                <a class="forgotPassword" href="/home"><u>Forgot password?</u></a>
            </form>
        </div>        
    </div>

</template>

<style scoped>

.loginForm {
    background-color: #1F42AE;
    width: 350px;
    height: 500px;
    border-radius: 20px;
    position: relative;
    left: 50%;
    top: 15%;
  }

.logo {
    width: 120px;
    height: 120px;
    position: relative;
    left: 33%;
    margin-top: 10%;
    
}
.toRegister,
.forgotPassword {
    position: absolute;
    color: rgb(255, 255, 255);
    font-family: Montserrat;
    font-size: 16px;
    font-weight: 400;
    line-height: 20px;
    letter-spacing: 0px;
    text-align: center;
    text-decoration-line: underline;
    opacity: 0.5;
    cursor: pointer;
    border-radius: 10px;
}

.toRegister:active,
.forgotPassword:active {
    background-color: rgb(30, 208, 131);
}

.toRegister {
    width: 80px;
    height: 20px;
    left: 256px;
    top: 7px;
}

.forgotPassword {
    width: 146px;
    height: 20px;
    left: 179px;
    top: 443px;
}

.login-input {
    position: relative;
    width: 300px;
    height: 44px;
    left: 25px;

    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: flex-start;
    gap: 19;
    padding: 12px;
    
    box-sizing: border-box;
    border: 1px solid rgb(255, 255, 255);
    border-radius: 4px;

    box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);

    color: rgb(0, 0, 0);
    font-family: Georgia;
    font-size: 14px;
    font-weight: 300;
    line-height: 20px;
    letter-spacing: 0px;
    text-align: left;
    padding-left: 5%;
}

.login-button {
    position: absolute;
    width: 300px;
    height: 45px;
    left: 25px;
    top: 387px;
    border-radius: 4px;
    box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.3);
    background: rgb(255, 255, 255);
}


</style>