<p align="center">
<img src="https://github.com/AM1CODES/Emotional-Recommender/blob/main/EMOR3C%20-%20Logo%20Transparent.png" alt="drawing" width="300"/>
</p>

# EmoR3c - Emotional-Recommender

We all listen to music almost everyday. We listen to music while we are programming, during our workouts, while editing, etc. Music is an integral part of everyone's life but sometimes it can get really difficult to choose the right music that you really enjoy. We browse through these different apps searching for the right music which might take up some of our time. So what if we could get music recommendations based on our emotions? Let me introduce EmoR3c, a GUI based recommender that recommends songs to the user based on their emotions.

# How was it built?
EmoR3c is the result of lot of researching, working, editing, programming and experimenting. The process was long but i will try to break it down in the best way possible so that anyone who wishes to build a similar project has a sort of road map. Let's begin - </br>
* I started off by creating my Emotion detection model, this was by far the toughest thing. I used FER2013 competition data which wasn't very great and i had to do lot of experimentation and research inorder to get the right model working. I created around 9-10 models before getting an optimal model. After i had my model, i exported it in an 'h5' format.
* The next step was to start working with OpenCV to detect emotions using the webcam. The model would detect the emotions and would return the result. The result is the probability of a particular class out of the 7 classes of emotions we had.
* Next, we needed data of songs that we would recommend to the user. There were literally no data set available for this purpose. So i had to create my own. I used the 'Spotipy' library to scrape song data into JSON files from Spotify playlists. I had a playlist with songs for each class of emotion that we would use to recommend the songs. For example, i had a playlist of calming songs for someone who's feeling angry and so on. I also converted these JSON files to excel for anyone hwo might like to use them.
* Once, we had all of our seperate components, i connected all of these using Tkinter to create a GUI application that the user could use to detect the emotions and get song recommendations. It would return a list of song based on the emotion detected and using the buttons, the user could go to Spotify or Youtube Music to stream these songs.</br>

And that's how EmoR3c was built. It seems very simple and easy to build but it does take a lot of time with all the researching and experimentation.

# Information about the Data set
The data set used was FER2013 competition data set that i used for emotion detection. The dataset has 35685 images. All of these images are of size 48x48 pixel and are in grayscale. It contains images of 7 categories of emotions. For song recommendations, i used a custom data set which is included in the repository. It contains song's data taken from spotify playlists.

FER 2013 emotions data - https://www.kaggle.com/ananthu017/emotion-detection-fer

# Some Results
Here are some of the results from the project - </br>
* Model Results - 
<p align="center">
<img src="https://github.com/AM1CODES/Emotional-Recommender/blob/main/Result%20-%203.png" alt="drawing" width="500"/>
</p>
<p align="center">
<img src="https://github.com/AM1CODES/Emotional-Recommender/blob/main/Result%20-%204.png" alt="drawing" width="500"/>
</p>
<p align="center">
<img src="https://github.com/AM1CODES/Emotional-Recommender/blob/main/Result%20-%205.png" alt="drawing" width="500"/>
</p>

* GUI Application -
<p align="center">
<img src="https://github.com/AM1CODES/Emotional-Recommender/blob/main/Result%20-%201.PNG" alt="drawing" width="700"/>
</p>
<p align="center">
<img src="https://github.com/AM1CODES/Emotional-Recommender/blob/main/Result%20-%202.PNG" alt="drawing" width="700"/>
</p>

# Future Plans
EmoR3c is an Open source  project and i have a few ideas that would make this project even better. I will create issues for the same later. For now, these are the future additions that will help in upgrading this project - 
* Web App - Currently, the project is a GUI application but it would look much better as a web app instead of a GUI application. It will also give us more opportunity for styling and make the whole application look even better.
* Better Recommender - We can use the already available Spotify dataset to use features like Danceability and some other similar features to recommend songs instead of using the playlist data and human connect. 
