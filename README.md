<p align="center">
  <img width="1000" height="300" src="https://github.com/rafadedubra/python-mongodb-rest-Api/blob/main/naruto-shippuden.jpg" alt="Sentiment analysis">
</p>

# API de Naruto
En esto proyecto creo una API de Naruto que permite obtener información de una base de datos que contiene frases que han dicho los personajes ordenadas por grupos como si fuera una conversación.<br>
También analizo los sentimientos de los personajes mediante el procesamiento del lenguaje natural (NLTK) <br>

# Endpoints
<h2>@GET<h2>
<ul><li> /users</li></ul>
<p>Con este endpoint se obtienen todos los personajes</p>
<ul><li> /users/id </li></ul>
<p>Con este endpoint se obtiene un personaje por su id</p>
<ul><li> /chat </li></ul>
<p>Con este endpoint se obtienen las conversaciones de los personajes</p>
<ul><li> /chat/id </li></ul>
<p>Con este endpoint se obtienen las conversaciones de los personajes por id</p>
<br>
<h2>@POST<h2>
<ul><li> /users </li></ul>
<p>Con este endpoint se inserta un usuario/personaje</p>
<ul><li> /chat </li></ul>
<p>Con este endpoint se inserta la conversación de un personaje</p>
<br>
<h2>@DELETE<h2>
<ul><li> /users/id </li></ul>
<p>Con este endpoint se borra un usuario/personaje por id</p>
<ul><li> /chat/id </li></ul>
<p>Con este endpoint se borra la conversación de un personaje por id</p>
<br>
<h2>@PUT<h2>
<ul><li> /users/id </li></ul>
<p>Con este endpoint se actualiza un usuario/personaje por id</p>
<ul><li> /chat/id </li></ul>
<p>Con este endpoint se actualiza la conversación de un personaje por id</p>



