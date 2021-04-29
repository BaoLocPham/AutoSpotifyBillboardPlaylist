# SpotifyAutoBillboardPlaylist
This project is implement web-scraping and using spotipy library

the billboard url: https://www.billboard.com/charts/hot-100/

1. In order to create a playlist in Spotify you must have an account with Spotify. If you don't already have an account, you can sign up for a free one here: http://spotify.com/signup/

2. Once you've signed up/ signed in, go to the developer dashboard and create a new Spotify App:

https://developer.spotify.com/dashboard/
<img width="700" height="500" alt="step1" src="https://user-images.githubusercontent.com/67360122/116534017-3b07ca00-a90c-11eb-8ca1-3d1287a3ec10.png">


3. Once you've created a Spotify app, copy the Client ID and Client Secret into your Python project.
<img width="1451" alt="step3" src="https://user-images.githubusercontent.com/67360122/116534048-4529c880-a90c-11eb-8455-bdea727795c3.png">

4. Use http://example.com as your Redirect URI. You're looking to get the currentuser id (your Spotify username). As per the documentation, make sure you set the redirect URI in the Spotify Dashboard as well.

![step4](https://user-images.githubusercontent.com/67360122/116534561-def17580-a90c-11eb-8c14-4a4daaccadfe.png)
![step5](https://user-images.githubusercontent.com/67360122/116534582-e7e24700-a90c-11eb-98d4-9f592df5f87c.png)

5.  If successful, you should see the page below show up automatically (be sure to click Agree):
<img width="640" height="500" alt="step6" src="https://user-images.githubusercontent.com/67360122/116534332-96d25300-a90c-11eb-88f9-8612348ade08.png">
<img width="1504" alt="step7" src="https://user-images.githubusercontent.com/67360122/116534342-9934ad00-a90c-11eb-9c88-c56f0c569163.png">

6. Paste the copied URL into terminal prompt
![step8 1](https://user-images.githubusercontent.com/67360122/116535700-3d6b2380-a90e-11eb-89e2-2c30a5d1ff18.PNG)

7. Because there are song  unavailable on spotify, so we skip those songs
![Video_21-04-29_17-22-30](https://user-images.githubusercontent.com/67360122/116536836-a4d5a300-a90f-11eb-85e9-fb43e41a417c.gif)

8. The Result Ta da~~
![Video_21-04-29_17-34-59](https://user-images.githubusercontent.com/67360122/116538054-3d205780-a911-11eb-8d75-09c693c5be38.gif)
