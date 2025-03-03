
<script>
export default {
   data() {
      return {
         API_URL: 'http://localhost:8000',
         isOpen: false,
         recipes: [],
         searchQuery: '',
         isAddRecipeModalOpen: false,
         newRecipeName: '',
         newRecipeDescription: '',
         newRecipeDifficulty: 1
      }
   },

   methods: {
      toggleMenu() {
         this.isOpen = !this.isOpen;
      },
      
      async fetchRecipes() {
         const response = await fetch(`${this.API_URL}/recipes`);
         if (!response.ok) {
               throw new Error('Network response was not ok');
            }
         this.recipes = await response.json();
      },

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
         alert('Рецепт успешно добавлен!')
         window.location.reload()
      },
      openAddRecipeModal() {
         this.isAddRecipeModalOpen = true;
         document.querySelector('.overlay').style.display = 'block';
      },
      closeAddRecipeModal() {
         document.querySelector('.overlay').style.display = 'none';
         this.isAddRecipeModalOpen = false;
      },
      searchRecipe() {
         // Добавьте логику для поиска
      }
   },

   mounted() {
      this.fetchRecipes();
   },

   computed: {
      filteredRecipes() {
         return this.recipes.filter(recipe => recipe.name.includes(this.searchQuery));
      }
   }
}
</script>   

<template>
   <div class="background">
      <div class="bar">
         <div class="menu-div" @click="toggleMenu">
            <span class="line" v-bind:class="{ open: isOpen }"></span>
            <span class="line" v-bind:class="{ open: isOpen }"></span>
            <span class="line" v-bind:class="{ open: isOpen }"></span>
         </div>

         <div class="search-div">
            <input type="search" class="search-input" placeholder="Найти рецепт" v-model="searchQuery"/>
            <button class="filter-bttn"></button>
            <button class="search-bttn" @click="searchRecipe"></button>
         </div>

         <button class="add-recipe-bttn" @click="openAddRecipeModal">Добавить</button>

         <div class="profile-div">a</div>
      </div>

      <div class="recipe-list-div">
         <div v-for="recipe in recipes" :key="recipe.id" class="recipe">
            <h3>{{ recipe.name }}</h3>

            <label for="diff">Сложность:</label> 
            <a>1</a><input type="range" step="1" min="0" max="10" :value=recipe.difficulty id="diff" disabled /><a>10</a>

            <p>{{ recipe.description }}</p>
            
         </div>
      </div>

      <div class="overlay"></div>

      <div v-if="isAddRecipeModalOpen"  class="add-recipe-modal">
         <input v-model="newRecipeName" placeholder="Название"/>
         <input v-model="newRecipeDescription" placeholder="Описание"/>
         <input v-model="newRecipeDifficulty" type="number" placeholder="Сложность"/>
         <button @click="addRecipe">Добавить рецепт</button>
         <button @click="closeAddRecipeModal">Закрыть</button>
      </div>


   </div>
</template>

