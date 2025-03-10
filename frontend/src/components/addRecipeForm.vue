<template>
<div>
    <div class="overlay"></div>

    <div v-if="isAddRecipeModalOpen"  class="add-recipe-modal">
        <h3>Добавить рецепт</h3>

        <form @submit.prevent="addRecipe" style="text-align: right; padding-right: 20px; ;">
            <label for="name">Название:</label>
            <input id="name" v-model="newRecipeName" 
             required placeholder="Название" 
             style="margin: 5px;"
             autocomplete="off"/>

            <label for="description">Описание:</label>
            <input id="description" v-model="newRecipeDescription" 
             required placeholder="Описание" 
             style="margin: 5px"
             autocomplete="off"/>
            
            <label for="diff">Сложность:</label>
            <input id="diff" v-model="newRecipeDifficulty" type="number"
             required placeholder="Сложность" 
             style="margin: 5px; width: 162px;"
             min="1" max="10" step="1"/>

            <button type="submit" style="margin: 5px; margin-top: 20px;">Добавить рецепт</button>
            <button @click="closeAddRecipeModal" style="margin: 5px">Закрыть</button>  

        </form>

    </div>
</div>


</template>

<script>
import Config from "./config.js"

export default {
    data() {
        return {
            API_URL: Config.api,
            isAddRecipeModalOpen: true,
            newRecipeName: '',
            newRecipeDescription: '',
            newRecipeDifficulty: 1
        }
    },

    methods: {
        async addRecipe() {
            const response = await fetch(`${this.API_URL}/add_recipe`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    name: this.newRecipeName,
                    description: this.newRecipeDescription,
                    difficulty: this.newRecipeDifficulty
                })
                });
            const result = await response.json();
            this.closeAddRecipeModal();
            alert('Рецепт успешно добавлен!');
            window.location.reload();
        },

        closeAddRecipeModal() {
            document.querySelector('.overlay').style.display = 'none';
            this.$parent.isAddRecipeModalOpen = false;
        },
    }
}
</script>

<style>
input[type="range"] {
    appearance: none;
    background-color: rgb(8, 194, 8);
    border-radius: 10px;
    cursor: pointer;
    
}

.add-recipe-modal {
    background: rgb(41, 43, 167);
    border-color: rgb(33, 35, 102);

    border-style: solid;
    border-width: 3px;
    border-radius: 10px;

    width: 300px;
    height: 300px;

    position: fixed;
    left: 41%;
    top: 20%;
    text-align: center;
    z-index: 2;
    padding: 5px;
}

.add-recipe-modal h3 {
    color: rgb(211, 203, 203);
}

.overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5); /* Полупрозрачный черный цвет */
    display: none; /* Скрыто по умолчанию */
    z-index: 1; /* Размещаем ниже модального окна */

    display: block;
}
</style>