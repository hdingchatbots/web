#https://studygyaan.com/python/create-web-based-chatbot-in-python-django-flask

#https://www.svgrepo.com/svg/190334/chat

#https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html


strReturn = "<br/>"

def get_str_image(strFilePath, strFileName):
    strRes = "<img src='" + strFilePath + strFileName + "'>"
    return strRes

def get_str_hyperlink(strHttpWebsite, strWebsiteName):
    strRes = '<a href="' + strHttpWebsite + '">' + strWebsiteName + '</a>'
    return strRes

def chatbot(userText):
    tStrImage = "D:\z_chatbot_whiplash\m_x_stickers\Chatbot_UI\chatbot_001.png"
        
    #<img src="{{ url_for('static', filename='/img/user/' + profilePic) }}" />
    tStr = '<img src="' + "{{ url_for('static', filename='images/chatbot_001.png') }}" + '"/>'
    tStr1 = "<img src='./static/my_images/ai_003.png'/>"
    tStr2 = "<img src='/static/my_images/ai_003.png'/>"
    tstr3 = '<a href="https://www.google.com"> www.google.com</a>'
    
    tStr4 = "<img src='/static/my_images/ICA_Tribal-Dragon-26_01_s.svg'>" 
    strPath = '/static/my_images/'
    strFileName = 'ICA_Tribal-Dragon-26_01_s.svg'
    strImage = get_str_image(strPath, strFileName)
    strHyperLine = get_str_hyperlink('https://www.google.com', "Google")
    
    tStr = "Testing. www.google.com" + strReturn + "HD:Test. Input Msg: "  + strReturn + userText + strReturn + tStr1 + strReturn + strHyperLine + strReturn + strImage
    
    tStr = "Testing." 
    return tStr

from flask import Flask, render_template, request, redirect, url_for

#HD Step 1, Flask initialisation
app = Flask(__name__)
app.static_folder = 'static'

#@app.route('/results/<path:filename>')

# HD Step 2: The basic home page
@app.route("/")
def my_home_page():
    #return render_template("index.html")
    
    #X:\My Drive\z_chatbot_ica\m_PythonCodes\templates\my_chatbot_ui_04.html
    return render_template("my_chatbot_ui_04.html")

#HD Step 3
#@app.route("/get")
@app.route("/get", methods=["GET","POST"])
def get_bot_response():
    userText = request.args.get('msg')
    return chatbot(userText)

#HD Step 4
if __name__ == "__main__":
    app.run()
