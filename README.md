installation 
1. create env by using command    python3 -m venv env  
2. activate env.   source env/bin/activate    
3. install requirements  pip install -r requirements.txt
4. migrate to DB  python manage.py migrate
5. run server python manage.py runserver



Api docs


List of api’s 

1.	Registration:
 <br />
url: {baseUrl}/register/
 <br />
method: POST
 <br />
No Auth Required
 <br />
body = { 
“email”:asdasd@gmail.com,
“password”: “123123Lol!”
}
 <br />

2.	Login
url: {baseUrl}/login /,
method: POST
No Auth Required
body = { 
“email”:asdasd@gmail.com,
“password”: “123123Lol!”}

3.	User statistics
url: {baseUrl}/get_user_statistics/ ,
method: GET,
No Auth Required
Params = { 
“email”:asdasd@gmail.com}

4. Create a Post 
url: {baseUrl}/post/create_post/ ,
method: POST,
Auth Required,
Headers = {
«Content-Type»: «application/json»,
«Authorization» «Token 0857e584d3f3a5afe5904344b5b56d25737def99»
}
Body = {
«title»: «13123»,
«body»: «adds»
}

Or several post could be created by sending 
Body = [{«title»: «13123»,«body»: «adds»}, {«title»: «and»,«body»: «fa»}]

5. Like a Post / Unlike a post    // if you send a request for the first time it will like the post, for the second time request sending it will unlike post
url: {baseUrl}/post/like_post/ ,
method: POST,
Auth Required,
Headers = {
«Content-Type»: «application/json»,
«Authorization» «Token 0857e584d3f3a5afe5904344b5b56d25737def99»
}

Body = {
«post»: «260ccadc-11b2-497e-9aa3-d4113b87d5e3» /// post_id,
}


6.Bulk  Like  of posts Post 
url: {baseUrl}/post/bulk_post_like/ ,
method: POST,
Auth Required,
Headers = {
«Content-Type»: «application/json»,
«Authorization» «Token 0857e584d3f3a5afe5904344b5b56d25737def99»
}
Body = {
[{«post»: «260ccadc-11b2-497e-9aa3-d4113b87d5e3»},{«post»: «fe889e44-a752-4566-a9c9-8b1efcd7d6a4»}] ,
}
	

7. Get likes statistics
url: {baseUrl}/post/get_like_statistics/ ,
method: GET,
Auth Required,
Headers = {
«Content-Type»: «application/json»,
«Authorization» «Token 0857e584d3f3a5afe5904344b5b56d25737def99»
}
Params = {
«date_from» : «2020-01-01»,
«date_to» : «2022-01-01»,

}
