<script>
    import Config from "./config.js"

    export default {
        data() {
            return {
                API_URL: Config.api,
                login: '',
                password: '',
                password2: ''
            };
        },
        methods: {
            async Register() {
                try {
                    if (this.password == this.password2){
                        const response = await fetch(`${this.API_URL}/register`, {
                            method: 'POST',
                            body: new URLSearchParams({
                                username: this.login,
                                password: this.password,
                            }).toString(),
                            headers: {
                                'Content-Type': 'application/x-www-form-urlencoded',
                            },
                        });

                        if (!response.ok) {
                            const errorData = await response.json();
                            throw new Error(errorData.detail || 'Ошибка при авторизации');
                        }

                        alert(`Пользователь "${this.login}" зарегистрирован`)

                        this.$router.push('/login')
                    }
                    else {
                        alert('Пароли не совпадают!')
                    }
                } catch (error) {
                    alert('Ошибка: ' + error.message);
                }
            },

            goToLogin() {
                this.$router.push('/login')
            },
        },
}
</script>

<template>
    <div class="regForm">
        <div>
            <a class="toLogin" @click="goToLogin"><u>Login ></u></a>
            <img src="..\assets\food.png" class="logo"/>
        </div>
        <div>
            <form @submit.prevent="Register">
                <p><input type="login" class="reg-input" v-model="login" placeholder="Login / Email" maxlength=50/></p>
                <p><input type="password" class="reg-input" v-model="password" placeholder="Password" maxlength=50/></p>
                <p><input type="password" class="reg-input" v-model="password2" placeholder="Password again" maxlength=50/></p>
                <p><button type="submit" class="reg-button">Register</button></p>
            </form>
        </div>        
    </div>

</template>

<style scoped>

.regForm {
    background-color: #1f39ae;
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
.toLogin {
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

    width: 80px;
    height: 20px;
    left: 256px;
    top: 7px;
}

.toLogin:active {
    background-color: rgb(30, 208, 131);
}

.reg-input {
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

.reg-button {
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