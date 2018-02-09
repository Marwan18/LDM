from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import threading
import webbrowser
from PyQt5.uic import loadUiType
from os import path
import urllib.request
from Calculator import *
import pafy
import humanize
import os



From_Desgin,_ = loadUiType(path.join(path.dirname(__file__),"LuckyDM.ui"))

class Window(SS,From_Desgin):
    def __init__(self, parent = None):

        super(Window,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(861,387)
        self.Buttons_Actions()
        self.statusBar()
        self.StatusTip()
        self.setWindowTitle("LDM ")
        self.setWindowIcon(QIcon("Lucky.png"))
        self.line_1.setPlaceholderText("Enter The Video URL")
        self.line_2.setPlaceholderText("Enter The Video Location")
        self.line_5.setPlaceholderText("Enter The Playlist URL")
        self.line_6.setPlaceholderText("Enter The Playlist Location")
        self.btn1.setToolTip("Start Download")
        self.mainmenu = QMenuBar(self)
        self.Filemenu = self.mainmenu.addMenu("File")
        self.E_Aciton = QAction("Exit",self)
        self.Filemenu.addAction(self.E_Aciton)
        self.E_Aciton.triggered.connect(self.Close_App)








        self.show()

    def Quality(self):
        if self.line_1.text() == "" :
            self.comboBox.clear()

        else:

            self.video = pafy.new("https://www.youtube.com/watch?v=q6YkcNgTOxk")
            self.stream = self.video.videostreams
            self.lis = []
            for i in self.stream:
                size = humanize.naturalsize(i.get_filesize())
                h = "{} {} {} {}".format(i.mediatype, i.extension, i.quality, size)
                self.comboBox.addItem(h)


    def Download_From_Youtube(self):

        try:
            self.Url = self.line_1.text()
            self.video = pafy.new(self.Url)
            self.stream = self.video.videostreams
            self.Save_youtube_location = self.line_2.text()
            self.quality = self.comboBox.currentIndex()
            self.download = self.stream[self.quality].download(filepath=self.Save_youtube_location)
            self.box = QMessageBox.about(self,"LDM","Download Finshed")
            if self.CheckBox.isChecked() :
                self.close()
        except Exception:
            box = QMessageBox.warning(self,"LDM","Please Check Your video Url \n or \n This video Already Has Been Downloaded in This Path ...")
    def Youtube_Browse(self):
        self.Save_youtube_location = QFileDialog.getExistingDirectory(self,"Save Location")
        self.line_2.setText(self.Save_youtube_location)
    def Youtube_Browse2(self):
        self.Save_Playlist_Location = QFileDialog.getExistingDirectory(self,"Save Location")
        self.line_6.setText(self.Save_Playlist_Location)

    def Google(self):
        webbrowser.open_new("http://www.google.com")
    def Youtube(self):
        webbrowser.open_new("http://www.youtube.com")
    def Instagram(self):
        webbrowser.open_new("http://www.instagram.com")
    def Twitter(self):
        webbrowser.open_new("http://www.twitter.com")
    def Facebook(self):
        webbrowser.open_new("http://www.facebook.com")
    def calculator(self):
        SS.__init__(self)

    def Info(self):
        Info = QMessageBox.information(self,"Welcome"," Coded By <Marwan>")

    def Progress(self, blocknum , blocksize ,totalsize):
        self.File_Downloaded = blocknum * blocksize
        if totalsize > 0 :
            percent = (self.File_Downloaded *100) / totalsize
            self.progressBar.setValue(percent)




    def Browse(self):
        self.Save_location = QFileDialog.getSaveFileName(self,caption="Save AS",directory=".",filter="All Files (*.*)")
        p = list(self.Save_location)[0:1]
        s = str(p).replace("[", "")
        h = s.replace("]", "")
        f = h.replace("'", "")
        self.line_2.setText(f)
    def StatusTip(self):
        self.btn1.setStatusTip("Start Download")
        self.btn2.setStatusTip("Close")
        self.btn3.setStatusTip("Save Location")
        self.btn4.setStatusTip("Info")
        self.btn5.setStatusTip("Calculator")
        self.btn7.setStatusTip("Close")
        self.btn4.setStatusTip("Info")
        self.btn5.setStatusTip("Calculator")
        self.btn10.setStatusTip("Facebook")
        self.btn11.setStatusTip("Twitter")
        self.btn12.setStatusTip("Youtube")
        self.btn13.setStatusTip("Instagram")
        self.btn14.setStatusTip("Google")
        self.btn21.setStatusTip("Download")
        self.btn22.setStatusTip("Quality")
        self.btn23.setStatusTip("Save Location")
        self.btn10_3.setStatusTip("Facebook")
        self.btn11_3.setStatusTip("Twitter")
        self.btn12_3.setStatusTip("Youtube")
        self.btn13_3.setStatusTip("Instagram")
        self.btn14_3.setStatusTip("Google")
        self.btn4_3.setStatusTip("Info")
        self.btn9_3.setStatusTip("Calculator")
        self.btn7_3.setStatusTip("Close")
        self.btn21_3.setStatusTip("Start Download")
        self.btn23_3.setStatusTip("Save Location")
    def  Buttons_Actions(self):
        self.btn1.clicked.connect(self.Download)
        self.btn2.clicked.connect(self.close)
        self.btn3.clicked.connect(self.Browse)
        self.btn4.clicked.connect(self.Info)
        self.btn5.clicked.connect(self.calculator)
        self.btn7.clicked.connect(self.Close_App)
        self.btn8.clicked.connect(self.Info)
        self.btn9.clicked.connect(self.calculator)
        self.btn10.clicked.connect(self.Facebook)
        self.btn11.clicked.connect(self.Twitter)
        self.btn12.clicked.connect(self.Youtube)
        self.btn13.clicked.connect(self.Instagram)
        self.btn14.clicked.connect(self.Google)
        self.btn21.clicked.connect(self.Download_From_Youtube)
        self.btn22.clicked.connect(self.Quality)
        self.btn23.clicked.connect(self.Youtube_Browse)
        self.btn10_3.clicked.connect(self.Facebook)
        self.btn11_3.clicked.connect(self.Twitter)
        self.btn12_3.clicked.connect(self.Youtube)
        self.btn13_3.clicked.connect(self.Instagram)
        self.btn14_3.clicked.connect(self.Google)
        self.btn4_3.clicked.connect(self.Info)
        self.btn9_3.clicked.connect(self.calculator)
        self.btn7_3.clicked.connect(self.Close_App)
        self.btn21_3.clicked.connect(self.Download_Playlist)
        self.btn23_3.clicked.connect(self.Youtube_Browse2)
    def Download_Playlist(self):
        try:
            PlayList_Url = self.line_5.text()
            Playlist_Location = self.line_6.text()
            Playlist = pafy.get_playlist(PlayList_Url)
            os.chdir(Playlist_Location)
            if os.path.exists(str(Playlist["title"])) :
                os.chdir(str(Playlist["title"]))
            else :
                os.mkdir(str(Playlist["title"]))
                os.chdir(str(Playlist["title"]))
            videos = Playlist["items"]
            for video in videos :
                Video = video["pafy"]
                Best_Quality = Video.getbest()
                Best_Quality.download()
                if self.CheckBox_3.isChecked():
                    self.close()
        except Exception :
            M = QMessageBox.warning(self,"LDM","Please Check The Playlist URL ")


    def Download(self):
        try :
            if self.line_1.text() == "":
                self.QmessageBox = QMessageBox.warning(self, "        LDM          ",
                                                       "Your Download Failed\nPlease Check Your Url !!")
            elif self.line_2.text() == "":
                self.QmessageBox = QMessageBox.warning(self, "        LDM          ",
                                                       "Your Download Failed\nPlease Check Your Save Location !!")
            url = self.line_1.text()
            self.Save_location = self.line_2.text()
            urllib.request.urlretrieve(url , self.Save_location,self.Progress)
            self.QmessageBox = QMessageBox.about(self, "LDM ", "Your Download Finshed")

            if self.CheckBox.isChecked()  :
                self.close()

            else :
                self.show()


        except Exception:
            self.progressBar.setValue(0)
            self.line_1.setText("Ya3m a2deha ^_^")
            webbrowser.open_new("http://www.facebook.com")






if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = Window()
    window.start()
    app.exec_()
