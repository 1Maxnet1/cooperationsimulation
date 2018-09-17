#import of the needed libraries
from flask import Flask, request, render_template, url_for, redirect
import csv
import lib
app = Flask(__name__)
winnumber = 0
simwinnumber = 0
win = 'Verloren'
prize = 0
simprize = 0

@app.route('/')
def start():
    return render_template('startscreen.html')

@app.route('/willkommen')
def welcome():
    return render_template('screen1.html')

@app.route('/kooperation')
def kooperation():
    return render_template('screen2a.html')

@app.route('/nichtkooperation')
def nichtkooperation():
    return render_template('screen2b.html')


@app.route('/result')
def result():
    global win
    showwin = win
    win = 'Verloren'
    global prize
    showprize = prize
    prize = 0
    return render_template('screen3.html', winnumber=str(winnumber), win=str(showwin), prize=str(round(showprize)))


@app.route('/simulation')
def simulation():
    return render_template('simulation1.html')


@app.route('/end')
def ending():
    return render_template('simulation2.html')


@app.route('/', methods=['POST'])
def startpost():
    if request.form['submit'] == 'Experiment':
        return redirect(url_for("welcome"))
    elif request.form['submit'] == 'Simulation':
        return redirect(url_for("simulation"))
    else:
        return redirect(url_for('welcome'))


@app.route('/willkommen', methods=['POST'])
def welcomepost():
    if request.form['submit'] == 'Kooperieren':
        return redirect(url_for("kooperation"))
    elif request.form['submit'] == 'Nicht Kooperieren':
        return redirect(url_for("nichtkooperation"))
    else:
        return redirect(url_for('result'))


@app.route('/kooperation', methods=['POST'])
def kooperationpost():
    amount = int(request.form['text'])
    print('Kooperierende:' + str(amount))
    guesslist = lib.addownguess(lib.playersguess(9 - amount), 0)
    for i in range(amount):
        guesslist[len(guesslist):] = [0]
    print('Rateliste')
    print(guesslist)
    global winnumber
    winnumber = lib.findwinnumber(guesslist)
    print(winnumber)
    closeguess = lib.closestguess(guesses=guesslist, winnumber=winnumber)
    print(closeguess)
    if 9 in closeguess or len(closeguess) == 10:
        global win
        win = 'Gewonnen'
        print('Du hast ' + win)
        global prize
        prize = lib.calculateprize(closeguess)
    return redirect(url_for('result'))


@app.route('/nichtkooperation', methods=['POST'])
def nichtkooperationpost():
    guess = int(request.form['text'])
    print('Eingabe: ' + str(guess))
    guesslist = lib.addownguess(lib.playersguess(9), guess)
    print('Ratelist: ')
    print(guesslist)
    global winnumber
    winnumber = lib.findwinnumber(guesslist)
    print('Gewinnzahl:' + str(winnumber))
    if 10 in lib.closestguess(guesses=guesslist, winnumber=winnumber):
        global win
        win = 'Gewonnen'
        print(win)
        global prize
        prize = lib.calculateprize(lib.closestguess(guesses=guess, winnumber=winnumber))
    return redirect(url_for('result'))


@app.route('/result', methods=['POST'])
def resultpost():
    name = request.form['name']
    geschlecht = request.form['sex']
    alter = request.form['age']
    kursnummer = request.form['classnumber']
    kenntnis = request.form['knowledge']
    kooperiert = request.form['cooperation']
    anzahl = request.form['amount']
    zahl = request.form['number']
    grund = request.form['reason']
    print('Name: ' + str(name))
    print('Geschecht: ' + str(geschlecht))
    print('Alter: ' + str(alter))
    print('Kursnummer: ' + str(kursnummer))
    print('Kenntnis: ' + str(kenntnis))
    print('Kooperiert: ' + str(kooperiert))
    print('Anzahl: ' + str(anzahl))
    print('Zahl: ' + str(zahl))
    print('Grund: ' + str(grund))
    return redirect(url_for('start'))


@app.route('/simulation', methods=['POST'])
def end():
    repitition = int(request.form["repitition"])
    playeramount = int(request.form["playeramount"])
    knowingplayeramount = int(request.form["knowingplayeramount"])
    prizelist = []
    amount = knowingplayeramount - 1
    for i in range(repitition):
        print('Kooperierende:' + str(amount))
        guesslist = lib.addownguess(lib.playersguess(9 - amount), 0)
        for i in range(amount):
            guesslist[len(guesslist):] = [0]
        print('Rateliste')
        print(guesslist)
        global simwinnumber
        simwinnumber = lib.findwinnumber(guesslist)
        print(simwinnumber)
        closeguess = lib.closestguess(guesses=guesslist, winnumber=simwinnumber)
        print(closeguess)
        global simprize
        if 9 in closeguess or len(closeguess) == 10:
            simprize = lib.calculateprize(closeguess)
        else:
            simprize = 0
        print(simprize)
        prizelist[len(prizelist):] = [simprize]
    summe = sum(prizelist)
    averagewin = summe / repitition
    print(averagewin)
    #    distribution = lib.playersguess(playeramount - knowingplayeramount)
    #    for i in range(knowingplayeramount):
    #        distribution = lib.addownguess(distribution, 0)
    #    print(distribution)
    #    winnernumber = lib.findwinnumber(distribution)
    #    prize = lib.calculateprize(lib.closestguess(distribution,winnernumber))
    #    print(prize)
        #with open('.csv', 'a', newline='') as csvfile:
        #    writer = csv.writer(csvfile)
        #    writer.writerow(distribution)
        #with open('winningnumber.csv', 'a', newline='') as csvfile:
        #    writer = csv.writer(csvfile)
        #    writer.writerow(csvfile)
    #print('Der zu erwartende Gewinn bei ' + str(knowingplayeramount) + 'Spielern ist:')
    #print(sum(prizelist)/len(prizelist))
    return  redirect(url_for('ending'))


@app.route('/end', methods=['POST'])
def again():
    return redirect('simulation')

if __name__ == "__main__":
    app.run(use_reloader=True,host='0.0.0.0')