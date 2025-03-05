<template>
    <div class="recipe-list-div">
        <div v-for="recipe in recipes" :key="recipe.id" class="recipe">
            <h3>{{ recipe.name }}</h3>

            <label for="diff">Сложность:</label> 
            <a>1</a><input type="range" step="1" min="0" max="10" :value=recipe.difficulty id="diff" disabled /><a>10</a>

            <p>{{ recipe.description }}</p>
        
        </div>
    </div>
</template>

<script>
export default {
  props: {
    recipes: Array
  }
}
</script>

<style>
    .recipe-list-div {
      box-sizing: border-box;
      width: 100%;
      height: 100%;
      padding: 20px;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      overflow: auto;
      
      z-index: 1;
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
</style>