from flask import Flask, redirect, request, render_template
from instagramy import InstagramUser


app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')
@app.route('/kol',  methods = ["POST","GET"])
def kol():
    user = " "
    usrname = str(request.form.get("usrname"))
    print(usrname)
    # session_ig = ["48420109999%3AwYTofPNHOHFmPo%3A15%3AAYdePiWOn0bg3xhjxthCXGZ4ogwQzl2hbuT-QFLjbw" , "51669758945%3AQXe1CxsKaeEl0Z%3A14%3AAYcitzOLUpfaaC582rAfRbhWnz_5QSUIPnSNdhQYOQ"]
    session_id = "51669758945%3AeaoE7wCFnfMUUz%3A20%3AAYeauCt70M82lH0aKr9c-h3ZnUmHS5lgY6fKsNQGyw"
    try:
        user = InstagramUser(usrname, sessionid=session_id)
        print("user : ", user)
    except:
        print("user : ", user)
        return render_template("index.html")
    user = InstagramUser(usrname, sessionid=session_id)
    ig_user = user.fullname
    follower = user.number_of_followers
    Photo = user.profile_picture_url
    verified = user.is_verified
    print(user.number_of_followers)
    print(user.profile_picture_url)
    # print(user.posts)
    return render_template("index.html",
                           name = ig_user,
                           followers = follower,
                           url_photo = Photo,
                           is_verified = verified)
    

if __name__ == "__main__":
    app.run(debug=True)