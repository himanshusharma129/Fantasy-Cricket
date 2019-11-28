import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5 import QtGui
import sqlite3

conn = sqlite3.connect('playersdatabase.db')
class DBhandler:
    def __init__(self):

        self.c = conn.cursor()
        # self.c.execute(""" CREATE TABLE match
        # (player text, scored integer,faced integer,fours integer,
        # sixes integer,bowled integer,maiden integer,
        # given integer,wkts integer,catches integer,stumping integer,ro integer)
        # """)
        # self.c.execute(""" create table stats( player text,
        #  matches integer,runs integer,hundereds integer,fifty integer,
        #  value integer,ctg text)""")
        #
        # self.c.execute("""Create table teams(name text,players text,value integer)""")

        #self.insertDBData()
        #self.c.execute(" Select * from match")
        #print(self.c.fetchall())


    def insertDBData(self):
        '''self.c.execute(""" insert into match values('Kohli',102,98,8,2,0,0,0,0,0,0,1)""")
        self.c.execute(""" insert into match values('Yuvraj',12,20,1,0,48,0,36,1,0,0,0)""")
        self.c.execute(""" insert into match values('Rhane',49,75,3,0,0,0,0,0,1,0,0)""")
        self.c.execute(""" insert into match values('Dhawan',32,35,4,0,0,0,0,0,0,0,0)""")
        self.c.execute(""" insert into match values('Dhoni',56,45,3,1,0,0,0,0,3,2,0)""")
        self.c.execute(""" insert into match values('Axar',8,4,2,0,48,2,35,1,0,0,0)""")
        self.c.execute(""" insert into match values('Pandya',42,36,3,3,30,0,25,0,1,0,0)""")
        self.c.execute(""" insert into match values('Jadeja',18,10,1,1,60,3,50,2,1,0,1)""")
        self.c.execute(""" insert into match values('Kedar',65,60,7,0,24,0,0,0,0,0,0)""")
        self.c.execute(""" insert into match values('Ashwin',23,42,3,0,60,2,45,6,0,0,0)""")
        self.c.execute(""" insert into match values('Umesh',0,0,0,0,54,0,50,4,1,0,0)""")
        self.c.execute(""" insert into match values('Bhumrah',0,0,0,0,60,2,49,1,0,0,0)""")
        self.c.execute(""" insert into match values('Bhuvaneshwar',15,12,2,0,60,1,46,2,0,0,0)""")
        self.c.execute(""" insert into match values('Rohit',46,65,5,1,0,0,0,0,1,0,0)""")
        self.c.execute(""" insert into match values('Kartick',29,42,3,0,0,0,0,0,2,0,1)""")
        '''

        # self.c.execute(""" insert into stats values('Kohli',189,8257,28,43,120,'BAT')""")
        # self.c.execute(""" insert into stats values('Yuvraj',86,3589,10,21,100,'BAT')""")
        # self.c.execute(""" insert into stats values('Rhane',158,5435,11,31,100,'BAT')""")
        # self.c.execute(""" insert into stats values('Dhawan',25,565,2,1,85,'AR')""")
        # self.c.execute(""" insert into stats values('Dhoni',78,2573,3,19,75,'BAT')""")
        # self.c.execute(""" insert into stats values('Axar',67,208,0,0,100,'BWL')""")
        # self.c.execute(""" insert into stats values('Pandya',70,77,0,0,75,'BWL')""")
        # self.c.execute(""" insert into stats values('Jadeja',16,1,0,0,85,'BWL')""")
        # self.c.execute(""" insert into stats values('Kedar',111,675,0,1,90,'BWL')""")
        # self.c.execute(""" insert into stats values('Ashwin',136,1914,0,10,100,'AR')""")
        # self.c.execute(""" insert into stats values('Umesh',296,9496,10,64,110,'WK')""")
        # self.c.execute(""" insert into stats values('Bhumrah',73,1365,0,8,60,'WK')""")
        # self.c.execute(""" insert into stats values('Bhuvaneshwar',17,289,0,2,75,'AR')""")
        # self.c.execute(""" insert into stats values('Rohit',304,8701,14,52,85,'BAT')""")
        # self.c.execute(""" insert into stats values('Kartick',11,111,0,0,75,'AR')""")

        #print('VALES insetred')

    def showAllBats(self):

        self.c.execute("select player from stats where ctg like 'BAT'")
        tmp = self.c.fetchall()

        return tmp

    def showAllBowls(self):
        self.c.execute("select player from stats where ctg like 'BWL'")
        tmp = self.c.fetchall()

        return tmp
    def showallAR(self):
        self.c.execute("select player from stats where ctg like 'AR'")
        tmp = self.c.fetchall()
        return tmp
    def showallWK(self):
        self.c.execute("select player from stats where ctg like 'WK'")
        tmp = self.c.fetchall()
        return tmp

    def getTeams(self):
        self.c.execute("select distinct name from teams")
        teams = self.c.fetchall()
        return teams
    def updateTeamTable(self,team_name,players_names,pl_categ):
        listlen = len(players_names)

        for i in range(listlen):
            points_val = self.calPoints(players_names[i],pl_categ[i])
            cmd = "insert into teams values( '" + team_name + "'," + "'"+ str(players_names[i])+"'" + ","  +str(points_val)+")"
            self.c.execute(cmd)
            #data = self.c.fetchall()

        conn.commit()

    def getPlayerScores(self,t_name):

        self.c.execute("select players from teams where name like '"+str(t_name) + "'")
        p_names = self.c.fetchall()

        self.c.execute("select value from teams where name like '" + str(t_name) + "'")
        p_scores = self.c.fetchall()
        for i in range(len(p_names)):
            t = list(p_names[i])
            q = list(p_scores[i])
            p_names[i] = t[0]
            p_scores[i] = q[0]

        return p_names,p_scores

    def calPoints(self,pl_name,ctg_name):
        value = 0
        if ctg_name=="BAT":
            cmd = "select runs from stats where player like '"+pl_name+"'"
            self.c.execute(str(cmd))
            runs = self.c.fetchall()
            runs = runs[0][0]
            cmd = "select fifty from stats where player like '" + pl_name + "'"
            self.c.execute(str(cmd))
            fifty = self.c.fetchall()
            fifty = fifty[0][0]
            cmd = "select hundereds from stats where player like '" + pl_name + "'"
            self.c.execute(str(cmd))
            hund = self.c.fetchall()
            hund = hund[0][0]
            cmd = "select faced from match where player like '" + pl_name + "'"
            self.c.execute(str(cmd))
            balls_faced = self.c.fetchall()
            balls_faced = balls_faced[0][0]
            cmd = "select fours from match where player like '" + pl_name + "'"
            self.c.execute(str(cmd))
            fours = self.c.fetchall()
            cmd = "select sixes from match where player like '" + pl_name + "'"
            self.c.execute(str(cmd))
            sixes = self.c.fetchall()
            fours=fours[0][0]
            sixes = sixes[0][0]

            #print(runs,fifty,hund,balls_faced,fours,sixes)

            value += 1* (runs//2)
            value += 5*fifty
            value +=10*hund
            value += 1*fours
            value += 2*sixes
            strike = runs//balls_faced
            if strike>=80 and strike <100:
                value+=2
            if strike >100:
                value+=4
        if ctg_name == "BOW":
            cmd = "select wkts from match where player like '" + pl_name + "'"
            self.c.execute(str(cmd))
            wkts = self.c.fetchall()
            wkts = wkts[0][0]

            cmd = "select maiden from match where player like '" + pl_name + "'"
            self.c.execute(str(cmd))
            maiden = self.c.fetchall()
            maiden = maiden[0][0]

            cmd = "select given from match where player like '" + pl_name + "'"
            self.c.execute(str(cmd))
            given = self.c.fetchall()
            given = given[0][0]

            cmd = "select bowled from match where player like '" + pl_name + "'"
            self.c.execute(str(cmd))
            bowled = self.c.fetchall()
            bowled = bowled[0][0]
            eco_rate = (bowled//6)/given

            value+=10*wkts
            value+=5*maiden
            if eco_rate >=3.5 and eco_rate<=4.5:
                value+=4
            if eco_rate >=2 and eco_rate<3.5:
                value+=7
            if eco_rate<2:
                value+=10
        if ctg_name == "AR":
            cmd = "select catches from match where player like '" + pl_name + "'"
            self.c.execute(str(cmd))
            catches = self.c.fetchall()
            cmd = "select stumping from match where player like '" + pl_name + "'"
            self.c.execute(str(cmd))
            stumping = self.c.fetchall()
            cmd = "select ro from match where player like '" + pl_name + "'"
            self.c.execute(str(cmd))
            ro = self.c.fetchall()
            catches=catches[0][0]
            stumping = stumping[0][0]
            ro = ro[0][0]
            value +=10*catches+10*stumping+10*ro

        return value;
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
class EvaluateTeams(QWidget):
    def __init__(self):
        super(EvaluateTeams,self).__init__()
        self.total_score = 0

        self.setUI()
    def setUI(self):
        uic.loadUi('eval.ui',self)
        self.setWindowIcon(QIcon("ic2.png"))
        self.getTeamNames()
        self.evalButton.clicked.connect(self.evalClicked)
        self.comboBox1.setCurrentIndex(-1)

        self.show()
    def getTeamNames(self):
        teams = DBObj.getTeams()
        for i in range(len(teams)):
            t = list(teams[i])
            teams[i] = t[0]
        self.comboBox1.addItems(teams)
        self.comboBox1.currentIndexChanged.connect(self.selectionChange)
    def selectionChange(self):
        self.listWidget1.clear()
        self.listWidget2.clear()
        player_list , scores_list = DBObj.getPlayerScores(self.comboBox1.currentText())
        for x in scores_list:
            self.listWidget2.addItem(str(x))
        self.listWidget1.addItems(player_list)
        self.total_score = sum(scores_list)

    def evalClicked(self):
        result_diag = QMessageBox()
        result_diag.about(self,"RESULT","Your Score is "+ str(self.total_score))

#------------------------------------------------------------------------------------------------------------------------
class OpenTeamDiag(QDialog):
    def __init__(self):
        super().__init__()

        self.setUI()
    def setUI(self):
        uic.loadUi('openDiag.ui', self)
        self.setWindowIcon(QIcon('opened.png'))
        self.setWindowTitle("Open Team")

        teams = DBObj.getTeams()
        for i in range(len(teams)):
            t = list(teams[i])
            teams[i] = t[0]
        self.comboBox.addItems(teams)
        self.comboBox.setCurrentIndex(-1)
        self.comboBox.currentIndexChanged.connect(self.selectChanged)
        self.ok_Button.clicked.connect(self.exitOpenDiag)
        self.cancel_button.clicked.connect(self.exitOpenDiag)
        self.show()
    def exitOpenDiag(self):
        self.close()
    def selectChanged(self):
        player_list , scores_list = DBObj.getPlayerScores(self.comboBox.currentText())
        self.listWidget1.clear()
        self.listWidget2.clear()

        #print(player_list,scores_list)
        for x in scores_list:
            self.listWidget2.addItem(str(x))
        self.listWidget1.addItems(player_list)
        total_score = 0
        total_score = sum(scores_list)
        self.tot_score.setText(str(total_score))



#-----------------------------------------------------------------------------------------------------------------------
class MainWindow(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()

        self.InitUi()
        self.bats_count =0
        self.bowl_count = 0
        self.wk_count=0
        self.allr_count=0
        self.categ =[]
        self.playerSel =[]
        self.new_Team_Check = 0
        self.tot_points_avail = 1100
        self.p_used = 0

    def InitUi(self):
        #self.setGeometry(self.left, self.top, self.width, self.height)
        uic.loadUi('main.ui', self)
        self.setWindowTitle("Fantasy Cricket")
        self.setWindowIcon(QIcon('ic2.png'))
        #adBox.setStyleSheet('QGroupBox {color: rgb(255, 0, 0);}')

        self.actionNew_Team.triggered.connect(self.NewTeamClicked)
        self.actionOpen_Team.triggered.connect(self.OpenTeamClicked)
        self.actionSave_Team.triggered.connect(self.SaveTeamClicked)
        self.actionEvaluate_Team.triggered.connect(self.EvalTeamClicked)

        self.actionNew_Team.setIcon(QIcon('new.png'))
        self.actionOpen_Team.setIcon(QIcon('opened.png'))
        self.actionSave_Team.setIcon(QIcon('save.png'))
        self.actionEvaluate_Team.setIcon(QIcon('settings.png'))
        self.actionNew_Team.setShortcut("Ctrl+N")
        self.actionOpen_Team.setShortcut("Ctrl+O")
        self.actionSave_Team.setShortcut("Ctrl+S")
        self.actionEvaluate_Team.setShortcut("Ctrl+E")


        self.model = QtGui.QStandardItemModel()
        self.listview.setModel(self.model)

        self.rBat.toggled.connect(lambda :self.radioBclicked(self.rBat))
        self.rBow.toggled.connect(lambda :self.radioBclicked(self.rBow))
        self.rAr.toggled.connect(lambda :self.radioBclicked(self.rAr))
        self.rWk.toggled.connect(lambda :self.radioBclicked(self.rWk))
        self.listWidget.itemDoubleClicked.connect(self.showDCItem)


        self.exit_button.clicked.connect(self.closeMain)
        self.help_button.setIcon(QIcon('info.png'))
        self.help_button.setIconSize(QSize(15,15))
        self.exit_button.setIcon(QIcon('exiticon.png'))
        self.help_button.clicked.connect(self.help)
        self.show()

    def radioBclicked(self,butt):

        self.listWidget.clear()
        if butt.text() == 'BAT':
            if butt.isChecked() == True :
                items = DBObj.showAllBats()
                it2 = self.debugNames(items)
                self.listWidget.addItems(it2)

            else:
                pass
        else:
            pass
        if butt.text() == 'BOW':
            if butt.isChecked()==True:
                items = DBObj.showAllBowls()
                it2 = self.debugNames(items)
                self.listWidget.addItems(it2)


            else:
                pass
        else:
            pass
        if butt.text() == 'AR':
            if butt.isChecked() == True:
                items = DBObj.showallAR()
                it2 = self.debugNames(items)
                self.listWidget.addItems(it2)
            else:
                pass
        else:
            pass

        if butt.text() == 'WK':
            if butt.isChecked() == True:
                items = DBObj.showallWK()
                it2 = self.debugNames(items)
                self.listWidget.addItems(it2)
            else:
                pass
        else:
            pass

    def debugNames(self,items):
        it2 = []
        for i in range(len(items)):
            its = str(list(items[i]))
            its = its[2:-2]
            if its not in self.playerSel:
                it2.append(its)
        return it2
    def getCheckedRBut(self):
        if self.rBat.isChecked() == True:
            return self.rBat.text()
        if self.rBow.isChecked() == True:
            return self.rBow.text()
        if self.rAr.isChecked() == True:
            return self.rAr.text()
        if self.rWk.isChecked() == True:
            return self.rWk.text()

    def NewTeamClicked(self):
        self.team_name_edit.clear()
        self.model.clear()
        self.listWidget.clear()
        self.new_Team_Check = 1
        self.rBat.setChecked(True)
        self.radioBclicked(self.rBat)
        self.playerSel=[]
        self.categ =[]
        self.p_used=0
        self.tot_points_avail = 1100
        self.bats_count = 0
        self.bowl_count = 0
        self.wk_count = 0
        self.allr_count = 0
        self.updateLabels()


    def showDCItem(self,x):
        #print(x.text())
        if self.new_Team_Check !=1:
            return;
        if self.tot_points_avail ==0:
            self.errorDiag("Sorry","No More Points available, save the team")
            return;

        if self.rWk.isChecked() == True and self.wk_count ==1:
            self.errorDiag("Selection Error","You Can't Select More Than One Wicket-keeper")
            return;
        self.playerSel.append(x.text())
        R_but_Text = self.getCheckedRBut()
        self.categ.append(R_but_Text)
        self.addToList(x)
        self.updateData(R_but_Text)

    def addToList(self,item):
        itemx = QtGui.QStandardItem(item.text())
        self.model.appendRow(itemx)
        self.deleteItem()


    def deleteItem(self):
        self.crri = self.listWidget.currentRow()
        self.listWidget.takeItem(self.crri)
    def updateData(self,item):
        if item == 'BAT':
            self.bats_count +=1
        elif item == 'BOW':
            self.bowl_count +=1
        elif item == 'AR':
            self.allr_count +=1
        elif item == 'WK':
            self.wk_count +=1

        self.tot_points_avail -=100
        self.p_used +=100
        self.updateLabels()



    def errorDiag(self,e,s):
        msg = QMessageBox()
        msg.about(self,e, s)

    def updateLabels(self):
        self.availPointsD.setText(str(self.tot_points_avail))
        self.points_used.setText(str(self.p_used))
        self.batD.setText(str(self.bats_count))
        self.bowD.setText(str(self.bowl_count))
        self.arounderD.setText(str(self.allr_count))
        self.wkDis.setText(str(self.wk_count))

    def OpenTeamClicked(self):
        self.open = OpenTeamDiag()


    def SaveTeamClicked(self):

        if self.team_name_edit.text() =="":
            self.errorDiag("Enter Team Name","Team Name Cannot Be Empty")
            return;
        DBObj.updateTeamTable(self.team_name_edit.text(),self.playerSel,self.categ)
        msg = QMessageBox()
        msg.about(self,"Notification","Team saved!")
        self.new_Team_Check = 0
    def EvalTeamClicked(self):

        self.eval = EvaluateTeams()
    def help(self):
        helpbox = QMessageBox()
        helpbox.about(self,"Instructions","""1. Select new team from ManageTeams menu.
2. Select Players accordingly and Enter Team name.
3. Select Save Team from menu, now the team is saved.
4. Select Evaluate Team from menu -> Choose team from drop down menu and click evaluate.
5. Select open Team from menu to see the details of saved teams.
** Kohli should be chosen always !!**""")

    def closeMain(self):
        self.close()
app = QApplication(sys.argv)
DBObj = DBhandler()
window = MainWindow()

conn.commit()

sys.exit(app.exec())
conn.close()