<style scoped>
   .background {
      position: absolute;
      width: 762px;
      height: 1020px;
      left: 25%;
      top: 4%;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      align-items: center;
      gap: 10;
      padding: 15px;
      padding-top: 10px;

      border-radius: 20px;
      background: rgb(31, 66, 174);
   }

   .bar {
      position: static;
      width: 100%;
      height: 6.75%;
      display: flex;
      order: 0;
      align-self: stretch;
      flex-grow: 0;
      margin: 10px 0px;
      padding: 10px;

      box-sizing: border-box;
      /* - полезная хуйня (учитывает отступы в ширине) */

      border-radius: 20px;
      background: rgb(25, 57, 156);
   }

   .menu-div {
      width: 5.75%;
      height: 77%;
      border-radius: 10px;
      cursor: pointer;
      background: rgb(31, 66, 174);
      padding: 6px 2px;

      border-radius: 10px;
      align-content: center;
   }

   .menu-div:hover {
      background: rgb(0, 144, 103);
   }

   .line {
      display: block;
      width: 33px;
      height: 4px;
      margin: 5px;
      background-color: white;
      transition: all 0.3s ease;
      
   }

   .line.open:nth-child(1) {
      transform: rotate(45deg) translate(7px, 7px);
   }

   .line.open:nth-child(2) {
      opacity: 0;
   }

   .line.open:nth-child(3) {
      transform: rotate(-45deg) translate(5px, -5px);
   }

   .search-div {
      position: relative;
      width: 60%;
      height: 80%;
      margin-left: 10%;
      margin-top: 0.5%;
      padding: 2px;

      border-radius: 10px;
      background: rgb(255, 255, 255);

   }

   .search-input {
      width: 78%;
      height: 100%;
      border: 0px;
      border-radius: 10px;
      border-color: rgb(76, 76, 194);

      align-items: center;
      color: rgb(0, 0, 0);
      font-family: Georgia;
      font-style: italic;
      font-size: 16px;
      font-weight: 400;
      line-height: 20px;
      letter-spacing: 0px;
      text-align: left;

      padding-left: 5%;
   }

   .search-input:focus {
      background-color: rgb(201, 201, 201);
   }

   .filter-bttn {
      position: absolute;
      width: 39px;
      height: 91%;
      left: 80%;

      border: 0px;
      background: rgb(255, 255, 255);
      background-image: url("../assets/filter.png");
      background-size: cover;
      border-radius: 5px;
      cursor: pointer;
   }
   .filter-bttn:hover {
      background: rgb(201, 201, 201);
      background-image: url("../assets/filter.png");
      background-size: cover;
      border: 2px;
      border-style:solid;
      border-color: rgb(27, 27, 27);
   }

   .search-bttn {
      position: absolute;
      width: 39px;
      height: 91%;
      left: 90%;
      border: 0px;
      background: rgb(255, 255, 255);
      background-image: url("../assets/searchicon.png");
      background-size: 80%;
      background-repeat: no-repeat;
      background-position: 3px;
      border-radius: 5px;
      cursor: pointer;

      border-radius: 10px;
   }

   .search-bttn:hover {
      background: rgb(201, 201, 201);
      background-image: url("../assets/searchicon.png");
      background-size: cover;
      border: 2px;
      border-style:solid;
      border-color: rgb(27, 27, 27);
   }

   .add-recipe-bttn {
      position: relative;
      width: 15%;
      height: 85%;
      margin-top: 0.65%;
      margin-left: 4%;

      border: 0px;
      border-radius: 10px;
      background: rgba(8,255,70,1);

      color: rgb(3, 3, 3);
      font-family: Arial;
      font-size: 16px;
      font-weight: 500;
      line-height: 20px;
      letter-spacing: 0px;
      text-align: center;
      cursor: pointer;
   }

   .add-recipe-bttn:hover {
      background: rgba(1,161,41,1);
   }

   .profile-div {
      background: rgb(36, 75, 197);
      border-radius: 50%;
      position: relative;
      width: 48px;
      height: 48px;
      margin-left: 3%;
      cursor: pointer;

      color: rgb(255, 255, 255);
      font-family: Arial;
      font-size: 28px;
      font-weight: 700;
      line-height: 20px;
      letter-spacing: 0px;
      text-align: center;
      align-content: center;
      text-transform: uppercase;
   }

   .recipe-list-div {
      box-sizing: border-box;
      width: 100%;
      height: auto;
      padding: 20px;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      overflow: auto;
      
   }

   .recipe {
      border-radius: 10px;
      background: rgb(25, 57, 156);
      width: 47%;
      height: 300px;
      position: relative;
      margin: 10px;

      text-align: center;

   }

   .recipe h3, label, p, a {
      color: rgb(219, 219, 219);
   }

   input[type="range"] {
      appearance: none;
      background-color: rgb(8, 194, 8);
      border-radius: 10px;
      cursor: pointer;
      
   }

   .add-recipe-modal {
      background: red;
      width: 300px;
      height: 300px;

      position: fixed;
      left: 41%;
      top: 20%;
      text-align: center;
      z-index: 2;
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
   }

</style>