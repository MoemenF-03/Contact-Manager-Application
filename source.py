import csv
import tempfile
import shutil
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog
import datetime

#______main_page_____#
def verifnom(N):#fonction qui verifier un nom 
    if not N or len(N) > 30:
        return False
    return N.isalnum()

def verifemail(email):#fonction qui verifie un email institutionel
    parts = email.split('@')
    if len(parts) == 2 and parts[1] == 'isi.utm.tn':
        username = parts[0]
        if username and username.isalnum() and ' ' not in username:
            return True
    return False

def remplir1():#fonction d'ajout d'un seul contact
    n = main_window.nom.text()
    e = main_window.mail.text()
    t = main_window.tel.text()
    
    if e == "" or t == "" or n == "":
        QMessageBox.critical(main_window, "Avertissement", "Remplissez tous les champs!")
        return
    elif not verifnom(n):
        QMessageBox.critical(main_window, "Avertissement", "Le nom doit être non vide, alphanumérique et de taille maximale 30 caractères!")
        return
    elif not verifemail(e):
        QMessageBox.critical(main_window, "Avertissement", "Veuillez entrer une adresse institutionnelle valide!")
        return
    elif not (t.isdigit() and len(t) == 6):
        QMessageBox.critical(main_window, "Avertissement", "Numéro invalide")
        return
    
    # Check if email already exists
    with open("data.csv", "r", newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[2] == e:  # Check if email already exists
                QMessageBox.warning(main_window, "Avertissement", "Email already registered.")
                return

    # If email does not exist, add the new contact to the CSV file
    with open("data.csv", "a", newline='') as fichier:
        writer = csv.writer(fichier)
        writer.writerow([n, t, e])
    
    reinitialiser()
    QMessageBox.information(main_window, "Succès", "Ajoutée avec succès!")


def modifier():#fonction qui modifier un contact existant
    n = main_window.nom_cm.text()
    e = main_window.n_mail.text()
    t = main_window.n_num.text()
    if e == "" or t == "" or n == "":
        QMessageBox.critical(main_window, "Avertissement", "Remplissez tous les champs!")
    elif not verifnom(n):
        QMessageBox.critical(main_window, "Avertissement", "Le nom doit être non vide, alphanumérique et de taille maximale 30 caractères!")
    elif not verifemail(e):
        QMessageBox.critical(main_window, "Avertissement", "Veuillez entrer une adresse institutionnelle valide!")
    elif not (t.isdigit() and len(t) == 6):
        QMessageBox.critical(main_window, "Avertissement", "Numéro invalide")
    else:
        fichier_temp = tempfile.NamedTemporaryFile(mode='w', delete=False)
        modifie = False
        with open("data.csv", newline='') as fichier_csv, fichier_temp:
            lecteur_csv = csv.reader(fichier_csv)
            writer = csv.writer(fichier_temp)
            for ligne in lecteur_csv:
                if ligne and ligne[0] == n:
                    ligne[1] = t
                    ligne[2] = e
                    modifie = True
                if ligne:
                    writer.writerow(ligne)
        if modifie:
            shutil.move(fichier_temp.name, "data.csv")
            reinitialiser()
            QMessageBox.information(main_window, "Succès", "Modifiée avec succès!")
        else:
            QMessageBox.critical(main_window, "Avertissement", "Nom non trouvé dans la base de données.")

def afficher():#fonction qui affiche la liste des contact dans une text_edit de qt
    name = main_window.nom_ca.text()
    text_edit = main_window.aff 
    if name:
        with open("data.csv", newline='') as fichier_csv:
            lecteur_csv = csv.reader(fichier_csv)
            contacts = [ligne for ligne in lecteur_csv if ligne and ligne[0] == name]
            if contacts:
                output = ""
                for index, contact in enumerate(contacts, start=1):
                    output += f"[{index}] name: {contact[0]} | email: {contact[2]} | tel: {contact[1]}\n"
                text_edit.setPlainText(output)
            else:
                QMessageBox.warning(main_window, "Avertissement", "Aucune correspondance trouvée pour le nom spécifié.")
    else:
        with open("data.csv", newline='') as fichier_csv:
            lecteur_csv = csv.reader(fichier_csv)
            lines = []
            for index, ligne in enumerate(lecteur_csv, start=1):
                if ligne:
                    lines.append(f"[{index}] name: {ligne[0]} | email: {ligne[2]} | tel: {ligne[1]}")
            if lines:
                text = '\n'.join(lines)
                text_edit.setPlainText(text)
            else:
                QMessageBox.warning(main_window, "Avertissement", "Base de données vide.")


def supprimer():#fonction qui supprime un seul contact
    name = main_window.non_cs.text()
    if name:
        with open("data.csv", newline='') as fichier_csv:
            lignes = list(csv.reader(fichier_csv))
        with open("data.csv", "w", newline='') as fichier_csv:
            writer = csv.writer(fichier_csv)
            removed = False
            for ligne in lignes:
                if ligne and ligne[0] == name:
                    removed = True
                else:
                    writer.writerow(ligne)
            if removed:
                reinitialiser()
                QMessageBox.information(main_window, "Succès", "Contact supprimé avec succès!")
            else:
                QMessageBox.warning(main_window, "Avertissement", "Aucun contact trouvé avec ce nom.")
    else:
        QMessageBox.warning(main_window, "Avertissement", "Veuillez entrer un nom à supprimer.")

def vider(): # fonction qui supprime la liste des contacts
    confirmation = QMessageBox.question(main_window, "Confirmation", "Êtes-vous sûr de vouloir vider l'annuaire?", QMessageBox.Yes | QMessageBox.No)
    if confirmation == QMessageBox.Yes:
        with open("data.csv", "w", newline='') as fichier_csv:
            fichier_csv.truncate(0)
        main_window.aff.clear()
        QMessageBox.information(main_window, "Succès", "Annuaire vidé avec succès!")

def reinitialiser(): # fonction qui reinitialiser tous les champs
    main_window.nom.clear()
    main_window.mail.clear()
    main_window.tel.clear()
    main_window.nom_cm.clear()
    main_window.n_mail.clear()
    main_window.n_num.clear()
    main_window.non_cs.clear()
    main_window.nom_ca.clear()
    main_window.aff.clear()


def import_contacts(): #fonction qui import une nouvelle liste du contacts depuis une fichier csv qq
    options = QFileDialog.Options()
    file_path, _ = QFileDialog.getOpenFileName(None, "Import Contacts", "", "CSV Files (*.csv)", options=options)
    if file_path:
        
        with open(file_path, newline='') as file:
            contacts = file.read()  
        
        
        with open("data.csv", "w", newline='') as data_file:
            data_file.write(contacts)
        
        
        
        
        
        QMessageBox.information(None, "Success", "Contacts imported successfully!")
        
def ex():#fonction qui close le window actif
    main_window.close()
    QApplication.quit()
    
def keyPressEvent(event):#fonction des shortucs de clavier en page main(ctrl+..)
    if event.modifiers() == Qt.ControlModifier:
        if event.key() == Qt.Key_Q:
            main_window.close()
            QApplication.quit()
        elif event.key() == Qt.Key_R:
            reinitialiser()
        elif event.key() == Qt.Key_S:
            vider()
#end______main_page_____end#
   
   
   
#______login_page_____#

def check_login():
    global admin
    username = login_window.mail.text()
    password = login_window.passs.text()

    with open("admin_list.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 2 and row[0] == username and row[1] == password:
                login_window.close()
                main_window.show()
                admin = username
                name, domain_part = admin.split('@')
                main_window.admin.setText(name)  
                return

    QMessageBox.warning(login_window, "Login Failed", "Incorrect username or password.")
    login_window.mail.clear()
    login_window.passs.clear()

#end______login_page_____end#
    
    
#______switch_pages_____#
def go_sign():#close login and open signup
    login_window.close()
    create_window.show()
def go_log():#close signup and open login
    create_window.close()
    login_window.show()
#end______switch_pages_____end#

    
def is_valid_email(email):#simple fonction qui verifie un mail de la forme xxxxxx@xxx.xxx
    
    if '@' not in email or '.' not in email:
        return False
    
    local_part, domain_part = email.split('@')
    
    if not local_part or not domain_part:
        return False
    
    if '.' not in domain_part:
        return False
    return True

def is_valid_password(password):#simple fonction pour verifier la cohérence dune mot de pass
    return password.isalnum() and len(password) >= 4

#☺______signup page_________#
def check_signup():#fonction responsable de ajouter un nouveau admin
    email = create_window.newmail.text()
    password = create_window.newpass1.text()
    re_enter_password = create_window.newpass2.text()
    
    # Check if email and passwords are not empty
    if email and password and re_enter_password:
        # Check if passwords match
        if password == re_enter_password:
            # Check if email is in valid format
            if not is_valid_email(email):
                QMessageBox.warning(create_window, "Warning", "Please enter a valid email address.")
                create_window.newmail.clear()
                return
            # Check if password is alphanumeric and has at least 4 characters
            if not is_valid_password(password):
                QMessageBox.warning(create_window, "Warning", "Password must be alphanumeric and have at least 4 characters.")
                create_window.newpass1.clear()
                create_window.newpass2.clear()
                return
            # Check if email already exists
            with open('admin_list.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0] == email:  # Check if 'row' is not empty before accessing index
                        QMessageBox.warning(create_window, "Warning", "Email already registered. Please log in.")
                        
                        return
            # If email does not exist and password is valid, add it to the CSV file
            with open('admin_list.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([email, password])
                QMessageBox.information(create_window, "Success", "Account created successfully. Please log in.")
                go_log()
        else:
            QMessageBox.warning(create_window, "Warning", "Passwords do not match.")
            create_window.newpass2.clear()
    else:
        QMessageBox.warning(create_window, "Warning", "Please fill in all fields.")
#end______signup page_________end#
        
        
##################Programme Principale###################
        
app = QApplication([])

#attribuer des nom au variable des widgets
main_window = loadUi("qt.ui")
login_window = loadUi("login.ui")
create_window = loadUi("create.ui")

#caractéristiques du page login
login_window.show()
login_window.enter.clicked.connect(check_login)
login_window.sign.clicked.connect(go_sign)

#caractéristiques du page signup
create_window.create.clicked.connect(check_signup)
create_window.gologin.clicked.connect(go_log)




#caractéristiques du page principale
d = datetime.datetime.now().strftime("%Y-%m-%d")
main_window.date.setText(d)

main_window.ajouter.clicked.connect(remplir1)  # enregistrer un neavau contact
main_window.modifier.clicked.connect(modifier)  # modifier un contact existant deja
main_window.afficher.clicked.connect(afficher)  # affichage 
main_window.supprimer.clicked.connect(supprimer)  # supprission d'un contact
main_window.vider.clicked.connect(vider)  # supprission de touts les contacts
main_window.reini.clicked.connect(reinitialiser)  # vider tous les cases textes
main_window.upload.clicked.connect(import_contacts) # button pour importer des contact d'un fichier csv autre que notre
main_window.qtt.clicked.connect(ex) #fermer le programme

main_window.keyPressEvent = keyPressEvent #activer les event keypress(les shortcuts CTRL + .. )

app.exec_()
