<template>
    <div id="body">
        <div id="header">
            <h1></h1>
            <div id="nav">
                <ul>
                    <li><a href="#">g</a></li>
                    <li><a href="#">fdgfdgfdg</a></li>
                    <li><a href="#">fgdfgfdgfddfgfdgd</a></li>

                </ul>
            </div>
        </div>
        <div class="main">

            <div id="sidebar1" class="aside">
                
            </div>

            <div id="sidebar2" class="aside">
                
            </div>

            <div id="article">
                
            </div>

        </div>

        <div id="footer">
            <p></p>
            <p></p>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style>
    * {
        box-sizing: border-box;
    }
    html, body, div, span, h1, h2, h3, h4, h5, h6, p, a, ul, li{
                    
        margin: 0;
        padding: 0;
        border: 0;
        font-size: 100%;
        vertical-align: baseline;
    }
    #body {
        position: absolute;
        left: 0px;
        top: 0px;
        font-family: Verdana, Arial, sans-serif;    
        width: 100%;
        background-color: blue;
    }
    #header{ 
        width: 100%;
    }
    #header h1 {
        font-size: 24px;
        text-transform: uppercase;
        font-weight: bold;
        padding: 30px 30px 30px 10px;
        clear: both;
    }
    #nav {
        border-top: 1px solid ;
        border-bottom: 1px solid ;
    }
    #nav li {
        float: left;
        list-style: none;   
    }
    #nav a {
        display: block;
        color: black;
        padding: 10px 25px;
        text-decoration: none;
        border-right: 1px solid ;
    }
    #nav li:last-child a {
        border-right: none; 
    }
    #nav a:hover {
        font-weight: bold;
    }
    #nav:after {
        content: " ";
        display: table;
        clear: both;
    }
    .main{

    }
    .aside h2 {
        font-size: 0.95em;
        margin-top: 15px;
    }
    .aside h3 {
        font-size: 0.85em;
        margin-top: 10px;
    }
    .aside p, .aside li {
        font-size: .75em;
        margin-top: 10px;   
    }
    .aside li{ 
        list-style-type: none;
    }
    #sidebar1 {
        float: left;
        width: 20%; 
        padding: 0 10px 0 20px;
    }
    #sidebar2 {
        float: right;
        width: 20%; 
        padding: 0 20px 0 10px;
    }
    #article{

        border-left: 1px solid ;
        border-right: 1px solid ;
        margin-left: 20%;
        margin-right: 20%;
        padding: 15px;
        width: 60%;
    }
    #article:after{
        clear:both;
        display:table;
        content:'';
    }
    #article h2{
        font-size: 1.3em;
        margin-bottom:15px;
    }
    #article p{
        line-height: 150%;
        margin-bottom: 15px;
    }
    #footer{ 
        border-top: 1px solid ;
        font-size: .8em;    
        text-align: center;
        padding: 10px 10px 30px 10px;
    }
    #nav ul, #header h1, .main, #footer p {
        max-width: 1200px;
        margin: 0 auto; 
    }
    .main, #nav, #header, #footer{
        min-width: 768px;
    }
</style>