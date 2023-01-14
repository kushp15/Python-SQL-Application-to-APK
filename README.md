# Python-Sql Application converting to APK

Using pymysql instead of Mysql module:

If you were trying to use mysql into your application it will crash, so use pymysql to access mysql server. I used mysql and its crashes after deploying into apk file since there is no recipie for it. But using an pymysql module, it will be easy to convert into apk file without crash. 


Converting an python file to apk with using an kivymd and pymysql.

Using the google colab, run the command below to convert the python file to apk without crash. 

Installing buildozer:

1) !pip install buildozer

Installing Cython, use the latest version of cython:

2) !pip install cython==0.29.32

Installing supported libs:

3) !sudo apt-get install -y \
    python3-pip \
    build-essential \
    git \
    python3 \
    python3-dev \
    ffmpeg \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev

4) !sudo apt-get install -y \
    libgstreamer1.0 \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good


5) !sudo apt-get install build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev zlib1g-dev libssl-dev openssl libgdbm-dev libgdbm-compat-dev liblzma-dev libreadline-dev libncursesw5-dev libffi-dev uuid-dev libffi6

6) !sudo apt-get install libffi-dev

Make sure to drag all python and kivy files with supporting files before running below command. After running BUILDOZER INIT you get an buildozer.spec file. 
You will be editing that file according to your project requirenment:

7) !buildozer init

The below command will debug the code and convert into apk file:

8) !buildozer -v android debug
