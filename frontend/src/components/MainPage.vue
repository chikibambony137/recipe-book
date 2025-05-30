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

      <h3 v-if="isNotFound">По данному запросу ничего не найдено!</h3>
      <RecipeList :recipes="recipes" />
      

      <AddRecipeForm v-if="isAddRecipeModalOpen"></AddRecipeForm>

   </div>
</template>

<script>
   import RecipeList from './recipeList.vue';
   import AddRecipeForm from './addRecipeForm.vue';
   import Config from "./config.js"

   export default {
      components: { RecipeList, AddRecipeForm },

      data() {
         return {
            isOpen: false,
            isAddRecipeModalOpen: false,
            API_URL: Config.api,
            recipes: [],
            searchQuery: "",
            isNotFound: false,
         }
      },

      methods: {
         toggleMenu() {
            this.isOpen = !this.isOpen;
         },
         
         openAddRecipeModal() {
            this.isAddRecipeModalOpen = true;
         },

         async fetchRecipes() {
            // Получаем токен из localStorage
            const token = localStorage.getItem('access_token');

            // Если токена нет, перенаправляем пользователя для авторизации или уведомляем об этом
            if (!token) {
               alert('Авторизуйтесь');
               this.$router.push('/login');
            }

            const response = await fetch(`${this.API_URL}/recipes`);

            if (response.status === 401) {
                  alert('Сессия истекла. Пожалуйста, авторизуйтесь заново');
                  localStorage.removeItem('access_token');
                  this.$router.push('/login');
            }

            if (!response.ok) {
                  const errorData = await response.json();
                  throw new Error(errorData.detail || 'Ошибка при отображении рецептов');
            }

            this.recipes = await response.json();
         },

         async searchRecipe() {
            const response = await fetch(`${this.API_URL}/recipe?search=${this.searchQuery}`);
            if (!response.ok) {
               throw new Error('Network response was not ok');
            }
            
            this.recipes = await response.json();

            if (this.recipes.length === 0)
            {
               this.isNotFound = true;
            }
            else {
               this.isNotFound = false;
            }
            
         },
      },

      mounted() {
         this.fetchRecipes();
      }
   }
</script>

<style scoped>

   .background {
      position: absolute;
      width: 762px;
      height: 90%;
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
      z-index: 0;
   }

   .bar {
      position: static;
      width: 100%;
      height: 11%;
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

   h3 {
      color: rgb(185, 185, 185);
      font-family: 'Segoe UI'; 
   }

</style>